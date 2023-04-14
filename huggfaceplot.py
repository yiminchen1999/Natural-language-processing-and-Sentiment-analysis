import pandas as pd
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
# Load dictionary
dictionary = pd.read_excel("dictionary 2.0.xlsx")
keyword_list = dictionary["traget n-gram"].tolist()

# Get all sentences and scores for each file
all_scores = []
for i in range(1, 13):
    file_name = f"Year 2022/{i:02d}_frank.txt"
    keyword_sentences = keyword_sentence(file_name)
    scores = get_sentiment_scores(keyword_sentences)
    for j, score in enumerate(scores):
        all_scores.append({
            "Sentence": keyword_sentences[j],
            "Negative": score["neg"],
            "Neutral": score["neu"],
            "Positive": score["pos"],
            "File": file_name
        })

# Convert scores to dataframe and save to Excel
all_scores_df = pd.DataFrame(all_scores)

all_scores_df.to_excel("2022_frank_huggingfacetotal_sentiment_scores.xlsx", index=False)


