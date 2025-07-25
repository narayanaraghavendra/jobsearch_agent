import requests
import json
from config import SERPAPI_KEY, DEFAULT_QUERY, DEFAULT_LOCATION

def fetch_jobs(query=DEFAULT_QUERY, location=DEFAULT_LOCATION, api_key=SERPAPI_KEY, num_results=20):
    params = {
        "engine": "google_jobs",
        "q": query,
        "location": location,
        "hl": "en",
        "api_key": api_key
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()
    jobs = []

    for job in data.get("jobs_results", [])[:num_results]:
        title = job.get("title", "")
        company = job.get("company_name", "")
        description = job.get("description", "")
        location = job.get("location", "")
        jobs.append(f"{title} at {company} in {location}. Description: {description}")

    with open("jobs_db.json", "w") as f:
        json.dump(jobs, f, indent=2)

    return jobs