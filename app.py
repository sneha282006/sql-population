import streamlit as st
import pandas as pd

# Read CSV file
df = pd.read_csv("population.csv")

# Show column names
st.write("Columns in CSV:", df.columns)

# Dashboard title
st.title("Population Dashboard")

# Show table
st.write(df)

# Use correct column name
gender_count = df["Gender"].value_counts()

# Show gender distribution
st.subheader("Gender Distribution")
st.write(gender_count)

# Bar chart
st.bar_chart(gender_count)

# Age chart
st.subheader("Age Distribution")
st.bar_chart(df["age"])
