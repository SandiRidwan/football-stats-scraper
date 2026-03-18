# ⚽ Global Football League Data Scraper
**High-Scale Automated Statistics Extraction for 250+ Worldwide Leagues**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Automation-Undetected_Chromedriver-red.svg?style=for-the-badge&logo=selenium)
![Data](https://img.shields.io/badge/Source-FBRef-green.svg?style=for-the-badge)
![Analysis](https://img.shields.io/badge/Output-Analysis--Ready_CSV-orange.svg?style=for-the-badge&logo=pandas)

---

## 📌 Project Overview
This is a high-performance **Sports Intelligence Engine** built to bypass complex web protections and extract deep-level football statistics. Whether you are a Data Scientist, Scout, or Betting Analyst, this tool provides a seamless pipeline to harvest data from over **250+ leagues** worldwide (Premier League, La Liga, Serie A, and beyond).

> **The Challenge:** FBRef uses complex MultiIndex headers and Cloudflare protection.  
> **The Solution:** This scraper automates the bypass using `undetected-chromedriver` and flattens the nested data into a clean, single-layer CSV format ready for PowerBI, Tableau, or Machine Learning models.

---

## ⚡ Elite Features

### 🛡️ Stealth & Bypass Logic
Uses `undetected-chromedriver` to mimic human-like browser behavior, successfully navigating through **Cloudflare** and other anti-bot perimeters that block standard scrapers.

### 🧹 Advanced MultiIndex Cleaning
Automatically processes FBRef's nested HTML tables. It flattens "Complex Headers" (e.g., Performance -> Goals, Performance -> Assists) into intuitive, analysis-ready column names like `Performance_Gls` or `Expected_xG`.

### 🌍 Global Mass Processing
Engineered for scale. The bot can iterate through hundreds of league URLs in a single execution, archiving them into a structured directory for historical comparison.

---

## 🛠️ Technical Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core Logic & Control |
| **Stealth Engine** | Undetected Chromedriver | Bypassing Cloudflare/WAF |
| **Data Cleaning** | Pandas | MultiIndex Flattening & CSV Export |
| **HTML Parsing** | LXML / BeautifulSoup4 | High-speed Table Extraction |

---

## 📂 Project Structure

```text
├── src/
│   ├── main_scraper.py      # The Engine: Stealth navigation & extraction
│   └── data_processor.py    # The Polisher: MultiIndex flattening logic
├── data/                    # Auto-archived league datasets (.csv)
├── requirements.txt         # Dependency list
└── README.md
