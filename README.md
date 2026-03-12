# Football League Data Scraper (Automated)

This project is a high-scale web scraping tool built with Python to extract team statistics from FBRef for over 250+ leagues worldwide.

## Key Features
- **Anti-Bot Protection:** Uses `undetected-chromedriver` to bypass Cloudflare.
- **Data Structuring:** Automatically cleans MultiIndex headers into analysis-ready CSVs.
- **Mass Processing:** Scrapes and archives datasets for hundreds of leagues in one run.

## Tech Stack
- Python 3.x
- Pandas
- Selenium (Undetected Chromedriver)

## How to Use
1. Install dependencies: `pip install pandas undetected-chromedriver lxml`
2. Run the script: `python main.py`
