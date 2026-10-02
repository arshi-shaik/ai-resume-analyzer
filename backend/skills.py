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
    "golang",
    "rust",
    "kotlin",
    "swift",
    "php",
    "ruby",
    "scala",
    "r",
    "dart",
    "perl",
    "bash",
    "shell scripting",

    "html",
    "html5",
    "css",
    "css3",
    "react",
    "reactjs",
    "angular",
    "vue",
    "vue.js",
    "next.js",
    "nextjs",
    "node.js",
    "nodejs",
    "node",
    "express",
    "express.js",
    "django",
    "flask",
    "fastapi",
    "spring",
    "spring boot",
    "springboot",
    "asp.net",
    "bootstrap",
    "tailwind css",
    "jquery",
    "redux",
    "graphql",
    "rest api",
    "rest",
    "web development",
    "frontend development",
    "backend development",
    "full stack development",

    "sql",
    "mysql",
    "postgresql",
    "postgres",
    "mongodb",
    "oracle",
    "sqlite",
    "microsoft sql server",
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
    "object oriented programming",
    "object oriented design",
    "oops",
    "dbms",
    "database management systems",
    "operating systems",
    "computer networks",
    "computer architecture",
    "software engineering",
    "system design",
    "distributed systems",
    "computer science",

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
    "reinforcement learning",
    "neural networks",
    "predictive modeling",
    "recommendation systems",
    "speech recognition",

    "tensorflow",
    "pytorch",
    "scikit-learn",
    "sklearn",
    "keras",
    "opencv",
    "yolo",
    "yolov8",
    "hugging face",
    "transformers",
    "spacy",
    "nltk",
    "xgboost",
    "lightgbm",

    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scipy",
    "data science",
    "data analysis",
    "data analytics",
    "statistical analysis",
    "statistics",
    "data visualization",
    "power bi",
    "tableau",
    "microsoft excel",
    "excel",
    "google sheets",
    "etl",
    "data preprocessing",
    "feature engineering",

    "aws",
    "amazon web services",
    "azure",
    "microsoft azure",
    "google cloud",
    "gcp",
    "cloud computing",
    "aws ec2",
    "aws s3",
    "aws lambda",
    "azure functions",

    "docker",
    "kubernetes",
    "k8s",
    "jenkins",
    "terraform",
    "ansible",
    "github actions",
    "gitlab ci",
    "ci/cd",
    "continuous integration",
    "continuous deployment",
    "devops",
    "linux",
    "unix",
    "nginx",
    "apache",

    "git",
    "github",
    "gitlab",
    "bitbucket",
    "version control",
    "source control",

    "api",
    "soap",
    "microservices",
    "web services",
    "api development",
    "api integration",
    "authentication",
    "authorization",
    "jwt",
    "oauth",
    "json",
    "xml",

    "software testing",
    "unit testing",
    "integration testing",
    "system testing",
    "manual testing",
    "automation testing",
    "test automation",
    "selenium",
    "junit",
    "pytest",
    "postman",
    "api testing",

    "visual studio code",
    "vs code",
    "intellij idea",
    "eclipse",
    "pycharm",
    "jupyter notebook",
    "google colab",
    "jira",
    "trello",
    "figma",
    "canva",
    "streamlit",

    "android",
    "android development",
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
    "project planning",
    "risk management",

    "communication",
    "verbal communication",
    "written communication",
    "effective communication",
    "teamwork",
    "team player",
    "team collaboration",
    "collaboration",
    "leadership",
    "leadership skills",
    "problem solving",
    "problem-solving",
    "critical thinking",
    "analytical thinking",
    "decision making",
    "decision-making",
    "time management",
    "adaptability",
    "adaptable",
    "flexibility",
    "creativity",
    "creative thinking",
    "attention to detail",
    "interpersonal skills",
    "organizational skills",
    "presentation skills",
    "negotiation",
    "conflict resolution",
    "work ethic",
    "self motivation",
    "self-motivation",
    "emotional intelligence",
    "active listening",
    "learning ability",
    "quick learner",
    "multitasking",
    "planning",
    "customer service",
    "mentoring",
    "coaching",
    "research skills",
    "analytical skills",
    "decision making skills",
    "professionalism",
    "reliability",
    "accountability",
    "team management",
    "interpersonal communication",

    "business analysis",
    "business intelligence",
    "business strategy",
    "market research",
    "customer relationship management",
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
    "javascript": "javascript",
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
    "ms excel": "excel",
    "powerbi": "power bi",
    "oop": "object oriented programming",
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
    text = re.sub(r"[/|,;:()\[\]{}]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def normalize_skill(skill):
    skill = skill.lower().strip()

    if skill in ALIASES:
        return ALIASES[skill]

    return skill

def extract_skills(text):
    text = normalize_text(text)

    found_skills = set()

    for skill in SKILLS:
        skill_normalized = skill.lower()

        pattern = r"(?<!\w)" + re.escape(skill_normalized) + r"(?!\w)"

        if re.search(pattern, text):
            standard_skill = normalize_skill(skill)
            found_skills.add(standard_skill)

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

    matched_skills = resume_skills.intersection(
        job_skills
    )

    missing_skills = job_skills.difference(
        resume_skills
    )

    match_percentage = (
        len(matched_skills) /
        len(job_skills)
    ) * 100

    return {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills)
    }

def get_skill_categories():
    return {
        "Programming Languages": [
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
            "swift"
        ],

        "Web Development": [
            "html",
            "css",
            "react",
            "angular",
            "vue",
            "node.js",
            "express",
            "django",
            "flask",
            "fastapi",
            "spring boot"
        ],

        "Databases": [
            "sql",
            "mysql",
            "postgresql",
            "mongodb",
            "oracle",
            "redis",
            "sqlite"
        ],

        "AI & Machine Learning": [
            "artificial intelligence",
            "machine learning",
            "deep learning",
            "natural language processing",
            "computer vision",
            "generative ai",
            "tensorflow",
            "pytorch",
            "scikit-learn"
        ],

        "Data & Analytics": [
            "pandas",
            "numpy",
            "power bi",
            "tableau",
            "excel",
            "data analysis",
            "data science"
        ],

        "Cloud & DevOps": [
            "aws",
            "azure",
            "google cloud",
            "docker",
            "kubernetes",
            "jenkins",
            "terraform",
            "devops"
        ],

        "Computer Science": [
            "data structures",
            "algorithms",
            "object oriented programming",
            "dbms",
            "operating systems",
            "computer networks",
            "system design"
        ],

        "Soft Skills": [
            "communication",
            "teamwork",
            "collaboration",
            "leadership",
            "problem solving",
            "critical thinking",
            "time management",
            "adaptability",
            "creativity",
            "attention to detail",
            "interpersonal skills",
            "presentation skills",
            "learning ability",
            "professionalism"
        ]
    }
