# Credit Card Default Prediction: Risk-Based Classification

## 📌 Project Overview
[cite_start]This project presents a binary classification model designed to predict credit card default in the upcoming billing cycle[cite: 5]. [cite_start]Leveraging both behavioral and demographic features, the system is optimized for **recall** and the **$F_2$ score** to align with proactive risk management and early warning activation[cite: 6]. 

[cite_start]By identifying high-risk customers early, financial institutions can minimize credit risk through strategic interventions[cite: 10].

## 📊 Dataset Description
[cite_start]The model was developed using a dataset containing information on 30,000 customers[cite: 13]:
* [cite_start]**Train Set:** 25,000 customers with labeled default outcomes[cite: 13].
* [cite_start]**Validation Set:** 5,000 customers for performance evaluation[cite: 13].
* [cite_start]**Target Variable:** `next_month_default` ($1$ = default, $0$ = no default)[cite: 14].
* [cite_start]**Features:** Demographic details, credit limits, past payment status, bill amounts, and repayment history[cite: 15].

## 🔎 Exploratory Data Analysis (EDA)
Key insights derived from the data include:
* [cite_start]**Demographics:** Customers in younger age groups and those with lower credit limits show a higher tendency to default[cite: 18].
* [cite_start]**Payment Behavior:** Defaulters frequently display multiple late payments (delay level $\ge 1$) across several months, whereas non-defaulters consistently pay on time[cite: 24].




## 🛠️ Feature Engineering
[cite_start]To enhance the model's predictive power and interpretability, the following features were engineered[cite: 42]:
* [cite_start]**`AVG_Pay_amt`**: The mean of repayments over a 6-month period[cite: 43].
* [cite_start]**`Utilization_Ratio`**: The average bill amount divided by the credit limit[cite: 43].
* [cite_start]**`Delinquency_Streak`**: A count of the number of months where the payment status was $\ge 1$[cite: 43].
* [cite_start]**`Repayment_Std`**: The standard deviation of past repayments to capture volatility[cite: 44].

## 🤖 Model Training & Evaluation
[cite_start]Four classifiers were evaluated: Logistic Regression, Random Forest, XGBoost, and **LightGBM** [cite: 46-49]. [cite_start]LightGBM was selected as the best performer as it provided the most effective trade-off between recall and false positives[cite: 49, 50].

### Threshold Optimization
[cite_start]A standard default threshold of 0.5 yielded suboptimal recall[cite: 53]. [cite_start]Through threshold tuning, the optimal classification threshold was found to be **0.36**, which maximized the $F_2$ score[cite: 54].



### Final Performance Metrics
| Metric | Value |
| :--- | :--- |
| **Model** | [cite_start]LightGBM (Class-Weighted) [cite: 78] |
| **Optimal Threshold** | [cite_start]0.36 [cite: 78] |
| **$F_2$ Score** | [cite_start]0.6092 [cite: 74] |
| **Recall** | [cite_start]0.78 [cite: 75] |
| **Precision** | [cite_start]0.32 [cite: 76] |

## 💼 Business Implications
[cite_start]Identifying high-risk customers allows the institution to take defensive actions[cite: 80, 81]:
* [cite_start]**Credit Exposure Reduction:** Lowering credit limits for high-risk profiles[cite: 82].
* [cite_start]**Proactive Monitoring:** Keeping a closer watch on accounts showing delinquency streaks[cite: 83].
* [cite_start]**Early Reminders:** Activating early payment reminders for predicted defaulters[cite: 84].

## 📝 Conclusion
[cite_start]This solution delivers a recall-focused, interpretable credit default predictor that meets financial risk management goals[cite: 88]. [cite_start]It achieves strong performance on the $F_2$ metric while enabling actionable insights through behavioral metrics[cite: 89].

---
[cite_start]**Author:** Aditya Kumar Verma [cite: 2]  
[cite_start]**Institution:** B.Tech (Electronics and Communication), IIT Roorkee [cite: 3, 4]  
[cite_start]**Contact:** aditya_kv@ece.iitr.ac.in [cite: 4]  
[cite_start]**Reference:** UCI Credit Card Default Dataset [cite: 91]
