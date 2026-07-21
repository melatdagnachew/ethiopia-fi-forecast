# Forecasting Financial Inclusion in Ethiopia

## Overview

This project was completed as part of the Selam Analytics Financial Inclusion Forecasting Challenge.

The objective is to develop a forecasting system that predicts Ethiopia's financial inclusion progress by modeling historical financial inclusion indicators, infrastructure development, operator statistics, policy interventions, and major market events.

The project follows the World Bank Global Findex Framework and focuses on forecasting two key indicators:

- **Access** – Account Ownership Rate
- **Usage** – Digital Payment Adoption Rate

Forecasts will be generated for **2025–2027**.

---

# Business Problem

Ethiopia has experienced rapid digital financial transformation through initiatives such as:

- Telebirr launch (2021)
- Safaricom Ethiopia market entry (2022)
- M-Pesa Ethiopia launch (2023)
- Fayda Digital ID rollout
- Expansion of 4G infrastructure
- EthioPay Instant Payment System

Despite these developments, the Global Findex 2024 reports that only **49%** of Ethiopian adults own a financial account, only three percentage points higher than in 2021.

This project investigates the drivers of financial inclusion and develops forecasting models to estimate future Access and Usage indicators.

---

# Project Structure

```text
ethiopia-fi-forecast/

├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── task1_data_enrichment.ipynb
│   ├── task2_eda.ipynb
│
├── reports/
│   ├── data_enrichment_log.md
│   ├── Task1_Task2_Report.pdf
│   └── figures/
│
├── dashboard/
│
├── models/
│
├── src/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Dataset

The project uses the starter dataset provided by Selam Analytics.

Files include:

- **ethiopia_fi_unified_data.csv**
- **reference_codes.csv**

The dataset combines financial inclusion observations, policy events, infrastructure indicators, and strategic targets into a single unified schema.

---

# Understanding the Unified Schema

Unlike traditional datasets that separate observations and events into different tables, this project uses a **unified schema**.

Each row represents one record, identified by the **record_type** field.

The four primary record types are:

| Record Type | Description |
|--------------|------------|
| Observation | Measured financial inclusion indicators and infrastructure statistics |
| Event | Product launches, policy changes, infrastructure projects, milestones |
| Impact Link | Relationships connecting events to financial indicators |
| Target | Government strategic targets |

This unified structure makes it easier to integrate heterogeneous information into forecasting models while maintaining consistent metadata across all records.

---

# Data Sources

The dataset was enriched using publicly available information from trusted organizations including:

- World Bank Global Findex
- National Bank of Ethiopia
- Ethio Telecom
- Safaricom Ethiopia
- GSMA
- Fayda Digital ID Program

Each newly added record includes:

- Source URL
- Original quotation
- Confidence level
- Collection date
- Documentation notes

---

# Completed Tasks

## Task 1 — Data Exploration and Enrichment

Completed activities include:

- Dataset exploration
- Unified schema understanding
- Data quality assessment
- Indicator coverage analysis
- Data enrichment
- Metadata documentation
- Creation of data_enrichment_log.md

The dataset was expanded from **43** to **63** records through additional infrastructure, operator, and digital finance observations.

---

## Task 2 — Exploratory Data Analysis

EDA included:

- Dataset overview
- Temporal coverage analysis
- Confidence assessment
- Indicator coverage
- Account ownership trend analysis
- Mobile money usage analysis
- Infrastructure analysis
- Event timeline visualization
- Correlation analysis
- Business interpretation

Several visualizations were produced to identify relationships between infrastructure, policy interventions, and financial inclusion outcomes.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

# Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/ethiopia-fi-forecast.git
```

Navigate into the project:

```bash
cd ethiopia-fi-forecast
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

---

# Results

Key findings include:

- Financial account ownership increased steadily between 2011 and 2021 but slowed considerably between 2021 and 2024.
- Telebirr and M-Pesa significantly expanded digital financial services.
- Infrastructure improvements such as 4G coverage and digital ID enrollment appear to support financial inclusion.
- Registered mobile money users substantially exceed survey-reported account ownership, suggesting many users already possess traditional bank accounts.
- Gender disparities remain an important challenge.

---

# Future Work

The remaining project phases include:

- Event impact modeling
- Forecasting Access and Usage (2025–2027)
- Dashboard development
- Scenario analysis and uncertainty quantification

---

# Author

**Melat Dagnachew**

MSc Software Engineering
