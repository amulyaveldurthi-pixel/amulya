#def recommend_courses(missing_skills):

course_database = {

        "A/B Testing": "https://www.coursera.org/search?query=A/B%20Testing",
        "AI Optimization": "https://www.coursera.org/search?query=AI%20Optimization",
        "API Writing": "https://www.coursera.org/search?query=API%20Writing",
        "APIs": "https://www.coursera.org/search?query=APIs",
        "ARCore": "https://www.coursera.org/search?query=ARCore",
        "ARKit": "https://www.coursera.org/search?query=ARKit",
        "ATS": "https://www.coursera.org/search?query=ATS",
        "AWS": "https://www.coursera.org/search?query=AWS",
        "Active Directory": "https://www.coursera.org/search?query=Active%20Directory",
        "Agile": "https://www.coursera.org/search?query=Agile",
        "Airflow": "https://www.coursera.org/search?query=Airflow",
        "Analytics": "https://www.coursera.org/search?query=Analytics",
        "Android SDK": "https://www.coursera.org/search?query=Android%20SDK",
        "Angular": "https://www.coursera.org/search?query=Angular",
        "Apex": "https://www.coursera.org/search?query=Apex",
        "Auditing": "https://www.coursera.org/search?query=Auditing",
        "AutoCAD": "https://www.coursera.org/search?query=AutoCAD",
        "Automation Testing": "https://www.coursera.org/search?query=Automation%20Testing",
        "Azure": "https://www.coursera.org/search?query=Azure",
        "Behavioral Therapy": "https://www.coursera.org/search?query=Behavioral%20Therapy",
        "Branding": "https://www.coursera.org/search?query=Branding",
        "Budgeting": "https://www.coursera.org/search?query=Budgeting",
        "Business Process": "https://www.coursera.org/search?query=Business%20Process",
        "C": "https://www.coursera.org/search?query=C",
        "C#": "https://www.coursera.org/search?query=C%23",
        "C++": "https://www.coursera.org/search?query=C%2B%2B",
        "CI/CD": "https://www.coursera.org/search?query=CI/CD",
        "CRM": "https://www.coursera.org/search?query=CRM",
        "CSS": "https://www.coursera.org/search?query=CSS",
        "Campaign Management": "https://www.coursera.org/search?query=Campaign%20Management",
        "Campaign Strategy": "https://www.coursera.org/search?query=Campaign%20Strategy",
        "Canva": "https://www.coursera.org/search?query=Canva",
        "Circuit Design": "https://www.coursera.org/search?query=Circuit%20Design",
        "Cisco": "https://www.coursera.org/search?query=Cisco",
        "Classroom Management": "https://www.coursera.org/search?query=Classroom%20Management",
        "Client Relationship": "https://www.coursera.org/search?query=Client%20Relationship",
        "Cloud Architecture": "https://www.coursera.org/search?query=Cloud%20Architecture",
        "Computer Vision": "https://www.coursera.org/search?query=Computer%20Vision",
        "Content Marketing": "https://www.coursera.org/search?query=Content%20Marketing",
        "Content Strategy": "https://www.coursera.org/search?query=Content%20Strategy",
        "Control Systems": "https://www.coursera.org/search?query=Control%20Systems",
        "Customer Support": "https://www.coursera.org/search?query=Customer%20Support",
        "Cypress": "https://www.coursera.org/search?query=Cypress",
        "Data Analysis": "https://www.coursera.org/search?query=Data%20Analysis",
        "Data Modeling": "https://www.coursera.org/search?query=Data%20Modeling",
        "Data Visualization": "https://www.coursera.org/search?query=Data%20Visualization",
        "Deep Learning": "https://www.youtube.com/watch?v=0oyCUWLL_fU",
        "DevOps": "https://www.coursera.org/search?query=DevOps",
        "Docker": "https://www.coursera.org/search?query=Docker",
        "ETL": "https://www.coursera.org/search?query=ETL",
        "Excel": "https://www.coursera.org/search?query=Excel",
        "Experimentation": "https://www.coursera.org/search?query=Experimentation",
        "Firebase": "https://www.coursera.org/search?query=Firebase",
        "Figma": "https://www.coursera.org/search?query=Figma",
        "Flutter": "https://www.coursera.org/search?query=Flutter",
        "GANs": "https://www.coursera.org/search?query=GANs",
        "GCP": "https://www.coursera.org/search?query=Google%20Cloud",
        "Git": "https://www.coursera.org/search?query=Git",
        "Google Analytics": "https://www.coursera.org/search?query=Google%20Analytics",
        "Hadoop": "https://www.coursera.org/search?query=Hadoop",
        "HTML": "https://www.coursera.org/search?query=HTML",
        "IAM": "https://www.coursera.org/search?query=IAM",
        "Illustrator": "https://www.coursera.org/search?query=Illustrator",
        "Inventory Management": "https://www.coursera.org/search?query=Inventory%20Management",
        "Java": "https://www.coursera.org/search?query=Java",
        "JavaScript": "https://www.coursera.org/search?query=JavaScript",
        "Jenkins": "https://www.coursera.org/search?query=Jenkins",
        "JIRA": "https://www.coursera.org/search?query=JIRA",
        "Kotlin": "https://www.coursera.org/search?query=Kotlin",
        "Kubernetes": "https://www.coursera.org/search?query=Kubernetes",
        "Linux": "https://www.coursera.org/search?query=Linux",
        "LLMs": "https://www.coursera.org/learn/generative-ai-with-llms",
        "Machine Learning": "https://www.coursera.org/learn/machine-learning",
        "MATLAB": "https://www.coursera.org/search?query=MATLAB",
        "Metasploit": "https://www.coursera.org/search?query=Metasploit",
        "Microcontrollers": "https://www.coursera.org/search?query=Microcontrollers",
        "Microservices": "https://www.coursera.org/search?query=Microservices",
        "MongoDB": "https://www.coursera.org/search?query=MongoDB",
        "MySQL": "https://www.coursera.org/search?query=MySQL",
        "Networking": "https://www.coursera.org/search?query=Networking",
        "Node.js": "https://www.coursera.org/search?query=Node.js",
        "NumPy": "https://www.coursera.org/search?query=NumPy",
        "Objective-C": "https://www.coursera.org/search?query=Objective-C",
        "OpenCV": "https://www.coursera.org/search?query=OpenCV",
        "Oracle": "https://www.coursera.org/search?query=Oracle%20SQL",
        "OWASP": "https://www.coursera.org/search?query=OWASP",
        "Pandas": "https://www.coursera.org/search?query=Pandas",
        "Penetration Testing": "https://www.coursera.org/search?query=Penetration%20Testing",
        "Photoshop": "https://www.coursera.org/search?query=Photoshop",
        "PLC": "https://www.coursera.org/search?query=PLC",
        "PostgreSQL": "https://www.coursera.org/search?query=PostgreSQL",
        "Power BI": "https://www.coursera.org/search?query=Power%20BI",
        "Python": "https://www.coursera.org/search?query=Python",
        "PyTorch": "https://www.coursera.org/search?query=PyTorch",
        "React": "https://www.coursera.org/search?query=React",
        "REST API": "https://www.coursera.org/search?query=REST%20API",
        "Robotics": "https://www.coursera.org/search?query=Robotics",
        "ROS": "https://www.coursera.org/search?query=ROS",
        "Scikit-learn": "https://www.coursera.org/search?query=Scikit-learn",
        "Scrum": "https://www.coursera.org/search?query=Scrum",
        "SEO": "https://www.coursera.org/search?query=SEO",
        "Shell Scripting": "https://www.coursera.org/search?query=Shell%20Scripting",
        "Smart Contracts": "https://www.coursera.org/search?query=Smart%20Contracts",
        "Spark": "https://www.coursera.org/search?query=Apache%20Spark",
        "SQL": "https://www.coursera.org/search?query=SQL",
        "Statistics": "https://www.coursera.org/search?query=Statistics",
        "Swift": "https://www.coursera.org/search?query=Swift",
        "Tableau": "https://www.coursera.org/search?query=Tableau",
        "TensorFlow": "https://www.coursera.org/search?query=TensorFlow",
        "Terraform": "https://www.coursera.org/search?query=Terraform",
        "TestNG": "https://www.coursera.org/search?query=TestNG",
        "Transformers": "https://www.coursera.org/search?query=Transformers",
        "Unity": "https://www.coursera.org/search?query=Unity",
        #"Unreal Engine": "https://www.coursera.org/search?query=Unreal%20Engine",
        "Vue": "https://www.coursera.org/search?query=Vue",
        "Web3": "https://www.coursera.org/search?query=Web3",
        "Wireframing": "https://www.coursera.org/search?query=Wireframing",
        "Xcode": "https://www.coursera.org/search?query=Xcode"
    }

def recommend_courses(missing_skills):

    import urllib.parse

    recommended = []

    # lowercase version of database for safe matching
    course_db_lower = {k.lower(): v for k, v in course_database.items()}

    for skill in missing_skills:

        skill_clean = skill.strip()
        skill_lower = skill_clean.lower()

        # check if skill exists in database
        if skill_lower in course_db_lower:
            link = course_db_lower[skill_lower]

        else:
            # create dynamic Coursera search link
            query = urllib.parse.quote(skill_clean)
            link = f"https://www.coursera.org/search?query={query}"

        recommended.append({
            "skill": skill_clean,
            "title": f"{skill_clean} Course",
            "link": link
        })

    return recommended
