# Job Scraper

## Project Overview
This project is part of a **Data Engineering Pipeline** that involves extracting job postings from Xing by leveraging **Request Spoofing**. The extracted data is structured and stored in a CSV file for further processing, such as data analysis, transformation, or loading into a database.

## Features
- Extracts job postings from **Xing's hidden API**.
- Implements **Request Spoofing** to manipulate API calls.
- Retrieves job details such as **title, company, location, salary, and updated date**.
- Efficient data extraction with **batched API requests**.
- Saves data in a structured **CSV format**.

## Project Structure
```
project_root/
│── Helper_files/
│   ├── xing_helper.py       # Contains API request and data extraction logic
│── main_scraper.py          # Runs the scraping process and writes data to CSV
│── requirements.txt         # Required dependencies
│── README.md                # Project documentation
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
Get_xingData(data_size=1000, out_file="Xing_output_file.csv")
```
This will extract **1,000 job listings** and save them in `Xing_output_file.csv`.

## How It Works
1. **Request Spoofing:** The scraper mimics a web browser by sending crafted requests to Xing's hidden API.
2. **Data Extraction:** The API response is parsed to extract relevant job details.
3. **Batch Processing:** Jobs are fetched in chunks (default: 20 per request) for efficiency.
4. **CSV Output:** Extracted data is written in a structured CSV format.

## CSV File Format
| Job Title | Updated Date | Location | Company | Min Salary | Max Salary |
|-----------|-------------|----------|---------|------------|------------|
| Software Engineer | 2025-03-07 | Berlin | Xing GmbH | 60,000 | 90,000 |

## Legal & Ethical Considerations
- This project is for **educational and research purposes** only.
- Scraping websites without permission may **violate terms of service**.
- Ensure compliance with **local laws** and avoid excessive requests.

## Future Enhancements
- Store data in a **database** instead of CSV.
- Implement **job deduplication**.
- Automate daily/weekly job fetching.

## License
This project is open-source under the **MIT License**.