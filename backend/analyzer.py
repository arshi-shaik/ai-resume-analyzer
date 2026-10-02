import re


SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "go",
    "rust",
    "kotlin",
    "swift",
    "php",
    "ruby",
    "scala",
    "r",

    "html",
    "css",
    "react",
    "angular",
    "vue",
    "next.js",
    "node.js",
    "express",
    "django",
    "flask",
    "fastapi",
    "spring boot",
    "bootstrap",
    "tailwind css",
    "jquery",
    "redux",
    "graphql",

    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "oracle",
    "sqlite",
    "sql server",
    "redis",
    "cassandra",
    "firebase",
    "dynamodb",
    "mariadb",
    "database management",
    "database design",

    "data structures",
    "algorithms",
    "data structures and algorithms",
    "dsa",
    "oops",
    "oop",
    "object oriented programming",
    "dbms",
    "operating systems",
    "computer networks",
    "system design",
    "distributed systems",

    "artificial intelligence",
    "ai",
    "machine learning",
    "ml",
    "deep learning",
    "natural language processing",
    "nlp",
    "computer vision",
    "generative ai",
    "genai",
    "large language models",
    "llm",
    "prompt engineering",
    "neural networks",
    "predictive modeling",
    "recommendation systems",

    "tensorflow",
    "pytorch",
    "scikit-learn",
    "keras",
    "opencv",
    "yolo",
    "hugging face",
    "transformers",
    "spacy",
    "nltk",
    "xgboost",

    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scipy",
    "data science",
    "data analysis",
    "data analytics",
    "statistics",
    "data visualization",
    "power bi",
    "tableau",
    "excel",
    "google sheets",
    "etl",
    "feature engineering",

    "aws",
    "azure",
    "google cloud",
    "gcp",
    "cloud computing",

    "docker",
    "kubernetes",
    "jenkins",
    "terraform",
    "ansible",
    "github actions",
    "gitlab ci",
    "ci/cd",
    "devops",
    "linux",
    "unix",
    "nginx",
    "apache",

    "git",
    "github",
    "gitlab",
    "bitbucket",

    "rest api",
    "rest",
    "soap",
    "web services",
    "api",
    "authentication",
    "authorization",
    "jwt",
    "oauth",
    "json",
    "xml",
    "microservices",

    "software testing",
    "unit testing",
    "integration testing",
    "system testing",
    "manual testing",
    "automation testing",
    "selenium",
    "junit",
    "pytest",
    "postman",
    "api testing",

    "vs code",
    "visual studio code",
    "intellij",
    "eclipse",
    "pycharm",
    "jupyter",
    "google colab",
    "jira",
    "trello",
    "figma",
    "canva",
    "streamlit",

    "android",
    "ios",
    "flutter",
    "react native",
    "android studio",

    "cybersecurity",
    "information security",
    "network security",
    "ethical hacking",
    "penetration testing",
    "cryptography",
    "security testing",

    "project management",
    "agile",
    "scrum",
    "kanban",
    "product management",
    "planning",
    "risk management",

    "communication",
    "verbal communication",
    "written communication",
    "effective communication",
    "teamwork",
    "team player",
    "collaboration",
    "leadership",
    "problem solving",
    "critical thinking",
    "analytical thinking",
    "decision making",
    "time management",
    "adaptability",
    "flexibility",
    "creativity",
    "attention to detail",
    "interpersonal skills",
    "organizational skills",
    "presentation skills",
    "negotiation",
    "conflict resolution",
    "work ethic",
    "self motivation",
    "emotional intelligence",
    "active listening",
    "learning ability",
    "quick learner",
    "multitasking",
    "customer service",
    "mentoring",
    "coaching",
    "research skills",
    "professionalism",
    "reliability",
    "accountability",
    "team management",

    "business analysis",
    "business intelligence",
    "strategy",
    "market research",
    "crm",
    "sales",
    "marketing",
    "digital marketing",
    "content writing",
    "technical writing",

    "research",
    "documentation",
    "debugging",
    "troubleshooting",
    "requirements analysis",
    "requirements gathering",
    "software development",
    "software development life cycle",
    "sdlc"
}


ALIASES = {
    "js": "javascript",
    "ts": "typescript",
    "reactjs": "react",
    "react.js": "react",
    "nodejs": "node.js",
    "node": "node.js",
    "expressjs": "express",
    "express.js": "express",
    "nextjs": "next.js",
    "vuejs": "vue",
    "vue.js": "vue",
    "springboot": "spring boot",
    "postgres": "postgresql",
    "mongo": "mongodb",
    "k8s": "kubernetes",
    "golang": "go",
    "sklearn": "scikit-learn",
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "nlp": "natural language processing",
    "llm": "large language models",
    "genai": "generative ai",
    "gcp": "google cloud",
    "powerbi": "power bi",
    "oop": "object oriented programming",
    "oops": "object oriented programming",
    "dsa": "data structures and algorithms",
    "problem-solving": "problem solving",
    "decision-making": "decision making",
    "self-motivation": "self motivation",
    "team player": "teamwork",
    "leadership skills": "leadership",
    "adaptable": "adaptability",
    "quick learner": "learning ability"
}


def normalize_text(text):
    text = text.lower()
    text = text.replace("–", "-")
    text = text.replace("—", "-")
    text = text.replace("_", " ")
    return text


def normalize_skill(skill):
    skill = skill.lower().strip()

    if skill in ALIASES:
        return ALIASES[skill]

    return skill


def extract_skills(text):
    text = normalize_text(text)

    found_skills = set()

    for skill in SKILLS:
        normalized_skill = normalize_skill(skill)

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.add(normalized_skill)

    for alias, original in ALIASES.items():
        pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.add(original)

    return sorted(found_skills)


def calculate_match(resume_text, job_description):
    resume_skills = set(
        extract_skills(resume_text)
    )

    job_skills = set(
        extract_skills(job_description)
    )

    if not job_skills:
        return {
            "match_percentage": 0,
            "matched_skills": [],
            "missing_skills": []
        }

    matched_skills = (
        resume_skills.intersection(job_skills)
    )

    missing_skills = (
        job_skills - resume_skills
    )

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


def get_skill_categories(skills):
    categories = {
        "Programming": [],
        "Web Development": [],
        "Database": [],
        "AI/ML": [],
        "Data": [],
        "Cloud": [],
        "DevOps": [],
        "Testing": [],
        "Security": [],
        "Soft Skills": [],
        "Business": [],
        "Other": []
    }

    programming = {
        "python",
        "java",
        "c",
        "c++",
        "c#",
        "javascript",
        "typescript",
        "go",
        "rust",
        "kotlin",
        "swift",
        "php",
        "ruby",
        "scala",
        "r"
    }

    web = {
        "html",
        "css",
        "react",
        "angular",
        "vue",
        "next.js",
        "node.js",
        "express",
        "django",
        "flask",
        "fastapi",
        "spring boot",
        "bootstrap",
        "tailwind css",
        "jquery",
        "redux",
        "graphql"
    }

    database = {
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "oracle",
        "sqlite",
        "sql server",
        "redis",
        "cassandra",
        "firebase",
        "dynamodb",
        "mariadb",
        "database management",
        "database design",
        "dbms"
    }

    ai_ml = {
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "natural language processing",
        "computer vision",
        "generative ai",
        "large language models",
        "prompt engineering",
        "neural networks",
        "predictive modeling",
        "recommendation systems",
        "tensorflow",
        "pytorch",
        "scikit-learn",
        "keras",
        "opencv",
        "yolo",
        "hugging face",
        "transformers",
        "spacy",
        "nltk",
        "xgboost"
    }

    data = {
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scipy",
        "data science",
        "data analysis",
        "data analytics",
        "statistics",
        "data visualization",
        "power bi",
        "tableau",
        "excel",
        "google sheets",
        "etl",
        "feature engineering"
    }

    cloud = {
        "aws",
        "azure",
        "google cloud",
        "cloud computing"
    }

    devops = {
        "docker",
        "kubernetes",
        "jenkins",
        "terraform",
        "ansible",
        "github actions",
        "gitlab ci",
        "ci/cd",
        "devops",
        "linux",
        "unix",
        "nginx",
        "apache",
        "git",
        "github",
        "gitlab",
        "bitbucket"
    }

    testing = {
        "software testing",
        "unit testing",
        "integration testing",
        "system testing",
        "manual testing",
        "automation testing",
        "selenium",
        "junit",
        "pytest",
        "postman",
        "api testing"
    }

    security = {
        "cybersecurity",
        "information security",
        "network security",
        "ethical hacking",
        "penetration testing",
        "cryptography",
        "security testing"
    }

    soft = {
        "communication",
        "teamwork",
        "collaboration",
        "leadership",
        "problem solving",
        "critical thinking",
        "analytical thinking",
        "decision making",
        "time management",
        "adaptability",
        "flexibility",
        "creativity",
        "attention to detail",
        "interpersonal skills",
        "organizational skills",
        "presentation skills",
        "negotiation",
        "conflict resolution",
        "work ethic",
        "self motivation",
        "emotional intelligence",
        "active listening",
        "learning ability",
        "quick learner",
        "multitasking",
        "customer service"
    }

    business = {
        "business analysis",
        "business intelligence",
        "strategy",
        "market research",
        "crm",
        "sales",
        "marketing",
        "digital marketing",
        "content writing",
        "technical writing"
    }

    for skill in skills:
        if skill in programming:
            categories["Programming"].append(skill)

        elif skill in web:
            categories["Web Development"].append(skill)

        elif skill in database:
            categories["Database"].append(skill)

        elif skill in ai_ml:
            categories["AI/ML"].append(skill)

        elif skill in data:
            categories["Data"].append(skill)

        elif skill in cloud:
            categories["Cloud"].append(skill)

        elif skill in devops:
            categories["DevOps"].append(skill)

        elif skill in testing:
            categories["Testing"].append(skill)

        elif skill in security:
            categories["Security"].append(skill)

        elif skill in soft:
            categories["Soft Skills"].append(skill)

        elif skill in business:
            categories["Business"].append(skill)

        else:
            categories["Other"].append(skill)

    return categories