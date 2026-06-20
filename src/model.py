# src/model.py
# PURPOSE: Train a Linear Regression model to predict confirmed COVID-19 cases
# INPUT:   Cleaned dataset from transform.py
# OUTPUT:  Same dataset with an additional column for predicted values

import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

PROCESSED_PATH = "data/processed/covid19_cleaned.csv"
OUTPUT_PATH = "data/processed/covid19_with_predictions.csv"

def train_model():
    print("Training Linear Regression model...")

    # Load the cleaned data
    df = pd.read_csv(PROCESSED_PATH)

    # --- Step 1: Define features (X) and target (y) ---
    # X = day_number: a simple numeric representation of time
    # y = Confirmed: the total confirmed cases we want to predict
    X = df[['day_number']]
    y = df['Confirmed']

    # --- Step 2: Split data into training and test sets ---
    # 80% of data trains the model, 20% is held back to evaluate it
    # random_state=42 ensures reproducibility (same split every run)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # --- Step 3: Train the model ---
    model = LinearRegression()
    model.fit(X_train, y_train)

    # --- Step 4: Evaluate the model ---
    y_pred_test = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
    r2 = r2_score(y_test, y_pred_test)

    print(f"\nModel Performance on Test Set:")
    print(f"  MAE:  {mae:,.0f}")
    print(f"  RMSE: {rmse:,.0f}")
    print(f"  R²:   {r2:.4f}")

    # --- Step 5: Generate predictions for the entire dataset ---
    # This lets us plot actual vs predicted across all dates
    df['predicted_confirmed'] = model.predict(X).round(0)

    # --- Step 6: Save the output ---
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nPredictions saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    train_model()