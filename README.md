# COVID-19 Data Pipeline

An end-to-end ETL data pipeline built in Python that extracts, transforms, analyses, and visualises global COVID-19 time-series data.

## Dataset
- **Source:** [datasets/covid-19](https://github.com/datasets/covid-19)
- **Format:** CSV
- **Content:** Daily global confirmed cases, recoveries, and deaths (2020–2022)

## How to Run

1. Clone the repository and navigate into it
2. Create and activate a virtual environment: `python3 -m venv venv` then `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the pipeline scripts in order:
   - `python -m src.extract`
   - `python -m src.transform`
   - `python -m src.model`
5. Open the notebook: `jupyter notebook`

## Model Performance
| Metric | Value |
|--------|-------|
| R²     | 0.8972 |
| MAE    | 36,106,676 |
| RMSE   | 43,980,401 |

## Key Findings
- Global confirmed cases grew exponentially, peaking sharply in early 2022
- Clear wave patterns visible in daily new cases throughout 2020-2021
- Death rate relative to confirmed cases declined over time
- Linear Regression achieved R²=0.90 but struggles with exponential growth phases