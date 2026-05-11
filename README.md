# 🏀 NBA Win-Prediction Engine (2025-26 Season)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](https://nba-intensity-analysis-timuryesm.streamlit.app/)
[![GitHub Pages](https://img.shields.io/badge/View_Presentation-Slide_Deck-ff79c6?logo=github)](https://timuryesm.github.io/nba-intensity-analysis/)

## 📝 Project Overview
This project is an end-to-end data analytics pipeline designed to predict NBA regular-season win totals. By leveraging historical efficiency metrics (2020-2025), the model identifies which team characteristics most accurately correlate with success in the modern "Pace and Space" era.

### 🔗 Key Destinations
*   **[Live Interactive Dashboard](https://nba-intensity-analysis-timuryesm.streamlit.app/):** Explore model residuals and test "What-If" scenarios.
*   **[Professional Presentation Deck](https://timuryesm.github.io/nba-intensity-analysis/):** A deep dive into the methodology, feature engineering, and outlier analysis.

---

## 🚀 The Tech Stack
*   **Engine:** Python 3.10
*   **Model:** Scikit-Learn (Linear Regression)
*   **Data Source:** `nba_api` (Official NBA.com stats)
*   **Visualization:** Plotly, Seaborn, Matplotlib
*   **Deployment:** Streamlit Cloud & GitHub Pages

---

## 📊 Performance Analysis
The model achieved a **Mean Absolute Error (MAE) of ~2.8 wins**, proving highly accurate for teams with consistent efficiency profiles.

![Model Performance](nba_model_performance_2026.png)

### Model Insights:
*   **The Benchmarks:** The model predicted the **OKC Thunder** and **Houston Rockets** with <1.0 win error, suggesting their success is purely driven by elite efficiency metrics.
*   **The Anomalies:** 
    *   **LA Lakers (+7.86 Error):** Significantly outperformed statistical expectations, likely due to high veteran IQ in "clutch" situations.
    *   **Charlotte Hornets (-6.97 Error):** Underperformed relative to efficiency, indicating a gap in late-game execution or depth.

---

## 🛠️ Installation & Usage
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/timuryesm/nba-intensity-analysis.git](https://github.com/timuryesm/nba-intensity-analysis.git)