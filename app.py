import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Customer Journey Insights Dashboard")

# Load data
df = pd.read_csv("data.csv")

# Show raw data
with st.expander("Show Raw Data"):
    st.dataframe(df)

# Unique stages
stages = df['stage'].unique()

# Drop-off analysis
st.subheader("Customer Drop-off Analysis")
journey_counts = df.groupby('customer_id')['stage'].nunique().value_counts().sort_index()
st.bar_chart(journey_counts)

# Satisfaction score by stage
st.subheader("Satisfaction Scores by Stage")
avg_scores = df.groupby('stage')['satisfaction_score'].mean().reset_index()
fig = px.bar(avg_scores, x='stage', y='satisfaction_score', color='satisfaction_score',
             title="Average Satisfaction per Stage")
st.plotly_chart(fig)

# KPIs
st.subheader("Key Metrics")
total_customers = df['customer_id'].nunique()
completed = df[df['stage'] == 'Usage']['customer_id'].nunique()
completion_rate = round((completed / total_customers) * 100, 2)
avg_satisfaction = round(df['satisfaction_score'].mean(), 2)

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", total_customers)
col2.metric("Journey Completion", f"{completion_rate}%")
col3.metric("Avg Satisfaction", avg_satisfaction)
