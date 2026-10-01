import re


# Technical skills that our analyzer can detect
SKILLS = {
    "python",
    "java",
    "javascript",
    "typescript",
    "react",
    "node.js",
    "node",
    "express",
    "html",
    "css",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "git",
    "github",
    "docker",
    "redis",
    "aws",
    "azure",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "power bi",
    "fastapi",
    "spring boot",
    "rest api",
    "rest",
    "api",
    "data structures",
    "algorithms",
    "oops",
    "object oriented programming",
    "communication",
    "problem solving"
}


def extract_skills(text):
    """
    Find technical and professional skills
    mentioned in the given text.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        # Escape special characters such as "." in node.js
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill)

    return sorted(found_skills)


def calculate_match(resume_text, job_description):
    """
    Compare skills found in the resume
    with skills required in the job description.
    """

    resume_skills = set(
        extract_skills(resume_text)
    )

    job_skills = set(
        extract_skills(job_description)
    )


    # If the job description doesn't contain
    # any recognized skills
    if not job_skills:

        return {
            "match_percentage": 0,
            "matched_skills": [],
            "missing_skills": []
        }


    # Skills appearing in both resume and job
    matched_skills = (
        resume_skills.intersection(job_skills)
    )


    # Skills required by job but not found
    # in the resume
    missing_skills = (
        job_skills - resume_skills
    )


    # Calculate percentage
    match_percentage = (
        len(matched_skills)
        / len(job_skills)
    ) * 100


    return {
        "match_percentage": round(
            match_percentage,
            2
        ),

        "matched_skills": sorted(
            matched_skills
        ),

        "missing_skills": sorted(
            missing_skills
        )
    }
