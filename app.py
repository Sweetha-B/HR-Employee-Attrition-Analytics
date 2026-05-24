import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Pulls your data completely automatically 
csv_path = r"C:\Users\sweet\WA_Fn-UseC_-HR-Employee-Attrition.csv"
df = pd.read_csv(csv_path)

st.title("Live VS Code Graph Stream")

# 2. Side-by-side Department Chart (Matches your notebook perfectly)
st.subheader("Attrition Breakdown by Department")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.countplot(x='Department', hue='Attrition', data=df, palette='Set2', ax=ax1)
st.pyplot(fig1)

# 3. Income Boxplot (Matches your notebook perfectly)
st.subheader("Monthly Income vs Employee Attrition")
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df, palette='Set1', ax=ax2)
st.pyplot(fig2)