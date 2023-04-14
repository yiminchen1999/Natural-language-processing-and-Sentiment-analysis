import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_excel("frank_2022_SA_01_combined.xlsx")

# Define a dictionary mapping labels to colors
label_colors = {'positive': 'green', 'negative': 'red', 'neutral': 'grey'}

# Create a new column in the DataFrame containing the color for each label
data['color'] = data['label'].map(label_colors)

# Set the plot style
sns.set_style("ticks")
sns.set_context("talk")

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data as a scatter plot using the colors from the 'color' column
sns.scatterplot(data=data, x='file_number', y='score', hue='label', palette=label_colors)

# Set the axis labels and title
plt.xlabel('File Number')
plt.ylabel('Score')
plt.title('Sentiment Analysis Results')

# Create a boxplot of the score for each file number and label
sns.boxplot(data=data, x='file_number', y='score', hue='label', palette=label_colors, width=0.4, whis=1.5, dodge=True)

# Set the legend outside the plot and adjust spacing
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.subplots_adjust(right=0.8)

# Save the plot
plt.savefig("folder for plot/2022_ver3_frank_sentiment_analysis_scores.png")

# Display the plot
plt.show()




