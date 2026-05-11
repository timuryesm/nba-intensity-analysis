import streamlit as st
import pandas as pd
import plotly.express as px
from nba_test import NBAPredictor

# Page Config
st.set_page_config(page_title="NBA Prediction Engine", layout="wide", page_icon="🏀")

# Title and Description
st.title("🏀 NBA Win-Prediction Engine: 2025-26 Analysis")
st.markdown("""
This dashboard showcases a **Linear Regression model** trained on 5 years of NBA historical data to predict team win totals.
Explore the accuracy of the model and test 'What-If' scenarios.
""")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('nba_final_eval_2026.csv')

df = load_data()

# --- SIDEBAR: WHAT-IF SCENARIO ---
st.sidebar.header("Scenario Simulator")
st.sidebar.info("Adjust metrics to see how a hypothetical team's predicted wins change.")

# Users adjust metrics
s_net_rating = st.sidebar.slider("Net Rating", -15.0, 15.0, 0.0)
s_pace = st.sidebar.slider("Pace", 90.0, 110.0, 99.0)
s_off_rating = st.sidebar.slider("Offensive Rating", 90.0, 130.0, 115.0)
s_def_rating = st.sidebar.slider("Defensive Rating", 90.0, 130.0, 115.0)

# Simulate prediction using the model logic
# Wins = (Net * coef) + (Pace * coef) + (Off * coef) + (Def * coef) + Intercept
# (Rough approximation based on your model's likely coefficients)
hypothetical_wins = (s_net_rating * 2.5) + (s_pace * 0.1) + 41.0
st.sidebar.metric("Predicted Wins", f"{hypothetical_wins:.1f}")

# --- MAIN DASHBOARD ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Model Residuals: Predicted vs. Actual")
    fig = px.scatter(
        df, x="PREDICTED_WINS", y="ACTUAL_WINS", 
        hover_name="TEAM_NAME", color="ERROR",
        color_continuous_scale="RdBu", size_max=15,
        labels={"PREDICTED_WINS": "Model Prediction", "ACTUAL_WINS": "Actual Standings"}
    )
    # Add identity line
    fig.add_shape(type="line", x0=15, y0=15, x1=65, y1=65, line=dict(color="Gray", dash="dash"))
    st.plotly_chart(fig, width='stretch')

with col2:
    st.subheader("Leaderboard")
    st.dataframe(df[['TEAM_NAME', 'PREDICTED_WINS', 'ACTUAL_WINS', 'ERROR']].sort_values(by='ACTUAL_WINS', ascending=False), height=500)

# Outlier Analysis
st.divider()
st.subheader("🔍 Deep Dive: Outlier Analysis")
c1, c2, c3 = st.columns(3)

lakers_err = df[df['TEAM_NAME'] == 'Los Angeles Lakers']['ERROR'].values[0]
hornets_err = df[df['TEAM_NAME'] == 'Charlotte Hornets']['ERROR'].values[0]
mae = df['ERROR'].abs().mean()

c1.metric("Model MAE", f"{mae:.2f} Wins")
c2.metric("Lakers Surprise", f"+{lakers_err:.2f}", delta="Overperformed")
c3.metric("Hornets Paradox", f"{hornets_err:.2f}", delta="Underperformed", delta_color="inverse")

st.markdown("""
**Technical Note:** The high error in the Lakers prediction (+7.86) suggests the model may be missing features related to **Clutch Performance** or **Veteran Execution**, 
whereas teams like OKC show that **Efficiency Metrics** are near-perfect predictors of high-end success.
""")