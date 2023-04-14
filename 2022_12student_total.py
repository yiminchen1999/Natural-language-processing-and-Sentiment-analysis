import pandas as pd
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
# Load dictionary
dictionary = pd.read_excel("dictionary 2.0.xlsx")
keyword_list = dictionary["traget n-gram"].tolist()
# Define function to get keyword sentences
def keyword_sentence(file_name, added_sentences=set()):
    with open(file_name, "r") as f:
        text = f.read().replace("\n", " ")
    sentences = re.findall(r'\b.+?[.!?]+(?:\s|\n\n|$)', text)
    keyword_sentences = []
    for sentence in sentences:
        for keyword in keyword_list:
            if keyword in sentence and sentence not in added_sentences:
                keyword_sentences.append(sentence)
                added_sentences.add(sentence)
    return keyword_sentences


# Define function to get sentiment scores
def get_sentiment_scores(keyword_sentences):
    sid = SentimentIntensityAnalyzer()
    scores = []
    for sentence in keyword_sentences:
        score = sid.polarity_scores(sentence)
        scores.append(score)
    return scores

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

all_scores_df.to_excel("2022_frank__sentiment_scores.xlsx", index=False)


