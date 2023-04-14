import matplotlib.pyplot as plt
import pandas as pd
import json
# read the excel file
df = pd.read_excel('frank_2022_SA_01.xlsx')

import matplotlib.pyplot as plt
import pandas as pd

# Define the data as a pandas DataFrame
data = pd.DataFrame({
    'sentiment': ['neutral', 'negative', 'neutral', 'neutral', 'positive', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'positive', 'positive', 'neutral', 'neutral', 'negative', 'neutral'],
    'file_number': [1]*23
})

# Group the data by sentiment and file_number and calculate the mean sentiment score
grouped_data = data.groupby(['sentiment', 'file_number']).size().reset_index(name='count')

# Create a boxplot of the sentiment scores by file number
plt.boxplot([
    grouped_data[grouped_data['sentiment'] == 'negative']['count'],
    grouped_data[grouped_data['sentiment'] == 'neutral']['count'],
    grouped_data[grouped_data['sentiment'] == 'positive']['count']
], labels=['Negative', 'Neutral', 'Positive'])

# Set the plot title and axis labels
plt.title('Sentiment Analysis Results by File Number')
plt.xlabel('File Number')
plt.ylabel('Sentiment')

# Show the plot
plt.show()
