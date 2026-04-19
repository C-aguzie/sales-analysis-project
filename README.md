# 📊 Sales Data Analysis Project

## 📌 Project Overview

This project analyzes a retail sales dataset to uncover key business insights related to revenue trends, customer behavior, product performance, and shipping efficiency. The goal is to transform raw data into actionable insights that support better decision-making.

---

## ❓ Problem Statement

Organizations often collect large volumes of sales data but lack clear insights into performance drivers. This project aims to identify patterns in sales across regions, customer segments, and product categories to highlight opportunities for growth and optimization.

---

## 🎯 Objectives

* Clean and prepare raw sales data
* Analyze sales performance across regions and categories
* Identify high-value customers and top-performing products
* Evaluate shipping efficiency
* Build a clear and interactive Excel dashboard

---

## 🛠️ Tools & Technologies

* **Excel** → Data cleaning & dashboard creation
* **Python (Pandas)** → Data transformation and analysis
* **SQL (SQLite)** → Data querying and aggregation
* **Git & GitHub** → Version control and project sharing

---

## 🧹 Data Cleaning & Preparation

* Removed duplicates and handled missing values
* Standardized column names and formats
* Converted date fields to proper datetime format
* Created new features to enhance analysis:

  * `order_year`
  * `order_month`
  * `shipping_days`

---

## 📊 Dashboard Preview

![Sales Dashboard](images/dashboard.png)

---

## 📈 Key Insights

* **Regional Performance:** Certain regions consistently generate higher revenue, indicating stronger market demand.

* **Product Trends:** Technology and Office Supplies contribute significantly to total sales, while some sub-categories underperform.

* **Customer Segmentation:** A small group of customers accounts for a large portion of total sales, highlighting high-value customers.

* **Shipping Efficiency:** Standard shipping methods have longer delivery times compared to faster shipping options.

* **Sales Trends:** Monthly sales patterns suggest potential seasonality in customer purchasing behavior.

---

## 🗂️ Project Structure

```
sales-analysis-project/
│
├── data/
│ ├── raw_sales.xlsx
│ └── cleaned_sales.csv
│
├── sales.db
├── analysis.sql
├── analysis.py
├── excel_dashboard.xlsx
├── images/
│ └── dashboard.png
└── README.md
```

---

## 🚀 How to Use This Project

1. Open the dataset from the `data/` folder
2. Run `analysis.py` for Python-based analysis
3. Execute queries in `analysis.sql` using SQLite
4. Explore the Excel dashboard for visual insights

---

## 📈 Future Improvements

* Build an interactive dashboard using Power BI or Tableau
* Automate the data cleaning process with Python
* Perform deeper customer and product segmentation

---

## 💡 Key Takeaway

This project demonstrates how raw sales data can be cleaned, analyzed, and transformed into meaningful business insights using a combination of Excel, Python, and SQL.
