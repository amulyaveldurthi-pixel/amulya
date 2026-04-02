import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS job_roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS role_skills (
    role_id INTEGER,
    skill_id INTEGER,
    FOREIGN KEY (role_id) REFERENCES job_roles(id),
    FOREIGN KEY (skill_id) REFERENCES skills(id)
)
""")

# Insert sample data
roles_data = {
    "data analyst": ["python", "sql", "excel", "power bi", "statistics"],
    "backend developer": ["python", "django", "flask", "sql", "api"],
    "frontend developer": ["html", "css", "javascript", "react"],
    "machine learning engineer": ["python", "tensorflow", "pytorch", "machine learning"],
    "software engineer": ["python", "java", "c++", "data structures"]
}

for role, skills in roles_data.items():

    # Insert role
    cursor.execute("INSERT OR IGNORE INTO job_roles (role_name) VALUES (?)", (role,))
    cursor.execute("SELECT id FROM job_roles WHERE role_name = ?", (role,))
    role_id = cursor.fetchone()[0]

    for skill in skills:
        # Insert skill
        cursor.execute("INSERT OR IGNORE INTO skills (skill_name) VALUES (?)", (skill,))
        cursor.execute("SELECT id FROM skills WHERE skill_name = ?", (skill,))
        skill_id = cursor.fetchone()[0]

        # Link role & skill
        cursor.execute(
            "INSERT INTO role_skills (role_id, skill_id) VALUES (?, ?)",
            (role_id, skill_id)
        )

conn.commit()
conn.close()

print("Database created successfully with correct tables.")