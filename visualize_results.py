import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data we exported earlier
df = pd.read_csv('nba_final_eval_2026.csv')

# 2. Set the visual style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 8))

# 3. Create the Scatter Plot
# We'll use 'hue' to color by Error, so we can see under/overperformers visually
scatter = sns.scatterplot(
    data=df, 
    x='PREDICTED_WINS', 
    y='ACTUAL_WINS', 
    hue='ERROR', 
    palette='vlag', 
    size='ACTUAL_WINS',
    sizes=(50, 400),
    alpha=0.7
)

# 4. Add the "Perfect Prediction" Line (y = x)
line_coords = [df['ACTUAL_WINS'].min(), df['ACTUAL_WINS'].max()]
plt.plot(line_coords, line_coords, color='red', linestyle='--', label='Perfect Prediction')

# 5. Label the Outliers (The "Storytelling" part)
# We'll label teams where the error is greater than 4 wins
for i in range(df.shape[0]):
    if abs(df.ERROR[i]) > 4:
        plt.text(
            df.PREDICTED_WINS[i] + 0.5, 
            df.ACTUAL_WINS[i] + 0.5, 
            df.TEAM_NAME[i], 
            fontsize=9, 
            weight='bold'
        )

# 6. Final Formatting
plt.title('NBA 2025-26: Predicted vs. Actual Win Totals', fontsize=16)
plt.xlabel('Model Predicted Wins', fontsize=12)
plt.ylabel('Actual Wins (Final Standings)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the visualization for your website/GitHub
plt.savefig('nba_model_performance_2026.png', dpi=300)
print("Chart generated: 'nba_model_performance_2026.png'")
plt.show()