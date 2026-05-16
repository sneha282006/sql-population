import streamlit as st
import pandas as pd

# Read CSV file
df = pd.read_csv("population.csv")

# Dashboard title
st.title("Population Dashboard")

# Show table
st.write(df)

# Show column names
st.write(df.columns)

# Use first text column automatically
gender_count = df.iloc[:, 1].value_counts()

# Show gender distribution
st.subheader("Gender Distribution")
st.write(gender_count)

# Bar chart
st.bar_chart(gender_count)

# Age chart
st.subheader("Age Distribution")
st.bar_chart(df.iloc[:, 2])
