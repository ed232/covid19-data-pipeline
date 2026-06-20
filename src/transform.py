# src/transform.py
# PURPOSE: Clean and prepare the raw COVID-19 data for analysis and modelling

import pandas as pd
import os

RAW_PATH = "data/raw/covid19_raw.csv"
PROCESSED_PATH = "data/processed/covid19_cleaned.csv"

def transform():
    print("Transforming data...")

    # Load the raw CSV into a pandas DataFrame
    df = pd.read_csv(RAW_PATH)

    # --- Step 1: Inspect the data ---
    print("Columns:", df.columns.tolist())
    print("Shape:", df.shape)
    print("Missing values:\n", df.isnull().sum())

    # --- Step 2: Parse dates ---
    # Convert the Date column from a string to a proper datetime object
    df['Date'] = pd.to_datetime(df['Date'])

    # --- Step 3: Sort by date (earliest first) ---
    df = df.sort_values('Date').reset_index(drop=True)

    # --- Step 4: Handle missing values ---
    # Forward fill: if a value is missing, use the previous day's value
    df = df.ffill()

    # --- Step 5: Feature engineering ---
    # Create a numeric column representing days since the pandemic started
    # This is what the model will use as its input (X)
    df['day_number'] = (df['Date'] - df['Date'].min()).dt.days

    # Calculate daily new cases (difference between consecutive days)
    df['new_cases'] = df['Confirmed'].diff().fillna(0).clip(lower=0)

    # --- Step 6: Remove any duplicate rows ---
    df = df.drop_duplicates()

    # --- Step 7: Save cleaned data ---
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    print(f"Cleaned data saved to {PROCESSED_PATH}")
    print(f"Final shape: {df.shape}")

if __name__ == "__main__":
    transform()