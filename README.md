# HR Employee Attrition & Analytics Dashboard

## 📌 Project Overview
This project focuses on analyzing employee data to identify key factors driving workforce attrition. By combining the data manipulation power of Python with the interactive visualization capabilities of Power BI, this dashboard uncovers trends related to departments, income levels, and work-life balance to help HR teams improve employee retention.

## 🛠️ Tech Stack & Tools
- **Data Processing:** Python (Pandas)
- **Data Visualization:** Seaborn, Matplotlib, Power BI Desktop
- **Dataset:** HR-Employee-Attrition (1,470 employee records)

## 🔍 Key Insights Discovered
- **Department Trends:** The Research & Development department shows the highest stable workforce volume, while specific roles within Sales experience higher relative attrition rates.
- **Income Impact:** Employees with lower monthly income brackets show a higher propensity to leave the organization, indicating salary benchmarking needs.
- **Work-Life Balance:** A strong correlation exists between high overtime hours and employee turnover metrics.
- **Model Performance:**

**Dataset:** 1,470 employee records, 35 features
**Models compared:** Logistic Regression vs Random Forest
**Evaluation metrics:** F1-score, Precision, Recall, AUC-ROC
**Final model accuracy:** 87%
**Output:** 5 costed HR retention recommendations targeting highest-risk segments

## 📥 How to Run the Project
1. Clone this repository.
2. Run the `Employee.ipynb` notebook in VS Code to see the data processing pipeline.
3. Open the `HR_Analytics.pbix` file in Power BI Desktop to interact with the dashboard live.
