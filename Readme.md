# IT Job Market Insights ( Germany )

## Overview
This project focuses on extracting, processing, and analyzing job postings from Xing to understand the IT job demand across Germany. The extracted data is cleaned, enriched with geographical details, and visualized using Tableau.

## Technologies Used
- **Python** (for data extraction and cleaning)
- **Requests & BeautifulSoup** (for web scraping and request spoofing)
- **Pandas** (for data processing and cleaning)
- **Fuzzy Matching** (for city name corrections)
- **CSV** (for structured data storage)
- **Tableau** (for data visualization and dashboarding)
- **Git & GitHub** (for version control and collaboration)

## Features
- **Job Postings Extraction:** Scraped job postings from Xing using request spoofing.
- **Data Cleaning:** Used fuzzy matching to correct city names and enriched the dataset with latitude, longitude, and state.
- **CSV Export:** Saved extracted and cleaned job data into structured CSV files.
- **Tableau Dashboard:** Created an interactive visualization of IT job demand in Germany.

## Project Structure
```
project_root/
│── Helper_files/
│   ├── xing_scraping_helper.py   # Contains API request and data extraction logic
│   ├── xing_cleaning_helper.py  # Contains data cleaning and geographical data addition logic
│   └── Deutschland_Cities.csv    # Contains city names and geographical data
|── raw/
|   |__dashboard_preview.png
│── main_scraper.py               # Runs the scraping and cleaning processes
│── requirements.txt              # Required dependencies
│── README.md                     # Project documentation
```

## Tableau Dashboard
To make the data more accessible and insightful, an interactive Tableau dashboard was created. It provides insights into IT job demand trends, regional distribution, and key job roles.

🔗 **[View the Tableau Dashboard](https://public.tableau.com/views/ITJobDemandAcrossGermany/CompleteDashboard)**

![IT Job Market Insights Dashboard for Germany](https://github.com/akhilpsin/Data-engineering-project/raw/dashboard_preview.png)

## How to Use
1. Clone the repository:
   ```sh
   git clone https://github.com/akhilpsin/Data-engineering-project.git
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the scraper to extract job data:
   ```sh
   python main_scraper.py
   ```
4. View the cleaned data (`xing_cleaned_jobs.csv`) and analyze it using Tableau or other visualization tools.

## CSV File Format
**Raw Data (xing_output_file.csv):**
|     Job Title     | Updated Date| Location | Company   | Min Salary | Max Salary |
|-------------------|-------------|----------|-----------|------------|------------|
| Software Engineer | 2025-03-07  | Berlin   | Xing GmbH | 60,000     | 90,000     |

**Raw Data (xing_output_file.csv):**

|    Job Title    | Updated Date|  Company  |Min Salary|Max Salary|Cleaned_City|Latitude|Longitude|State |
|-----------------|-------------|-----------|----------|----------|---------------------|---------|------|
|Software Engineer| 2025-03-07  | Xing GmbH |60,000    |90,000    |Berlin      |525167  |133833   |Berlin|

---
This project provides a foundation for understanding the IT job market in Germany through data engineering and visualization techniques.