from nba_test import NBAPredictor
from nba_api.stats.endpoints import leaguestandingsv3
import pandas as pd

# 1. Initialize and Run your Model
print("Running prediction model...")
predictor = NBAPredictor()
predictor.train_model()
predictions = predictor.predict_season('2025-26')

# 2. Retrieve ACTUAL wins from NBA API for all 30 teams
print("Fetching actual 2025-26 standings...")
live_standings = leaguestandingsv3.LeagueStandingsV3(season='2025-26').get_data_frames()[0]
actuals = live_standings[['TeamID', 'WINS']].rename(columns={'WINS': 'ACTUAL_WINS'})

# 3. Connect the two: Merge Predictions with Actuals
final_report = pd.merge(predictions, actuals, left_on='TEAM_ID', right_on='TeamID')

# 4. Calculate error metrics for all 30 teams
final_report['ERROR'] = final_report['ACTUAL_WINS'] - final_report['PREDICTED_WINS']
final_report = final_report.sort_values(by='ACTUAL_WINS', ascending=False)

print("\n--- Full 30-Team Comparison: 2025-26 Season ---")
print(final_report[['TEAM_NAME', 'PREDICTED_WINS', 'ACTUAL_WINS', 'ERROR']].to_string(index=False))

# Save for your website
final_report.to_csv('nba_final_eval_2026.csv', index=False)
print("\nExported full results to 'nba_final_eval_2026.csv'")

total_mae = final_report['ERROR'].abs().mean()
print(f"\nFinal Portfolio Metric - Mean Absolute Error: {total_mae:.2f} wins")