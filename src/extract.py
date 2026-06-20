# src/extract.py
# PURPOSE: Fetch the raw COVID-19 CSV from GitHub and save it locally

import requests
import os

URL = "https://raw.githubusercontent.com/datasets/covid-19/refs/heads/main/data/worldwide-aggregate.csv"

RAW_PATH = "data/raw/covid19_raw.csv"

def extract():
    print("Extracting data from source...")

    os.makedirs("data/raw", exist_ok=True)

    response = requests.get(URL)
    response.raise_for_status()

    with open(RAW_PATH, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"Raw data saved to {RAW_PATH}")

if __name__ == "__main__":
    extract()