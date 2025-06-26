import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
from datetime import datetime
import requests
from streamlit_lottie import st_lottie

# Load Lottie animation from URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Show logo smaller in sidebar
def show_sidebar_logo():
    try:
        logo = Image.open("bsg_logo.png")
        st.sidebar.image(logo, width=120)
    except:
        st.sidebar.write("**BSG Logo Here**")

# Show logo on login page (larger)
def show_login_logo():
    try:
        logo = Image.open("bsg_logo.png")
        st.image(logo, width=250)
    except:
        st.write("**BSG Logo Here**")

# Login function (no experimental_rerun)
def login():
    correct_username = "Keanu"
    correct_password = "Keanumoodley1"

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.markdown("""
            <style>
                .login-title {
                    text-align: center;
                    font-size: 2.2rem;
                    color: #3a3a3a;
                    margin-bottom: 10px;
                }
                .login-subtitle {
                    text-align: center;
                    font-size: 1rem;
                    color: #666;
                    margin-bottom: 20px;
                }
            </style>
            <div class='login-title'>🔐 Welcome to Keanu's Dashboard</div>
            <div class='login-subtitle'>Please log in to access customer insights</div>
        """, unsafe_allow_html=True)

        show_login_logo()
        login_animation = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json")
        if login_animation:
            st_lottie(login_animation, height=250)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == correct_username and password == correct_password:
                st.session_state.logged_in = True
                st.success("Login successful 🎉")
            else:
                st.error("Incorrect username or password")
        return False
    else:
        return True

# Main app code
def main():
    st.set_page_config(
        page_title="BSG Customer Journey Dashboard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    if login():
        show_sidebar_logo()

        df = pd.read_csv("data.csv", parse_dates=["timestamp"])
        segments = df['segment'].unique()
        regions = df['region'].unique()

        st.sidebar.title("🔍 Filters")
        selected_segment = st.sidebar.selectbox("Select Segment", ["All"] + list(segments))
        selected_region = st.sidebar.selectbox("Select Region", ["All"] + list(regions))

        df_filtered = df.copy()
        if selected_segment != "All":
            df_filtered = df_filtered[df_filtered['segment'] == selected_segment]
        if selected_region != "All":
            df_filtered = df_filtered[df_filtered['region'] == selected_region]

        st.markdown("""
            <style>
                .main-title {
                    font-size: 2.5rem;
                    font-weight: 600;
                    color: #3a3a3a;
                    padding-bottom: 10px;
                }
                .sub-title {
                    font-size: 1.2rem;
                    color: #555;
                    margin-top: -10px;
                    padding-bottom: 20px;
                }
            </style>
            <div class='main-title'>📊 BSG Customer Journey Dashboard</div>
            <div class='sub-title'>Tracking engagement & satisfaction across key stages</div>
        """, unsafe_allow_html=True)

        # Optional animation in main page header
        dashboard_animation = load_lottie_url("https://assets4.lottiefiles.com/private_files/lf30_l8csvcry.json")
        if dashboard_animation:
            st_lottie(dashboard_animation, height=150)

        # KPIs
        st.markdown("### 📌 Key Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Customers", df_filtered['customer_id'].nunique())
        col2.metric("Avg Satisfaction", round(df_filtered['satisfaction_score'].mean(), 2))
        col3.metric("Low Scores (<5)", df_filtered[df_filtered['satisfaction_score'] < 5].shape[0])
        st.markdown("---")

        # Satisfaction Over Time
        st.markdown("### 📈 Satisfaction Over Time")
        fig1 = px.line(df_filtered.groupby("timestamp")["satisfaction_score"].mean().reset_index(),
                    x="timestamp", y="satisfaction_score")
        st.plotly_chart(fig1, use_container_width=True)

        # Stage Counts
        st.markdown("### 🧭 Customer Stage Distribution")
        fig2 = px.histogram(df_filtered, x="stage", color="segment", barmode="group")
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("---")

        # Drilldown
        st.sidebar.header("📌 Customer Drilldown")
        selected_customer = st.sidebar.selectbox("Select Customer ID", df_filtered['customer_id'].unique())
        if selected_customer:
            cust_data = df_filtered[df_filtered['customer_id'] == selected_customer].sort_values(by='timestamp')
            st.markdown(f"### 🧑 Journey Details: Customer {selected_customer}")
            st.table(cust_data[['stage', 'timestamp', 'satisfaction_score', 'segment', 'region']])
            fig3 = px.line(cust_data, x='timestamp', y='satisfaction_score', markers=True)
            st.plotly_chart(fig3, use_container_width=True)

        st.markdown("### 🚨 Satisfaction Alerts")
        low_scores = df_filtered[df_filtered['satisfaction_score'] < 5]
        if not low_scores.empty:
            st.warning(f"⚠️ {len(low_scores['customer_id'].unique())} customer(s) have scores below 5.")
            if st.checkbox("Show low score details"):
                st.dataframe(low_scores[['customer_id', 'stage', 'timestamp', 'satisfaction_score', 'segment', 'region']])
        else:
            st.success("✅ No customers with low satisfaction scores!")

        st.markdown("---")
        st.caption(f"🕒 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
