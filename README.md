# 📊 BSG Customer Journey Dashboard

The **BSG Customer Journey Dashboard** is a dynamic, interactive web application built using **Streamlit** that provides real-time insights into customer behavior and satisfaction across key stages of their journey. The goal is to empower data-driven decision-making by visualizing how different customer segments experience the journey, identify areas of concern (e.g., low satisfaction), and explore individual user paths in a clean, easy-to-navigate interface.

## 🚀 Live Application

▶️ [Launch the Live Demo](https://customer-journey-dashboard-2jinuxotxvv5r2bxcy8kas.streamlit.app/)

---

## 🎯 Project Purpose

This dashboard is designed for teams (like marketing, product, or CX) who need to:

- Understand customer experience trends across stages (Awareness → Decision)
- Segment customers by demographic or regional groupings
- Monitor satisfaction levels and respond to low-performing areas
- View individual customer journeys in detail
- Securely restrict access to internal stakeholders

---

## 🔐 Key Features

- ✅ **Login Authentication**  
  Simple login form using a username and password. Only authorized users can access the dashboard (Keanu / Keanumoodley1 by default).

- 🎨 **Custom UI Enhancements**  
  Beautiful, clean interface styled with embedded HTML/CSS and Lottie animations to add personality to the login and dashboard.

- 📁 **CSV-Based Data**  
  The app loads customer journey data from a CSV file and dynamically filters and visualizes this information.

- 🔍 **Advanced Filtering**  
  Use the sidebar to filter by `Segment`, `Region`, or drill down into specific `Customer ID`s.

- 📊 **Key Performance Indicators (KPIs)**  
  - Total unique customers  
  - Average satisfaction score  
  - Number of low satisfaction scores (< 5)

- 📈 **Trend Visualizations**  
  - Line chart showing satisfaction over time  
  - Histogram of customer stage distribution segmented by group

- 🧭 **Customer Drill-Down**  
  Select any customer to view a detailed timeline of their journey, satisfaction scores, and behavior across stages.

- ⚠️ **Satisfaction Alerts**  
  Auto-detects low scores and presents them clearly, with an option to review those customers’ details.

- 🖼️ **Visual Branding**  
  The BSG logo is prominently placed in the sidebar next to filters for consistent branding.


## 🧪 Demo Credentials

- **Username**: `Keanu`  
- **Password**: `Keanumoodley1`

---

## 🧰 Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io/) - UI framework
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [Plotly](https://plotly.com/python/) - Charting and visuals
- [streamlit-lottie](https://github.com/andfanilo/streamlit-lottie) - For animated UI
- HTML / CSS - Embedded for custom styling

---

## 📂 How to Run Locally

1. **Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/customer-journey-dashboard.git
cd customer-journey-dashboard

```
Install Requirements

```bash
pip install -r requirements.txt
Run the App
```

```bash

streamlit run app.py

```

🧱 File Structure
```bash
├── app.py                # Main Streamlit application
├── data.csv              # Customer journey data
├── requirements.txt      # All Python dependencies
├── screenshots/          # Screenshots for documentation
│   ├── login.png
│   └── dashboard.png
└── README.md             # This file

