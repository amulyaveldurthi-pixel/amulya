import re
import PyPDF2

# List of known skills (you can expand this anytime)
KNOWN_SKILLS = [
    "python", "java", "sql", "machine learning",
    "data analysis", "html", "css", "javascript",
    "aws", "cloud", "git", "excel",
    "statistics", "pandas", "numpy", "visualization",
    "flask", "django", "react"
]

# -------------------------
# PDF TEXT EXTRACTION
# -------------------------
def extract_text_from_pdf(filepath):
    text = ""
    with open(filepath, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()
    return text


# -------------------------
# SKILL EXTRACTION
# -------------------------
def extract_skills_from_text(text):
    text = text.lower()
    found_skills = []

    for skill in KNOWN_SKILLS:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.append(skill)

    return list(set(found_skills))