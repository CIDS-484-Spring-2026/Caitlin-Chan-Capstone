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

## Milestone 1: Environment Setup & Data Pipeline
*Completed: February 2026*

### What I Accomplished:
- [x] **Moved to a professional workspace:** Migrated from browser-based tools (Google Colab) to a local development environment using **IntelliJ** and **Jupyter**.
- [x] **Cloud Connectivity:** Configured authentication for **Google BigQuery** to enable remote data fetching.
- [x] **Environment Configuration:** Installed essential libraries (`db-dtypes`, `Pandas`) to facilitate data transformation between SQL and Python.
- [x] **Optimization:** Enabled the **BigQuery Storage API** for high-speed data retrieval to handle large-scale datasets efficiently.

---

## M1 Technologies Used
* **Language:** Python 3.x
* **IDE:** IntelliJ IDEA
* **Database:** Google BigQuery (SQL)
* **Data Libraries:** Pandas, NumPy

## Milestone 2: Data Preparation & ML Model
What I Accomplished

- [x]	Cleaned and validated the data: I removed zero-price records that would corrupt the model, confirmed that products with multiple prices reflect genuine price changes over time (not dirty data), and extracted the most recent price per product for use in recommendations.

- [x]	Performed Exploratory Data Analysis (EDA): Investigated the dataset to understand user behaviour before modelling. This included identifying the top users by interaction count, analysing which products had the highest number of interactions, and ranking the top 10 best-selling products by purchase frequency.

- [x] Built a product relationship map: I created a co-occurrence heatmap of the top 10 products to understand which products are genuinely bought together. After comparing two approaches, I chose Pearson correlation over raw co-purchase scores because it captures real buying behaviour rather than just popularity.

- [x] Plan and choose the right machine learning algorithm: I tried to install scikit-surprise (SVD) but it requires a C++ compiler that wasnΓÇÖt available on my Windows machine. Instead I used the implicit library (ALS ΓÇö Alternating Least Squares), which is purpose-built for this type of problem and installed without issues.

## M2 Technologies Used
* **Language**: Python 3.11
* **IDE**: IntelliJ IDEA + Jupyter Notebook
* **Database**: Google BigQuery (SQL)
* **Cloud Auth**: Google Cloud CLI + BigQuery Storage API
* **Data Libraries**: Pandas, NumPy, db-dtypes, PyArrow, SciPy, scikit-learn
* **Visualisation Libraries**: Matplotlib, Seaborn, adjustText

## Milestone 3: Machine Learning Model & Dashboard Deployment
What I Accomplished

 - [x]	Trained and compared two ML models: Built Model A on raw interaction counts and Model B on correlation-weighted interactions, using the heatmap analysis to boost products with strong co-purchase patterns and downweight isolated ones. Model B won with 11.9% Precision@5 versus Model A's 9.2%.
- [x]	Fixed a critical matrix orientation bug: The user-item matrix was accidentally passed in transposed format, causing the model to learn the wrong factors entirely. Fixing this single mistake improved Precision@5 from 0.3% to 9.2% — the biggest single performance jump in the project.
- [x]	Tuned the model across 98 parameter combinations: A wide grid search across 18 combinations followed by a narrow focused search across 80 combinations identified the optimal settings of factors=15, regularization=0.01, and iterations=20, pushing final model performance to 15.2% Precision@5.
- [x]	Saved all model artifacts: The trained ALS model, label encoders, sparse matrix, correlation matrix, label map, and most recent price lookup were saved to a pickle file for use in the dashboard without retraining.
- [x]	Built and deployed an interactive dashboard: Developed a Streamlit web application that loads the trained model and allows any user to select a product from a dropdown and instantly receive five personalised recommendations, each displaying the product name, current price, correlation score, and confidence level.

## M3 Technologies Used

Language: Python 3.11
* IDE: IntelliJ IDEA + Jupyter Notebook
* ML Library: implicit 0.7.2 (Alternating Least Squares)
* Sparse Matrix: SciPy (CSR format)
* Dashboard: Streamlit
* Model Persistence: pickle
* Version Control: Git + GitHub
* Sonnet 4.6

