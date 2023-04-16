import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_excel("2022_student1_10projects_combined.xlsx")

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
sns.scatterplot(data=data, x='Name', y='score', hue='label', palette=label_colors)

# Set the axis labels and title
plt.xlabel('Project Name')
plt.ylabel('Score')
plt.title('Sentiment Analysis Results')

# Set the x-axis tick labels
tick_labels = ['dream1', 'dream2', 'dream3', 'frank', 'lofi', 'omni', 'remix', 'rube', 'testing', 'tool']
plt.xticks(range(10), tick_labels, rotation=45)

# Create a boxplot of the score for each file number and label
#sns.boxplot(data=data, x=tick_labels, y='score', hue='label', palette=label_colors, width=0.4, whis=1.5, dodge=True)

# Set the legend outside the plot and adjust spacing
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.subplots_adjust(right=0.8)


# Save the plot
plt.savefig("2022_student01_10proj_SA.png")

# Display the plot
plt.show()