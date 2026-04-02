import os
import sqlite3
import uuid #user unique id
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import requests
import re

from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from course_recommender import recommend_courses
import pdfplumber
import docx


# ---------------- CREATE FLASK ----------------
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}


# ---------------- LOAD JOB ROLES ----------------
def load_job_roles():
    try:
        df = pd.read_csv("job_roles_skills.csv")
        roles = df["job_role"].dropna().astype(str).tolist()
        return roles
    except Exception as e:
        print("Error loading job roles:", e)
        return []


# ---------------- LOAD ALL SKILLS ----------------
def load_all_skills():
    try:
        df = pd.read_csv("job_roles_skills.csv")

        all_skills = set()

        for skills in df["skills"].dropna():
            for skill in skills.split(","):
                all_skills.add(skill.strip())

        return sorted(list(all_skills))

    except Exception as e:
        print("Error loading skills:", e)
        return []


JOB_ROLES = load_job_roles()
ALL_SKILLS = load_all_skills()


# ---------------- FILE CHECK ----------------
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------- RESUME TEXT EXTRACTION ----------------
def extract_text_from_resume(filepath):

    text = ""

    if filepath.endswith(".pdf"):
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    elif filepath.endswith(".docx"):
        doc = docx.Document(filepath)
        for para in doc.paragraphs:
            text += para.text + " "

    return text.lower()


# ---------------- ROLE SKILLS ----------------
def get_role_skills(role):

    df = pd.read_csv("job_roles_skills.csv")

    role_data = df[df["job_role"].str.lower() == role.lower()]

    skills_list = []

    for skills in role_data["skills"].dropna():

        split_skills = skills.lower().split(",")

        for skill in split_skills:
            skills_list.append(skill.strip())

    return skills_list
# ---------------- MULTI JOB PORTAL LINKS ----------------
def generate_job_portal_links(keyword):

    keyword = keyword.replace(" ", "+")

    portals = {
        "LinkedIn": f"https://www.linkedin.com/jobs/search/?keywords={keyword}",
        "Indeed": f"https://www.indeed.com/jobs?q={keyword}",
        "Naukri": f"https://www.naukri.com/{keyword}-jobs",
        "Glassdoor": f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={keyword}",
        "Monster": f"https://www.monster.com/jobs/search/?q={keyword}",
        "Foundit": f"https://www.foundit.in/srp/results?query={keyword}"
    }

    return portals


# ---------------- DATABASE ----------------
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_users_table():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


create_users_table()


# ---------------- AUTH SYSTEM ----------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not username or not email or not password:
            return "All fields required!"

        hashed_password = generate_password_hash(password)

        try:

            conn = get_db_connection()

            conn.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, hashed_password)
            )

            conn.commit()
            conn.close()

            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            return "Email already exists!"

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()

        conn.close()

        if user is None:
            return "User not found!"

        if not check_password_hash(user["password"], password):
            return "Wrong password!"

        session["user_id"] = user["id"]
        session["username"] = user["username"]

        return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


# ---------------- SKILL → ROLE RECOMMENDATION ----------------
@app.route("/recommend_roles", methods=["POST"])
def recommend_roles_route():

    skills_input = request.form.get("skills")

    if not skills_input:
        return redirect(url_for("home"))

    user_skills = [s.strip().lower() for s in skills_input.split(",")]

    df = pd.read_csv("job_roles_skills.csv")

    best_role = None
    best_match_count = 0
    role_skills = []

    for _, row in df.iterrows():

        role = row["job_role"]
        skills = [s.strip().lower() for s in str(row["skills"]).split(",")]

        match_count = len(set(user_skills) & set(skills))

        if match_count > best_match_count:
            best_match_count = match_count
            best_role = role
            role_skills = skills

    if not best_role:
        return redirect(url_for("home"))

    matched_skills = list(set(user_skills) & set(role_skills))
    missing_skills = list(set(role_skills) - set(user_skills))

    courses = recommend_courses(missing_skills)

    # -------- JOB API --------
    adzuna_url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": "e9e9f4c0",
        "app_key": "32a8fb5bc5f30025d3359d7bda6032f1",
        "results_per_page": 10,
        "what": best_role
    }

    jobs = []

    try:
        response = requests.get(adzuna_url, params=params)
        data = response.json()

        if "results" in data:
            jobs = data["results"]

    except Exception as e:
        print("Job API error:", e)

    portal_links = generate_job_portal_links(best_role)

    username = session.get("username")

# generate multi-platform search links
    portal_links = generate_job_portal_links(best_role)

    return render_template(
        "index.html",
        username=username,
        roles=JOB_ROLES,
        skills=ALL_SKILLS,
        skill_roles=True,
        best_role=best_role,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        courses=courses,
        jobs=jobs,
        portal_links=portal_links
    )


# ---------------- APPLY REDIRECT ----------------
@app.route("/apply", methods=["POST"])
def apply():
    job_url = request.form.get("job_url")
    return redirect(job_url)


# ---------------- MAIN ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    username = session.get("username")
    visualization_path = None

    if request.method == "POST":

        role = request.form.get("role")
        resume = request.files.get("resume")

        if not role or not resume or not allowed_file(resume.filename):

            return render_template(
                "index.html",
                result=None,
                username=username,
                roles=JOB_ROLES,
                skills=ALL_SKILLS
            )

        filename = f"{uuid.uuid4().hex}_{resume.filename}"

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        resume.save(filepath)

        resume_text = extract_text_from_resume(filepath)

        role_skills = get_role_skills(role)

        matched_skills = []
        unmatched_skills = []

        resume_words = set(re.findall(r'\b\w+\b', resume_text))

        for skill in role_skills:

            skill_words = skill.lower().split()

            if all(word in resume_words for word in skill_words):
                matched_skills.append(skill)
            else:
                unmatched_skills.append(skill)

        total_skills = len(role_skills)

        match_percentage = 0

        if total_skills > 0:
            match_percentage = (len(matched_skills) / total_skills) * 100

        # -------- PIE CHART --------
        plt.figure(figsize=(6, 6))

        plt.pie(
            [match_percentage, 100 - match_percentage],
            labels=["Match", "Gap"],
            autopct="%1.1f%%"
        )

        plt.title("Overall Resume Fitness")

        vis_filename = f"{uuid.uuid4().hex}_fitness.png"

        save_path = os.path.join("static", vis_filename)

        plt.savefig(save_path)

        plt.close()

        visualization_path = vis_filename

        courses = recommend_courses(unmatched_skills)
        portal_links = generate_job_portal_links(role)

        # -------- JOB API --------
        adzuna_url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

        params = {
            "app_id": "e9e9f4c0",
            "app_key": "32a8fb5bc5f30025d3359d7bda6032f1",
            "results_per_page": 10,
            "what": role
        }

        jobs = []

        try:

            response = requests.get(adzuna_url, params=params)
            data = response.json()

            if "results" in data:
                jobs = data["results"]

        except Exception as e:
            print("Adzuna API error:", e)

        result = {
            "match_percentage": round(match_percentage, 1),
            "matched_skills": matched_skills,
            "unmatched_skills": unmatched_skills,
            "courses": courses,
            "jobs": jobs
        }

        if os.path.exists(filepath):
            os.remove(filepath)

    return render_template(
    "index.html",
    result=result,
    username=username,
    visualization_path=visualization_path,
    roles=JOB_ROLES,
    skills=ALL_SKILLS,
    portal_links=portal_links if request.method == "POST" else None
)


if __name__ == "__main__":
    app.run(debug=True)