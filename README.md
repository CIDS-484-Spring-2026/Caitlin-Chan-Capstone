# Retail Data Analysis & Recommendation System
**Student:** Caitlin Chan  
**Course:** CIDS-484 Senior Capstone (Spring 2026)

---

## Technical Goals
This project focuses on the end-to-end pipeline of retail data, from raw cloud logs to user-facing recommendations.

* **Data Engineering:** Flattening and unnesting complex JSON web-logs from **BigQuery** using SQL.
* **Processing:** Utilizing **Python (Pandas)** for data cleaning, feature engineering (**RFM Analysis**), and outlier detection.
* **Machine Learning:** Implementing a **Collaborative Filtering** model to predict top-5 product recommendations per user.
* **Full-Stack Deployment:** Building an interactive dashboard to showcase real-time recommendations.

---

## 🚩 Milestone 1: Environment Setup & Data Pipeline
*Completed: February 2026*

### What I Accomplished:
- [x] **Moved to a professional workspace:** Migrated from browser-based tools (Google Colab) to a local development environment using **IntelliJ** and **Jupyter**.
- [x] **Cloud Connectivity:** Configured authentication for **Google BigQuery** to enable remote data fetching.
- [x] **Environment Configuration:** Installed essential libraries (`db-dtypes`, `Pandas`) to facilitate data transformation between SQL and Python.
- [x] **Optimization:** Enabled the **BigQuery Storage API** for high-speed data retrieval to handle large-scale datasets efficiently.

---

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **IDE:** IntelliJ IDEA
* **Database:** Google BigQuery (SQL)
* **Data Libraries:** Pandas, NumPy

✅  Milestone 2: Data Preparation & ML Model
What I Accomplished

- [x]	Cleaned and validated the data: I removed zero-price records that would corrupt the model, confirmed that products with multiple prices reflect genuine price changes over time (not dirty data), and extracted the most recent price per product for use in recommendations.

- [x] Built a product relationship map: I created a co-occurrence heatmap of the top 10 products to understand which products are genuinely bought together. After comparing two approaches, I chose Pearson correlation over raw co-purchase scores because it captures real buying behaviour rather than just popularity.

- [x] Plan and choose the right machine learning algorithm: I tried to install scikit-surprise (SVD) but it requires a C++ compiler that wasn’t available on my Windows machine. Instead I used the implicit library (ALS — Alternating Least Squares), which is purpose-built for this type of problem and installed without issues.

