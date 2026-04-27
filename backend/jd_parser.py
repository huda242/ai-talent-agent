def parse_jd(jd_text):
    skills_list = ["Python", "Flask", "SQL", "Django", "React", "Node.js", "Java"]

    extracted_skills = []
    for skill in skills_list:
        if skill.lower() in jd_text.lower():
            extracted_skills.append(skill)

    experience = 0
    import re
    match = re.search(r'(\d+)\+?\s*years', jd_text)
    if match:
        experience = int(match.group(1))

    return {
        "skills": extracted_skills,
        "experience": experience
    }