"""
xing_cleaning_helper.py

This script cleans the scraped job data by correcting city names and adding geographical information.
"""

import pandas as pd
from thefuzz import process

def clean_job_data(input_file="xing_job_data.csv", cities_file="Helper_files\Deutschland_Cities.csv", output_file="xing_cleaned_jobs.csv"):
    """
    Cleans the scraped job data by correcting city names and adding geographical information (latitude, longitude, and state).

    Args:
        input_file (str, optional): The input CSV file with job data. Defaults to "Job_data.csv".
        cities_file (str, optional): The CSV file containing city names and geographical data. Defaults to "Deutschland_Cities.csv".
        output_file (str, optional): The output CSV file for cleaned job data. Defaults to "cleaned_jobs.csv".

    Returns:
        None
    """
    try:
        cities_df = pd.read_csv(cities_file, sep=";", encoding="latin1")
        jobs_df = pd.read_csv(input_file, sep=";", encoding="latin1")
    except FileNotFoundError as e:
        print(f"Error: Could not find file {e.filename}")
        return

    # Ensure consistent column names in cities dataset
    cities_df.rename(columns={"city": "Cleaned_City", "lat": "Latitude", "lng": "Longitude", "State/admin": "State"}, inplace=True)

    # Convert city names to lowercase for easier matching
    cities_df["Cleaned_City"] = cities_df["Cleaned_City"].str.lower()
    jobs_df["Location"] = jobs_df["Location"].str.lower()

    # Function to clean and correct city names
    def correct_city_name(city):
        city = city.strip().replace(".", "")  # Remove spaces and dots
        result = process.extractOne(city, cities_df["Cleaned_City"])  # Find closest match
        if result:  # Ensure that there's a result
            closest_match, score = result[:2]  # Unpack only the first two values (match, score)
            return closest_match if score > 70 else None  # Only return match if confidence is high
        return None

    # Expand city names if they have multiple locations separated by "/" or ","
    jobs_df["Location"] = jobs_df["Location"].str.replace("/", ",").str.split(",")  # Normalize separators
    jobs_df = jobs_df.explode("Location")  # Expand into multiple rows

    # Clean city names
    jobs_df["Location"] = jobs_df["Location"].str.strip()  # Remove leading/trailing spaces
    jobs_df["Cleaned_City"] = jobs_df["Location"].apply(correct_city_name)  # Apply fuzzy matching

    # Remove rows where city couldn't be matched
    jobs_df = jobs_df.dropna(subset=["Cleaned_City"])

    # Merge with cities dataset to get lat, lng, and state
    jobs_df = jobs_df.merge(cities_df, left_on="Cleaned_City", right_on="Cleaned_City", how="left")

    # Drop old location column
    jobs_df.drop(columns=["Location"], inplace=True)

    # Save the cleaned data
    jobs_df.to_csv(output_file, index=False, sep=";", encoding="latin1")

    print("Cleaning complete! Saved as cleaned_jobs.csv")
