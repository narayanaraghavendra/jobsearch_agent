import json
import random

# Define job components
job_titles = [
    "DevOps Engineer", "Data Scientist", "AI Researcher", "Backend Developer", "Full Stack Developer",
    "Mobile App Developer", "Cybersecurity Analyst", "Cloud Architect", "Frontend Engineer", "ML Engineer",
    "Site Reliability Engineer", "Database Administrator", "Software Engineer", "Network Engineer", "QA Engineer",
    "Business Intelligence Analyst", "Big Data Engineer", "Computer Vision Engineer", "NLP Engineer", "Product Manager"
]

companies = ["TechNova", "DataWhiz", "GenAI Labs", "CodeCrush", "StackBuilders", "AppMob", "SecureSphere", "SkyInfra", "PixelFlow", "AutoMLWorks"]
locations = ["Remote", "Bangalore", "Hyderabad", "Pune", "Chennai", "Delhi", "Mumbai", "Kolkata", "Ahmedabad", "Noida"]
skills_pool = [
    "Python", "Java", "JavaScript", "React", "Node.js", "Docker", "Kubernetes", "AWS", "GCP", "Azure",
    "TensorFlow", "PyTorch", "SQL", "NoSQL", "CI/CD", "Jenkins", "Linux", "REST APIs", "GraphQL", "LangChain"
]
descriptions = [
    "Design, develop, and maintain scalable systems.",
    "Analyze data and build predictive models.",
    "Create and optimize deep learning pipelines.",
    "Implement and monitor security protocols.",
    "Develop mobile applications for Android and iOS.",
    "Architect and deploy cloud infrastructure.",
    "Collaborate with cross-functional teams for product delivery.",
    "Ensure high availability and system reliability.",
    "Build APIs and integrate third-party services.",
    "Develop user-facing web applications."
]

# Generate 300 job entries
job_list = []
for _ in range(300):
    title = random.choice(job_titles)
    company = random.choice(companies)
    location = random.choice(locations)
    skills = ", ".join(random.sample(skills_pool, 4))
    desc = random.choice(descriptions)
    job_text = f"{title} at {company} in {location}. Skills: {skills}. Description: {desc}"
    job_list.append(job_text)

# Save to jobs_db.json
with open("jobs_db.json", "w") as f:
    json.dump(job_list, f, indent=2)

print("✅ jobs_db.json created with 300 IT jobs.")
