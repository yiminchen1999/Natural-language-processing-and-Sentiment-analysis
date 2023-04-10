
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
all_scores_df = pd.read_excel("2022_frank_sentiment_scores.xlsx")

# Define the color palette for each sentiment
colors = ["#E74C3C", "#95A5A6", "#2ECC71", "#3498DB"]
#colors = ["#E74C3C", "#95A5A6", "#2ECC71"]

# Set the plot style
sns.set_style("ticks")
sns.set_context("talk")

# Melt the dataframe to long format
melted_df = all_scores_df.melt(id_vars=["File", "Sentence"], value_vars=["Negative", "Neutral", "Positive", "Compound"], var_name="Sentiment")

#ignore compound
#melted_df = all_scores_df.melt(id_vars=["File", "Sentence"], value_vars=["Negative", "Neutral", "Positive"], var_name="Sentiment")
#, "Compound"],
# Create the boxplot
fig, ax = plt.subplots(figsize=(12, 8))
sns.boxplot(x="File", y="value", hue="Sentiment", data=melted_df, ax=ax, palette=colors)
sns.stripplot(x="File", y="value", hue="Sentiment", data=melted_df, ax=ax, jitter=0.2, size=6, edgecolor='gray', linewidth=0.5)
plt.xticks(range(12), range(1, 13))
plt.title("Sentiment Analysis Scores for 12 Student Files for Frank Project", fontsize=20, fontweight='bold')
plt.xlabel("Student Number ", fontsize=16)
plt.ylabel("Sentiment Score", fontsize=16)
sns.despine(offset=10, trim=True)
plt.tight_layout()
plt.savefig("folder for plot/2022_compound_frank_sentiment_analysis_scores.png")
plt.show()



