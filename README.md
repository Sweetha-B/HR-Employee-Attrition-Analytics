#  HR Employee Attrition Prediction

ML-based HR analytics system predicting employee attrition
with actionable retention strategy recommendations.

## Tech Stack
Python · Scikit-learn · Pandas · Seaborn · SQL · Logistic Regression · Random Forest

## Features
- Deep EDA across 35 employee features
- Statistical analysis with Seaborn visualisations
- Logistic Regression and Random Forest comparison
- 87% model accuracy achieved
- 5 costed HR retention strategy recommendations

## Project Structure
```text
├── data/
│   └── ibm_hr_analytics.csv     # IBM HR dataset
├── notebooks/
│   └── attrition_analysis.ipynb # Full analysis notebook
├── models/
│   ├── logistic_model.pkl       # Trained LR model
│   └── rf_model.pkl             # Trained RF model
└── reports/
    └── hr_retention_strategy.pdf
```

## Analysis Flow
1. Data Loading: IBM HR Analytics dataset (35 features)
2. EDA: Statistical analysis and Seaborn visualisations
3. Feature Selection: Top 3 attrition predictors identified
4. Model Training: Logistic Regression vs Random Forest
5. Evaluation: F1-score, Precision, Recall comparison
6. Recommendations: 5 costed HR retention strategies

## Key Results
- Top predictors: Salary band, Department, Job satisfaction
- Model accuracy: 87%
- F1-score evaluated on test set
- 5 specific retention strategies with cost estimates

## Contact
Sweetha B | sweethab99@gmail.com 
