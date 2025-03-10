"""
main_scraper.py

This script fetches job listings from Xing, saves the extracted job data into a CSV file, 
and then cleans the data by correcting city names and adding geographical information.
"""

import csv
from Helper_files.xing_scraping_helper import fetch_jobs, extract_job_data
from Helper_files.xing_cleaning_helper import clean_job_data

def get_xing_data(data_size=100, out_file="xing_output_file.csv", limit=20):
    """
    Fetches job listings from Xing, saves the data to a CSV file, and then cleans the data.

    Args:
        data_size (int, optional): The total number of job listings to fetch. Defaults to 100.
        out_file (str, optional): The output CSV file name. Defaults to "xing_output_file.csv".
        limit (int, optional): Number of jobs to fetch per request. Defaults to 20.

    Returns:
        None
    """
    with open(out_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Updated Date", "Location", "Company", "Min Salary", "Max Salary"])

        for offset in range(0, data_size, limit):
            print(f"Fetching jobs {offset + 1} to {min(offset + limit, data_size)}...")
            jobs = fetch_jobs(limit, offset)

            if not jobs:
                print("No data received or API request failed. Skipping batch.")
                continue

            for job in jobs:
                writer.writerow(extract_job_data(job).values())

    print(f"Job data successfully saved to {out_file}")

    # Clean the data after scraping
    clean_job_data(input_file=out_file, output_file="xing_cleaned_jobs.csv")

if __name__ == "__main__":
    get_xing_data(1000, "xing_output_file.csv")
