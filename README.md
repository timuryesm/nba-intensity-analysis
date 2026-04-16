# NBA Game Intensity & Durability Analysis

### Project Overview
This project investigates the evolution of NBA game intensity and its potential impact on player durability. By comparing the "Jordan Era" (1995-96) with the "Modern Era" (2023-24), I analyzed the change in game pace and player workload.

### Key Findings
- **Historical Pace Gap:** There is a significant increase in game intensity.
- **1995-96 Season (Calculated):** 93.80 Pace
- **2023-24 Season (Official):** 99.15 Pace
- **Intensity Increase:** Game pace has increased by **5.7%** (approx. 5.35 more possessions per game).

### Technical Challenges Overcome
- **Data Recovery:** Fixed `NaN` issues in the NBA API for historical seasons by manually calculating Pace using the formula: `Possessions = FGA + 0.44 * FTA - OREB + TOV`.
- **API Handling:** Implemented robust data fetching using the `leagueleaders` endpoint to ensure 100% data integrity for the 90s era.

### Tech Stack
- **Python 3.10**
- **Pandas** (Data Manipulation)
- **NBA_API** (Data Sourcing)