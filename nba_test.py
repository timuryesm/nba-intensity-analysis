import pandas as pd
from nba_api.stats.endpoints import leaguestandingsv3, teamestimatedmetrics
from sklearn.linear_model import LinearRegression

class NBAPredictor:
    def __init__(self):
        self.model = LinearRegression()
        self.training_seasons = ['2020-21', '2021-22', '2022-23', '2023-24', '2024-25']

    def train_model(self):
        combined_data = []
        for season in self.training_seasons:
            standings = leaguestandingsv3.LeagueStandingsV3(season=season).get_data_frames()[0]
            metrics = teamestimatedmetrics.TeamEstimatedMetrics(season=season).get_data_frames()[0]
            merged = pd.merge(
                standings[['TeamID', 'WINS']], 
                metrics[['TEAM_ID', 'E_NET_RATING', 'E_PACE', 'E_OFF_RATING', 'E_DEF_RATING']], 
                left_on='TeamID', right_on='TEAM_ID'
            )
            combined_data.append(merged)
        
        df = pd.concat(combined_data)
        X = df[['E_NET_RATING', 'E_PACE', 'E_OFF_RATING', 'E_DEF_RATING']]
        y = df['WINS']
        self.model.fit(X, y)

    def predict_season(self, season='2025-26'):
        current_metrics = teamestimatedmetrics.TeamEstimatedMetrics(season=season).get_data_frames()[0]
        X_current = current_metrics[['E_NET_RATING', 'E_PACE', 'E_OFF_RATING', 'E_DEF_RATING']]
        current_metrics['PREDICTED_WINS'] = self.model.predict(X_current)
        return current_metrics[['TEAM_ID', 'TEAM_NAME', 'PREDICTED_WINS']]