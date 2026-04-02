def calculate_skill_gap(user_skills, job_skills):
    missing = [skill for skill in job_skills if skill not in user_skills]

    return {
        "missing_skills": missing,
        "match_percentage": round(
            (len(job_skills) - len(missing)) / len(job_skills) * 100
        ) if job_skills else 0
    }