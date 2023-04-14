import matplotlib.pyplot as plt
import pandas as pd
import json
# read the excel file
df = pd.read_excel('frank_2022_SA_03.xlsx')

# Initialize counters for each sentiment label
neg_count = 0
neu_count = 0
pos_count = 0

# Iterate over each row and increment the corresponding counter
for i, row in df.iterrows():
    sentiment = eval(row['sentiment'])  # Convert string to dictionary
    if sentiment['label'] == 'negative':
        neg_count += 1
    elif sentiment['label'] == 'neutral':
        neu_count += 1
    elif sentiment['label'] == 'positive':
        pos_count += 1

# Create a list of sentiment counts
counts = [neg_count, neu_count, pos_count]

# Create a list of sentiment labels
labels = ['Negative', 'Neutral', 'Positive']

# Define colors for each sentiment label
colors = {'Negative': 'red', 'Neutral': 'gray', 'Positive': 'green'}

# Create a list of color values based on the sentiment labels
bar_colors = [colors[label] for label in labels]

# Create a bar plot of sentiment counts with custom colors
plt.bar(labels, counts, color=bar_colors)

# Set plot title and labels
plt.title('Distribution of Sentiment Scores for 2022_frank_03')
plt.xlabel('Sentiment Label')
plt.ylabel('Count')

# Show plot
plt.show()
plt.savefig("2022_frank03_count.png")



# Extract the sentiment scores
#scores = []
#for sentiment in df['sentiment']:
    #sentiment_dict = json.loads(sentiment.replace("'", "\""))
    #scores.append(sentiment_dict['score'])

# create bar plot
#fig, ax = plt.subplots()
#ax.bar(df['sentence'], scores)
#ax.set_ylabel('Sentiment Score')
#plt.xticks(rotation=90)
#plt.tight_layout()
#plt.show()