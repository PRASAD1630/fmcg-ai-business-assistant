# 🥤 FMCG AI Business Assistant

## Overview

The FMCG AI Business Assistant is an interactive business intelligence dashboard designed for FMCG (Fast-Moving Consumer Goods) organizations. The system enables users to analyze sales, inventory, promotions, and product performance through visual analytics and business insights.

This project was developed as part of an AI Engineering Assessment focused on data modeling, business analytics, and dashboard development.

---

## Features

### 📊 Executive Dashboard
- Total Revenue KPI
- Total Units Sold KPI
- Total Products KPI
- Total Stores KPI
- Revenue Trend Analysis
- Revenue by Region

### 🛒 Sales Analytics
- Top Revenue Generating Products
- Product Performance Analysis
- Category-wise Revenue Distribution

### 🎯 Promotion Analytics
- Promotion Revenue Contribution
- Promotion Effectiveness Analysis
- Discount vs Revenue Correlation

### 📦 Inventory Analytics
- Stockout Monitoring
- Closing Stock Analysis
- Inventory Insights

### 🚀 Advanced Analytics
- Treemap Visualization
- Sunburst Charts
- Region vs Category Heatmap
- Interactive Business Intelligence Dashboards

---

## Dataset Structure

The project uses four datasets:

### Sales & Promotions
- week_start_date
- product_id
- store_id
- region
- units_sold
- revenue
- promotion_flag
- promotion_type
- discount_pct

### Inventory
- opening_stock
- units_received
- units_sold
- closing_stock
- stockout_flag

### Product Master
- product_name
- brand
- category
- sub_category
- pack_size_ml
- unit_price

### Store Master
- store_name
- region
- city
- store_format

---

## Technology Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/PRASAD1630/fmcg-ai-business-assistant.git
cd fmcg-ai-business-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Project Structure

```text
fmcg-ai-business-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── sales_promotions.csv
├── inventory.csv
├── product_master.csv
├── store_master.csv
```

---

## Business Value

- Reduces manual reporting effort.
- Provides quick business insights.
- Supports data-driven decision making.
- Enables sales and inventory monitoring.
- Improves visibility into promotional effectiveness.

---

## Future Improvements

- AI-powered chatbot using Gemini/OpenAI.
- Sales forecasting models.
- Inventory demand prediction.
- Real-time database integration.
- Cloud deployment and authentication.

---

## Author

**Bhukya Prasad**

B.E. Artificial Intelligence & Machine Learning (AIML)

Chaitanya Bharathi Institute of Technology (CBIT)

GitHub: https://github.com/PRASAD1630
