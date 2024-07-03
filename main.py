from database.mongo_connection import get_database
from scraper.job_scraper import scrape_jobs
import os 

JOBS_URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=#"
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "jobs_python"

def main():
    db = get_database(uri=MONGO_URI, db_name=DB_NAME)
    job_data = scrape_jobs(JOBS_URL)

    if job_data:
        db.jobs.insert_many(job_data)
        print(f"Inseridos {len(job_data)} anúncios de empregos no banco de dados!")


if __name__ == "__main__":
    main()

