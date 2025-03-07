"""
main_scraper.py

This script fetches job listings saves the extracted job data into a CSV file.
"""

import csv
from Helper_files.xing_helper import fetch_jobs, extract_job_data

def get_xing_data(data_size=100, out_file="xing_output_file.csv", limit=20):
    """
    Fetches job listings from Xing using the API and saves the extracted job data into a CSV file.

    Args:
        data_size (int, optional): The total number of job listings to fetch. Defaults to 100.
        out_file (str, optional): The output CSV file name. Defaults to "xing_output_file.csv".
        limit (int, optional): Number of jobs to fetch per request. Defaults to 20.

    Returns:
        None
    """
    # Open the file once for better performance
    with open(out_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Write CSV header
        writer.writerow(["Job Title", "Updated Date", "Location", "Company", "Min Salary", "Max Salary"])

        # Fetch and write job data in batches
        for offset in range(0, data_size, limit):
            print(f"Fetching jobs {offset + 1} to {min(offset + limit, data_size)}...")  # Progress tracking
            
            jobs = fetch_jobs(limit, offset)

            if not jobs:
                print("No data received or API request failed. Skipping batch.")
                continue  # Skip this batch if the API call failed

            # Write job data to CSV
            for job in jobs:
                writer.writerow(extract_job_data(job).values())

    print(f"Job data successfully saved to {out_file}")

# Run the scraper with default values
if __name__ == "__main__":
    get_xing_data(1000, "Xing_output_file.csv")
