# Credit Card Fraud Detection using Machine Learning

## 📌 Project Overview

This project focuses on detecting fraudulent credit card transactions using supervised machine learning techniques.  
The primary challenge addressed is **extreme class imbalance**, which is common in real-world fraud detection systems.

The project follows a **modular, production-oriented workflow**, separating data exploration, preprocessing, modeling, evaluation, and explainability into independent components.

---

## 🎯 Objectives

- Analyze and understand highly imbalanced transaction data
- Apply appropriate preprocessing and resampling techniques
- Train and compare multiple classification models
- Evaluate models using fraud-relevant metrics
- Interpret model predictions using explainability techniques

---

## 🗂️ Project Structure

```text
credit-card-fraud-detection/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   └── creditcard.csv
│   └── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modeling.ipynb
│   ├── 04_evaluation.ipynb
│   └── 05_explainability.ipynb
│
├── reports/
│   └── credit_card_fraud_detection_report.pdf
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── models.py
│   └── evaluation.py
│
├── requirements.txt
└── .gitignore
```
## 🧪 Methodology

The project follows a structured and modular machine learning workflow designed to handle
highly imbalanced financial transaction data while maintaining reproducibility and clarity.

### 1️⃣ Exploratory Data Analysis (EDA)

- Understanding the overall structure and characteristics of the dataset  
- Visualizing class imbalance to quantify the rarity of fraudulent transactions  
- Analyzing feature distributions and summary statistics  
- Examining correlations to identify redundant or informative features  

EDA provides critical insights that guide preprocessing choices and model selection.

---

### 2️⃣ Data Preprocessing

- Performing a stratified train–test split to preserve class distribution  
- Applying feature scaling using `StandardScaler`  
- Addressing class imbalance using **SMOTE**, applied **only on the training data**  
- Ensuring strict prevention of data leakage across all preprocessing steps  

Proper preprocessing is essential for fair model evaluation in imbalanced classification problems.

---

### 3️⃣ Model Training

- Training multiple supervised learning models suitable for fraud detection  
- Models used include:
  - Logistic Regression  
  - Decision Tree  
  - Random Forest  
- Maintaining consistent preprocessing and training protocols across all models  

This approach enables meaningful comparison of model performance.

---

### 4️⃣ Model Evaluation

- Evaluating models using metrics appropriate for imbalanced data:
  - Precision  
  - Recall  
  - F1-score  
  - ROC–AUC  
- Analyzing confusion matrices to understand false positives and false negatives  
- Emphasizing recall to minimize missed fraudulent transactions  

Evaluation focuses on real-world applicability rather than raw accuracy.

---

### 5️⃣ Model Explainability

- Applying SHAP (SHapley Additive exPlanations) for interpretability  
- Generating global feature importance to understand overall model behavior  
- Analyzing local explanations for individual predictions  
- Supporting transparency and trust in financial machine learning systems  

Explainability is critical for compliance, auditing, and stakeholder confidence.
## 📈 Evaluation Strategy

Due to the highly imbalanced nature of fraud detection datasets, accuracy alone is not a reliable
performance metric. This project prioritizes evaluation measures that better reflect real-world
fraud detection requirements.

- **Recall** to minimize missed fraudulent transactions (false negatives)  
- **Precision** to control false alarms and unnecessary investigations  
- **F1-score** to balance precision and recall  
- **ROC–AUC** for threshold-independent model comparison  

These metrics provide a more meaningful assessment of model effectiveness in imbalanced settings.

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Data Analysis:** pandas, NumPy  
- **Machine Learning:** scikit-learn  
- **Imbalanced Learning:** imbalanced-learn (SMOTE)  
- **Visualization:** matplotlib, seaborn  
- **Model Explainability:** SHAP  

---

## 🚀 Key Learnings

- Handling class imbalance requires careful metric selection and evaluation strategies  
- Resampling techniques must be applied cautiously to avoid data leakage  
- Explainability plays a crucial role in financial and risk-based ML systems  
- Modular project organization improves clarity, scalability, and maintainability  

---

## 📌 Future Improvements

- Hyperparameter tuning using Grid Search or Bayesian optimization  
- Incorporating cost-sensitive learning to reflect real business impact  
- Threshold optimization based on fraud detection trade-offs  
- Building an end-to-end ML pipeline for deployment  
- Integrating cloud-based model training and serving

## 👤 Author

Aditya  
Machine Learning & Data Science Enthusiast  

Interests include applied machine learning, financial modeling, and building
scalable, production-ready ML systems.

---


## 📄 License

MIT License

Copyright (c) 2025 Aditya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

├── requirements.txt
└── .gitignore
