# Korfball Events Scraper

This Python script (`korfball_events_scraper.py`) scrapes upcoming korfball events from the website https://korfball.sport/events/list and stores the extracted data in a CSV file. The purpose of this project is to gather data to build a dataset for a data visualization group challenge.

## Project Overview

The script performs the following tasks:

1. **Construct URL**: Constructs the URL for the korfball events page, specifying the base URL and filtering events starting from a specific date (in this case, January 1, 2015).

2. **Scrape Data**: Iterates through each page of the events listing, extracts event details such as title, country, city, address, start date, end date, and link to the event page using BeautifulSoup.

3. **Write to CSV**: Writes the extracted event details to a CSV file (`korfball_events.csv`) with appropriate headers.

## Dependencies

Ensure you have the following dependencies installed:

- `requests`
- `beautifulsoup4`

You can install the dependencies using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. **Run the Script**: Execute the script by running the following command in your terminal:

    ```bash
    python korfball_events_scraper.py
    ```

2. **View Results**: The scraped event details will be stored in the CSV file `korfball_events.csv`.

## Note

- Ensure you have an active internet connection to fetch the korfball events data.
- Adjust the start date in the URL construction according to your requirements.
- This script is provided for educational and data collection purposes. Ensure compliance with website terms of use and data privacy regulations.

---

*Disclaimer: This project is not affiliated with or endorsed by the korfball.sport website. Use at your own risk.*
