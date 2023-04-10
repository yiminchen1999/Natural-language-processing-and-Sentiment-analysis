import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load dictionary
dictionary = pd.read_excel("dictionary 2.0.xlsx")
keyword_list = dictionary["traget n-gram"].tolist()

# Define function to get keyword sentences
def keyword_sentence(file_name):
    with open(file_name, "r") as f:
        sentences = f.read().split(".")
        sentences = [sentence.strip() for sentence in sentences]
    keyword_sentences = []
    for sentence in sentences:
        for keyword in keyword_list:
            if keyword in sentence:
                keyword_sentences.append(sentence)
    return keyword_sentences

# Define function to get sentiment scores
def get_sentiment_scores(keyword_sentences):
    sid = SentimentIntensityAnalyzer()
    scores = []
    for sentence in keyword_sentences:
        score = sid.polarity_scores(sentence)
        scores.append(score)
    return scores

# Define function to process sentiment scores for a single file
def process_scores_for_file(file_name):
    keyword_sentences = keyword_sentence(file_name)
    scores = get_sentiment_scores(keyword_sentences)
    all_scores = []
    for j, score in enumerate(scores):
        all_scores.append({
            "Sentence": keyword_sentences[j],
            "Negative": score["neg"],
            "Neutral": score["neu"],
            "Positive": score["pos"],
            "Compound": score["compound"],
            "File": file_name
        })
    # Convert scores to dataframe and return
    all_scores_df = pd.DataFrame(all_scores).drop_duplicates(subset="Sentence")
    return all_scores_df

# Define function to process sentiment scores for all files
def process_scores_for_all_files():
    all_scores_combined = []
    for i in range(1, 13):
        file_name = f"Year 2022/{i:02d}_frank.txt"
        all_scores_combined.append(process_scores_for_file(file_name))
    all_scores_combined_df = pd.concat(all_scores_combined, ignore_index=True)
    return all_scores_combined_df

# Process sentiment scores for all files
all_scores_combined_df = process_scores_for_all_files()

# Group scores by file and compute mean sentiment scores for each file
mean_scores_by_file = all_scores_combined_df.groupby("File").mean()

# Display mean sentiment scores by file
print(mean_scores_by_file)
