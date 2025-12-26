# Credit Card Default Prediction: Risk-Based Classification

## 📌 Project Overview
This project presents a binary classification model designed to predict credit card default in the upcoming billing cycle. Leveraging both behavioral and demographic features, the system is optimized for **Recall** and the **$F_2$ score** to align with proactive risk management and early warning activation. 

By identifying high-risk customers early, financial institutions can minimize credit risk through strategic interventions.

## 📊 Dataset Description
The model was developed using a dataset containing information on 30,000 customers:
* **Train Set:** 25,000 customers with labeled default outcomes.
* **Validation Set:** 5,000 customers for performance evaluation.
* **Target Variable:** `next_month_default` ($1$ = default, $0$ = no default).
* **Features:** Demographic details, credit limits, past payment status, bill amounts, and repayment history.

## 🔎 Exploratory Data Analysis (EDA)
Key insights derived from the data include:
* **Demographics:** Customers in younger age groups and those with lower credit limits show a higher tendency to default.
* **Payment Behavior:** Defaulters frequently display multiple late payments (delay level $\ge 1$) across several months, whereas non-defaulters consistently pay on time.

## 🛠️ Feature Engineering
To enhance the model's predictive power and interpretability, the following features were engineered:
* **`AVG_Pay_amt`**: The mean of repayments over a 6-month period.
* **`Utilization_Ratio`**: The average bill amount divided by the credit limit.
* **`Delinquency_Streak`**: A count of the number of months where the payment status was $\ge 1$.
* **`Repayment_Std`**: The standard deviation of past repayments to capture volatility.

## 🤖 Model Training & Evaluation
Four classifiers were evaluated: Logistic Regression, Random Forest, XGBoost, and **LightGBM**. LightGBM was selected as the best performer as it provided the most effective trade-off between recall and false positives.

### Threshold Optimization
A standard default threshold of 0.5 yielded suboptimal recall. Through threshold tuning, the optimal classification threshold was found to be **0.36**, which maximized the $F_2$ score.

### Final Performance Metrics
| Metric | Value |
| :--- | :--- |
| **Model** | LightGBM (Class-Weighted) |
| **Optimal Threshold** | 0.36 |
| **$F_2$ Score** | 0.6092 |
| **Recall** | 0.78 |
| **Precision** | 0.32 |

## 💼 Business Implications
Identifying high-risk customers allows the institution to take defensive actions:
* **Credit Exposure Reduction:** Lowering credit limits for high-risk profiles.
* **Proactive Monitoring:** Keeping a closer watch on accounts showing delinquency streaks.
* **Early Reminders:** Activating early payment reminders for predicted defaulters.

## 📝 Conclusion
This solution delivers a recall-focused, interpretable credit default predictor that meets financial risk management goals. It achieves strong performance on the $F_2$ metric while enabling actionable insights through behavioral metrics.

---
**Author:** Aditya Kumar Verma  
**Institution:** B.Tech (Electronics and Communication), IIT Roorkee  
**Contact:** aditya_kv@ece.iitr.ac.in  
**Reference:** UCI Credit Card Default Dataset
