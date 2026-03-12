import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="AI Jobs Dashboard", layout="wide")

data = pd.read_csv("ai_jobs_market_2025_2026.csv")


st.title("AI Jobs Market Dashboard (2025–2026)")
st.write("Exploring salary trends, hiring patterns, and skills across the AI job market.")

st.sidebar.header("Filters")

country_choice = st.sidebar.selectbox(
    "Country",
    sorted(data["country"].unique())
)

exp_choice = st.sidebar.selectbox(
    "Experience Level",
    sorted(data["experience_level"].unique())
)

df = data[
    (data["country"] == country_choice) &
    (data["experience_level"] == exp_choice)
]

col1, col2, col3 = st.columns(3)

col1.metric("Jobs Found", len(df))
col2.metric("Average Salary", int(df["annual_salary_usd"].mean()))
col3.metric("Countries Covered", data["country"].nunique())

st.markdown("---")

st.subheader("Top Countries Hiring for AI Roles")

country_counts = data["country"].value_counts().head(10)

fig1, ax1 = plt.subplots()

sns.barplot(
    x=country_counts.values,
    y=country_counts.index,
    ax=ax1
)

ax1.set_xlabel("Number of Jobs")
ax1.set_ylabel("Country")

st.pyplot(fig1)

st.markdown("---")

st.subheader("Salary Distribution")

fig2, ax2 = plt.subplots()

sns.histplot(
    df["annual_salary_usd"],
    bins=30,
    ax=ax2
)

ax2.set_xlabel("Annual Salary (USD)")
ax2.set_ylabel("Count")

st.pyplot(fig2)

st.markdown("---")

st.subheader("Jobs by Experience Level")

fig3, ax3 = plt.subplots()

sns.countplot(
    data=df,
    x="experience_level",
    ax=ax3
)

ax3.set_xlabel("Experience")
ax3.set_ylabel("Job Count")

st.pyplot(fig3)

st.markdown("---")

st.subheader("Most Requested AI Skills")

skills_series = df["required_skills"].str.split(",").explode()

top_skills = skills_series.value_counts().head(10)

fig4, ax4 = plt.subplots()

sns.barplot(
    x=top_skills.values,
    y=top_skills.index,
    ax=ax4
)

st.markdown("---")

st.subheader("Remote vs On-site Jobs")

work_counts = df["remote_work"].value_counts()

fig5, ax5 = plt.subplots()

ax5.pie(
    work_counts.values,
    labels=work_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

ax5.axis("equal")

st.pyplot(fig5)

ax4.set_xlabel("Frequency")


st.pyplot(fig4)
