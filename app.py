import streamlit as st
import pandas as pd
import plotly.express as px

# App config
st.set_page_config(page_title="Customer Journey Dashboard", layout="wide")

# --- Theme colors
color_sequence = ['#004D7A', '#34699A', '#7CA3C2']

# --- Sidebar ---
st.sidebar.markdown("## 🏢 BSG Demo Dashboard")
st.sidebar.markdown("### 🔽 Navigation")
st.sidebar.markdown("- Filter Data\n- Overview\n- Drop-off\n- Satisfaction\n- Timeline & Funnel\n- Export")

# --- Title ---
st.title("📊 Customer Journey Insights Dashboard")

# --- How to Use ---
with st.expander("🧭 How to Use This Dashboard"):
    st.markdown("""
    - Use the sidebar to filter by customer journey stage.
    - Explore drop-off trends, satisfaction metrics, and journey progression.
    - View funnel stages and download filtered data.
    """)

# --- Load Data ---
df = pd.read_csv("data.csv")

# --- Filter ---
st.sidebar.header("🔍 Filter")
selected_stage = st.sidebar.selectbox("Select Stage", options=["All"] + list(df['stage'].unique()))
if selected_stage != "All":
    df = df[df['stage'] == selected_stage]

# --- Raw Data ---
with st.expander("📂 Show Raw Data"):
    st.dataframe(df)

# --- Metrics ---
st.markdown("## 📌 Key Metrics")
total_customers = df['customer_id'].nunique()
completed = df[df['stage'] == 'Usage']['customer_id'].nunique()
completion_rate = round((completed / total_customers) * 100, 2) if total_customers else 0
avg_satisfaction = round(df['satisfaction_score'].mean(), 2)

col1, col2, col3 = st.columns(3)
col1.metric("👥 Total Customers", total_customers)
col2.metric("✅ Completion Rate", f"{completion_rate}%")
col3.metric("⭐ Avg Satisfaction", avg_satisfaction)

# --- Insights ---
st.markdown("## 💡 Quick Insights")
if completion_rate < 60:
    st.error("🚨 High drop-off rate! Consider improving onboarding or sending follow-ups.")
if avg_satisfaction < 6:
    st.warning("⚠️ Customer satisfaction is low. Investigate user experience issues.")
else:
    st.success("✅ Overall journey and satisfaction appear healthy.")

# --- Drop-off Analysis ---
st.markdown("## 📉 Drop-off Analysis")
journey_counts = df.groupby('customer_id')['stage'].nunique().value_counts().sort_index()
st.bar_chart(journey_counts)

# --- Satisfaction Scores ---
st.markdown("## 😊 Satisfaction Scores by Stage")
avg_scores = df.groupby('stage')['satisfaction_score'].mean().reset_index()
fig = px.bar(avg_scores, x='stage', y='satisfaction_score', color='satisfaction_score',
             title="Average Satisfaction per Stage",
             color_continuous_scale='blues')
st.plotly_chart(fig, use_container_width=True)

# --- Timeline & Funnel Side-by-Side ---
st.markdown("## ⏱️ Timeline & Funnel")
colA, colB = st.columns(2)

with colA:
    st.subheader("📈 Customer Progress Timeline")
    timeline_data = df.sort_values(['customer_id', 'timestamp'])
    fig2 = px.line(timeline_data, x='timestamp', y='stage', color='customer_id',
                   markers=True, title="Customer Progression Over Time",
                   color_discrete_sequence=color_sequence)
    st.plotly_chart(fig2, use_container_width=True)

with colB:
    st.subheader("🔻 Journey Funnel")
    funnel_data = df.drop_duplicates(subset=['customer_id', 'stage'])
    funnel_counts = funnel_data['stage'].value_counts().reindex(['Signup', 'Onboarding', 'Usage'])
    fig3 = px.funnel(funnel_counts.reset_index(), x='stage', y='count',
                     title="Customer Journey Funnel",
                     color_discrete_sequence=color_sequence)
    st.plotly_chart(fig3, use_container_width=True)

# --- Download Button ---
st.markdown("## ⬇️ Export")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Filtered Data", csv, "filtered_data.csv", "text/csv")

# --- Footer Use Cases ---
st.markdown("---")
st.markdown("### 🧑‍💼 Use Case Examples")
st.markdown("""
- 📱 Telecom company tracking app onboarding.
- 💳 Bank analyzing digital account setup.
- 🛍️ E-commerce platform improving user retention.
""")
