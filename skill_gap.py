def calculate_skill_gap(user_skills, job_required_skills):
    user_skills = [s.lower().strip() for s in user_skills]
    job_required_skills = [s.lower().strip() for s in job_required_skills]

    missing = [skill for skill in job_required_skills if skill not in user_skills]

    match_percentage = int(
        ((len(job_required_skills) - len(missing)) / len(job_required_skills)) * 100
    )

    return match_percentage, missing