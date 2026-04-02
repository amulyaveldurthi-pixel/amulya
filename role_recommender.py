import pandas as pd

def recommend_roles(user_skills):

    df = pd.read_csv("job_roles_skills.csv")

    # user input skills
    user_skills = [s.strip().lower() for s in user_skills.split(",")]

    role_scores = {}

    for index, row in df.iterrows():

        role = row["job_role"]

        skills = str(row["skills"]).lower().split(",")

        skills = [s.strip() for s in skills]

        match_count = 0

        for skill in user_skills:
            if skill in skills:
                match_count += 1

        if match_count > 0:
            role_scores[role] = match_count

    # sort roles by match score
    sorted_roles = sorted(role_scores.items(), key=lambda x: x[1], reverse=True)

    # return top roles
    return [role for role, score in sorted_roles[:8]]