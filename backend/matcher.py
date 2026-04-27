def calculate_match(candidate, jd_data):
    candidate_skills = set(candidate["skills"])
    jd_skills = set(jd_data["skills"])

    if len(jd_skills) == 0:
        skill_match = 0
    else:
        skill_match = len(candidate_skills & jd_skills) / len(jd_skills)

    exp_match = 1 if candidate["experience"] >= jd_data["experience"] else 0

    match_score = (skill_match * 0.7) + (exp_match * 0.3)

    explanation = f"Matched {len(candidate_skills & jd_skills)}/{len(jd_skills)} skills"

    return round(match_score * 100, 2), explanation