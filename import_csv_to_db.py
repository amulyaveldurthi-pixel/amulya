import sqlite3
import csv

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

with open("job_roles_skills.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        role = row["job_role"].strip().lower()
        skill = row["skills"].strip().lower()

        # Insert role
        cursor.execute(
            "INSERT OR IGNORE INTO job_roles (role_name) VALUES (?)",
            (role,)
        )

        cursor.execute(
            "SELECT id FROM job_roles WHERE role_name = ?",
            (role,)
        )
        role_id = cursor.fetchone()[0]

        # Insert skill
        cursor.execute(
            "INSERT OR IGNORE INTO skills (skill_name) VALUES (?)",
            (skill,)
        )

        cursor.execute(
            "SELECT id FROM skills WHERE skill_name = ?",
            (skill,)
        )
        skill_id = cursor.fetchone()[0]

        # Prevent duplicate mapping
        cursor.execute(
            "SELECT 1 FROM role_skills WHERE role_id=? AND skill_id=?",
            (role_id, skill_id)
        )

        if not cursor.fetchone():
            cursor.execute(
                "INSERT INTO role_skills (role_id, skill_id) VALUES (?, ?)",
                (role_id, skill_id)
            )

conn.commit()
conn.close()

print("CSV imported successfully.")