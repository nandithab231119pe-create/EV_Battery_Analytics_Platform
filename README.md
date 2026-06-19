# EV Battery Analytics Platform

## Project Overview

The EV Battery Analytics Platform is an interactive data analytics and visualization project developed using Python, SQL, and Streamlit.

The project combines battery degradation analysis using the NASA Battery Dataset and EV market analysis using a global Electric Vehicle Specifications dataset. The platform provides insights into battery health, state-of-health (SOH), degradation trends, temperature effects, vehicle efficiency, battery capacity, and drivetrain distributions.

---

## Objectives

* Analyze battery degradation trends using NASA battery data.
* Calculate and visualize State of Health (SOH).
* Identify healthy and degraded batteries.
* Study the effect of temperature on battery performance.
* Perform EV market analysis using vehicle specifications.
* Develop an interactive Streamlit dashboard for decision support.

---

## Technologies Used

### Programming & Analytics

* Python
* SQL
* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib
* Streamlit

### Development Tools

* Visual Studio Code
* Jupyter Notebook
* Git & GitHub

---

## Datasets Used

### NASA Battery Dataset

Used for:

* Capacity degradation analysis
* SOH estimation
* Battery lifecycle monitoring

### Electric Vehicle Specifications Dataset

Used for:

* Range analysis
* Battery capacity comparison
* Efficiency benchmarking
* Market segmentation
* Drivetrain analysis

---

## Dashboard Features

### Battery Analytics

* Battery Health Overview
* Capacity Degradation Analysis
* State of Health (SOH) Tracking
* Battery Status Indicator
* Temperature Analysis
* Top Healthy Batteries
* Most Degraded Batteries

### EV Market Analytics

* Market KPIs
* Top Brands by Average Range
* Battery Capacity Analysis
* Efficiency Analysis
* Segment Distribution
* Drivetrain Distribution

---

## Key Insights

### Battery Dataset

* Average Battery SOH: 72.17%
* Best Battery: B0026 (97.37% SOH)
* Most Degraded Battery: B0050 (10.53% SOH)

### EV Dataset

* Lucid achieved the highest average driving range.
* Lotus showed the highest average battery capacity.
* AWD was the most common drivetrain configuration.
* Medium-sized vehicles dominated the dataset.

---

## Project Structure

```text
EV_BATTERY_ANALYTICS
│
├── dashboard/
├── data/
├── docs/
├── images/
├── notebooks/
├── sql/
├── README.md
└── requirements.txt
```

---

## Run Locally

```bash
pip install -r requirements.txt

streamlit run dashboard/app.py
```

---

## Author

Nanditha S Nambiar

B.Tech Production Engineering

National Institute of Technology Calicut
