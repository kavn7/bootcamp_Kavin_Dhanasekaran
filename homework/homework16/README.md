# Carvana Stock and Social Media Analysis Project

## Project Overview
This project investigates the relationship between social media activity related to Carvana, Inc. (ticker: CVNA) and its stock price behavior. We collect, process, and analyze both financial and simulated social media data over the 2023-2025 period to identify predictive signals.

## Lifecycle Mapping Summary
- Problem Framing: Defined a clear goal to link social signals to stock returns.
- Data Acquisition: Used Finnhub API (with yfinance fallback) for stock data and web scraping from Finviz plus synthetic social media data generation.
- Data Storage & Processing: Organized datasets in `/data/raw` and `/data/processed` with thoughtful cleaning and validation.
- Modeling: Experimented with regression and classification models to predict price changes.
- Reporting: Delivered results with visualizations and reports designed for both technical and non-technical audiences.
- Reflection: Documented lessons learned and future improvement opportunities in the lifecycle guide.

## Setup Instructions
- Requires Python 3.10+, Anaconda environment recommended.
- Install dependencies: `pip install -r requirements.txt` (including yfinance, pandas, requests, BeautifulSoup, scikit-learn)
- Obtain a Finnhub API key (optional, fallback to yfinance used if not valid).
- Run `src/ingest_data.py` to fetch and process data.
- Open notebooks in `/notebooks` for analysis and modeling steps.

## Contact
For questions, reach out to the project maintainer.
