# Job Scraper: Data Engineering Pipeline

## Project Overview

This project is part of a **Data Engineering Pipeline** that involves extracting job postings from Xing using **Request Spoofing**. The extracted data is structured and stored in a CSV file, cleaned to correct city names and add geographical information, and then prepared for further analysis, such as creating a dashboard in Tableau.

## Features

- Extracts job postings from **Xing's hidden API**.
- Implements **Request Spoofing** to mimic a web browser.
- Retrieves job details such as **title, company, location, salary, and updated date**.
- Efficient data extraction with **batched API requests**.
- Saves data in a structured **CSV format**.
- Cleans and corrects city names using **fuzzy matching**.
- Adds **latitude, longitude, and state information** to each job listing.
- Prepares data for **dashboarding in Tableau**.

## Project Structure
```
project_root/
│── Helper_files/
│   ├── xing_scraping_helper.py   # Contains API request and data extraction logic
│   ├── xing_cleaning_helper.py  # Contains data cleaning and geographical data addition logic
│   └── Deutschland_Cities.csv    # Contains city names and geographical data
│── main_scraper.py               # Runs the scraping and cleaning processes
│── requirements.txt              # Required dependencies
│── README.md                     # Project documentation
```

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed and set up in your environment.

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
Run the **main_scraper.py** file to start extracting job data:
```bash
python main_scraper.py
```
### Example Function Call
```python
get_xing_data(data_size=1000, out_file="Xing_output_file.csv")
```
This will extract **1,000 job listings** and save them in `Xing_output_file.csv`.

## How It Works
1. **Request Spoofing:** The scraper mimics a web browser by sending crafted requests to Xing's hidden API.
2. **Data Extraction:** The API response is parsed to extract relevant job details.
3. **Batch Processing:** Jobs are fetched in chunks (default: 20 per request) for efficiency.
4. **CSV Output:** Extracted data is written in a structured CSV format.
5. **Data Cleaning:** The xing_cleaning_helper.py script cleans the data by correcting city names and adding geographical information.
6. **Cleaned CSV Output:** Cleaned data is saved in xing_cleaned_jobs.csv.
7. **Tableau Dashboarding:** The cleaned data is now ready for visualization and analysis in Tableau.

## CSV File Format
**Raw Data (xing_output_file.csv):**
|     Job Title     | Updated Date| Location | Company   | Min Salary | Max Salary |
|-------------------|-------------|----------|-----------|------------|------------|
| Software Engineer | 2025-03-07  | Berlin   | Xing GmbH | 60,000     | 90,000     |

**Raw Data (xing_output_file.csv):**

|    Job Title    | Updated Date|  Company  |Min Salary|Max Salary|Cleaned_City|Latitude|Longitude|State |
|-----------------|-------------|-----------|----------|----------|---------------------|---------|------|
|Software Engineer| 2025-03-07  | Xing GmbH |60,000    |90,000    |Berlin      |525167  |133833   |Berlin|


## Legal & Ethical Considerations
- This project is for **educational and research purposes** only.

## License
This project is open-source under the **MIT License**.