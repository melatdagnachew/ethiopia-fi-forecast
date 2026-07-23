Forecasting Financial Inclusion in Ethiopia
Overview

This project was completed as part of the Selam Analytics Financial Inclusion Forecasting Challenge.

The objective is to develop a forecasting system that predicts Ethiopia's financial inclusion progress by modeling historical financial inclusion indicators, infrastructure development, mobile money operator statistics, policy interventions, and major market events.

The project follows the World Bank Global Findex Framework and focuses on forecasting two key indicators:

Access – Account Ownership Rate
Usage – Digital Payment Adoption Rate

Forecasts are generated for the 2025–2027 period to support decision-making by development finance institutions, mobile money operators, and the National Bank of Ethiopia.

Business Problem

Ethiopia has experienced rapid digital financial transformation through initiatives such as:

Telebirr launch (2021)
Safaricom Ethiopia market entry (2022)
M-Pesa Ethiopia launch (2023)
Fayda Digital ID rollout
Expansion of 4G infrastructure
EthioPay Instant Payment System
National Financial Inclusion Strategy II (NFIS-II)

Despite these developments, the Global Findex 2024 reports that only 49% of Ethiopian adults own a financial account, representing only a 3 percentage point increase since 2021.

This project investigates the drivers of financial inclusion, models the effects of major policy and market events, and forecasts future Access and Usage indicators.

Project Structure
ethiopia-fi-forecast/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── task1_data_enrichment.ipynb
│   ├── task2_eda.ipynb
│   ├── task3_impact_modeling.ipynb
│   └── task4_forecasting.ipynb
│
├── dashboard/
│   └── app.py
│
├── outputs/
│   ├── account_ownership_forecast.csv
│   └── mobile_money_usage_forecast.csv
│
├── reports/
│   ├── data_enrichment_log.md
│   ├── Task1_Task2_Report.pdf
│   └── figures/
│
├── models/
├── src/
│
├── README.md
├── requirements.txt
└── .gitignore
Dataset

The project uses the unified financial inclusion dataset provided by Selam Analytics.

Main files include:

ethiopia_fi_unified_data.csv
reference_codes.csv

The dataset integrates observations, policy events, infrastructure indicators, impact relationships, and strategic targets into a single unified schema.

Understanding the Unified Schema

The dataset uses a unified schema in which each row represents a different record type.

Record Type	Description
Observation	Financial inclusion indicators and infrastructure statistics
Event	Product launches, policies, infrastructure investments, milestones
Impact Link	Relationships connecting events to financial indicators
Target	National financial inclusion targets

This design enables historical observations, qualitative events, and strategic targets to be modeled together within the forecasting pipeline.

Data Sources

The dataset was enriched using publicly available information from:

World Bank Global Findex
National Bank of Ethiopia
Ethio Telecom
Safaricom Ethiopia
GSMA
Fayda Digital ID Program

Each added record includes:

Source information
Collection date
Confidence level
Documentation notes
Original supporting text
Completed Tasks
Task 1 — Data Exploration and Enrichment

Completed activities:

Dataset exploration
Unified schema analysis
Data quality assessment
Indicator coverage analysis
Data enrichment
Metadata documentation
Creation of data_enrichment_log.md

The dataset was expanded with additional observations covering:

Mobile money
Digital infrastructure
Digital ID
Payment statistics
Operator metrics
Task 2 — Exploratory Data Analysis

Completed analyses:

Dataset overview
Temporal coverage
Confidence assessment
Indicator coverage
Account ownership trends
Mobile money adoption
Infrastructure analysis
Event timeline
Correlation analysis
Business interpretation

Key insights include:

Account ownership growth slowed between 2021 and 2024.
Mobile money expanded rapidly after Telebirr and M-Pesa.
Infrastructure improvements support financial inclusion.
Digital ID is likely to accelerate onboarding.
Gender disparities remain an important challenge.
Task 3 — Event Impact Modeling

Developed an event-impact framework to quantify how major policy and market events influence financial inclusion indicators.

Completed activities:

Analysis of impact links
Event-indicator association matrix
Historical validation
Comparable-country evidence review
Impact estimation refinement
Documentation of assumptions and uncertainties

Major events modeled include:

Telebirr Launch
Safaricom Entry
M-Pesa Launch
Fayda Digital ID
NFIS-II Strategy
Foreign Exchange Liberalization
P2P surpassing ATM transactions
Task 4 — Forecasting Access and Usage

Forecasts were produced for 2025–2027 using trend-based forecasting combined with scenario analysis.

Outputs include:

Baseline forecast
Optimistic scenario
Pessimistic scenario
Confidence intervals
Forecast visualizations
Forecast tables

Forecasts indicate continued improvement in financial inclusion, although growth is expected to remain slower than during the 2014–2021 period.

Task 5 — Dashboard Development

A Streamlit dashboard was developed to enable interactive exploration of the project results.

Dashboard features include:

Dashboard Overview
Interactive Trends
Forecast Visualization
Inclusion Projections
Scenario Selection
Progress toward the 60% target
Forecast download functionality
Technologies Used
Python
Pandas
NumPy
Matplotlib
Plotly
Streamlit
Scikit-learn
Jupyter Notebook
Installation

Clone the repository

git clone https://github.com/<your-username>/ethiopia-fi-forecast.git

Navigate into the project

cd ethiopia-fi-forecast

Create a virtual environment

python -m venv .venv

Activate the environment

macOS / Linux
source .venv/bin/activate
Windows
.venv\Scripts\activate

Install dependencies

pip install -r requirements.txt
Running the Dashboard

Launch the Streamlit dashboard

streamlit run dashboard/app.py

The dashboard provides:

Financial inclusion overview
Interactive trend exploration
Forecast comparison
Inclusion projections
Scenario analysis
Downloadable forecast tables
Results

Major findings include:

Account ownership increased from 22% (2014) to 49% (2024).
Mobile money expanded rapidly following Telebirr and M-Pesa launches.
Digital infrastructure improvements appear strongly associated with financial inclusion.
Fayda Digital ID is expected to improve customer onboarding and KYC processes.
Event impact modeling suggests Telebirr, NFIS-II, and Fayda are among the strongest drivers of future financial inclusion.
Forecasts suggest Ethiopia could approach or slightly exceed 60% account ownership by 2027 under favorable conditions.
Future Improvements

Potential extensions include:

Machine learning forecasting models (XGBoost, Prophet, LSTM)
Additional socioeconomic indicators
Regional financial inclusion forecasts
Real-time dashboard updates
Automated data ingestion pipelines
Enhanced uncertainty modeling