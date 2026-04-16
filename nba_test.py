from nba_api.stats.endpoints import leagueleaders
import pandas as pd
import sys

# Now targeting the current 2024-25 season
print("Fetching historical data for 1995-96 and current for 2024-25...")

try:
    # Get 1995-96 data for comparison
    data_90s = leagueleaders.LeagueLeaders(season='1995-96').get_data_frames()[0]
    
    # Get 2024-25 data (Current Season)
    data_modern = leagueleaders.LeagueLeaders(season='2024-25').get_data_frames()[0]

    if data_90s.empty or data_modern.empty:
        print("Data is empty. Check your connection or season parameters.")
        sys.exit()

    # Calculation function to avoid repetition
    def calculate_pace(df):
        total_fga = df['FGA'].sum()
        total_fta = df['FTA'].sum()
        total_oreb = df['OREB'].sum()
        total_tov = df['TOV'].sum()
        total_min = df['MIN'].sum()
        total_poss = total_fga + (0.44 * total_fta) - total_oreb + total_tov
        return (total_poss / (total_min / 5)) * 48

    pace_95 = calculate_pace(data_90s)
    pace_modern = calculate_pace(data_modern)

    print(f"\n--- Analysis Results (Updated for 2024-25) ---")
    print(f"Calculated Pace for 1995-96: {pace_95:.2f}")
    print(f"Calculated Pace for 2024-25: {pace_modern:.2f}")
    print(f"Difference: {pace_modern - pace_95:.2f} possessions.")

except Exception as e:
    print(f"Error: {e}")