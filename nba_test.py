from nba_api.stats.endpoints import leagueleaders
import pandas as pd
import sys

print("Fetching historical data via LeagueLeaders for the 1995-96 season...")

try:
    # Stable endpoint for historical NBA data
    data_90s = leagueleaders.LeagueLeaders(
        season='1995-96',
        season_type_all_star='Regular Season'
    ).get_data_frames()[0]

    if data_90s.empty:
        print("Data is empty. The NBA API might be throttling requests or the season is unavailable.")
        sys.exit()
    else:
        print(f"Success! Data retrieved. Players found: {len(data_90s)}")
        
        # Displaying sample of the raw data for verification
        print("\n--- Data Sample ---")
        print(data_90s[['PLAYER', 'GP', 'MIN', 'FGA', 'FTA', 'REB', 'TOV']].head())

    # Calculating aggregates for the manual Pace formula
    total_fga = data_90s['FGA'].sum()
    total_fta = data_90s['FTA'].sum()
    total_oreb = data_90s['OREB'].sum()
    total_tov = data_90s['TOV'].sum()
    total_min = data_90s['MIN'].sum()

    # Possession Formula: FGA + 0.44 * FTA - OREB + TOV
    total_possessions = total_fga + (0.44 * total_fta) - total_oreb + total_tov

    # Pace Formula: (Possessions / (Minutes / 5)) * 48
    pace_95 = (total_possessions / (total_min / 5)) * 48

    print(f"\n--- Analysis Results ---")
    print(f"Calculated Pace for the 1995-96 season: {pace_95:.2f}")
    print(f"Official Pace for the 2023-24 season (from API): 99.15")
    print(f"Difference in Intensity: {99.15 - pace_95:.2f} possessions per game.")
    print(f"Game intensity has increased by {((99.15/pace_95)-1)*100:.1f}% compared to the Jordan era.")

except Exception as e:
    print(f"Error during execution: {e}")