import pandas as pd
import os
import ssl
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
from transformers import pipeline

# read a file from local folder and save it as a data frame called "dictionary"
dictionary = pd.read_excel("dictionary 2.0.xlsx")
# extract keyword list from dictionary
keyword_list = dictionary["traget n-gram"].tolist()


#def keyword_sentence(file_name, added_sentences=set()):
    #with open(file_name, "r") as f:
        #sentences = f.read().split(".")
        #sentences = [sentence.strip() for sentence in sentences]
    #keyword_sentences = []
    #for sentence in sentences:
        #for keyword in keyword_list:
            #if keyword in sentence and sentence not in added_sentences:
                #keyword_sentences.append(sentence)
                #added_sentences.add(sentence)
    #return keyword_sentences

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

# create an instance of the SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


def sentiment_scores_to_dataframe(sentences):
    scores = []
    for sentence in sentences:
        # calculate the sentiment score for the sentence
        score = sid.polarity_scores(sentence)
        # add the sentence and its score to the list
        scores.append({'sentence': sentence, 'score': score})

    # create a DataFrame from the scores
    df = pd.DataFrame(scores)

    return df




# generate sentiment scores and save them to an Excel file for each file
for i in range(1, 13):
    filename = f"Year 2022/{i:02d}_frank.txt"
    sentences = keyword_sentence(filename)
    df = sentiment_scores_to_dataframe(sentences)
    #output_filename = f"{i:02d}_frank_sentiment_scores_ver2.xlsx"
    output_filename = f"{i:02d}_frank_sentiment_scores_ver3.xlsx"
    # add a column for the filename and save the DataFrame to an Excel file
    df['filename'] = filename
    df.to_excel(output_filename, index=False)  # write the DataFrame to an Excel file


#Here's what the above class is doing, explained in a concise way:


   # 1. Read a txt file and save all sentences which are separated by period and remove any new line in a list called "sentences".
   # 2. Find out sentences in sentences list which contain any keyword in keyword list and save those sentences in a list called "keyword_sentences".
   # 3. Create an instance of the SentimentIntensityAnalyzer.
   # 4. Define a function to get the sentiment of a sentence.
   # 5. Call the function on each list of sentences.
   # 6. Print the list of scores for the first sentence in each list.
   # 7. Define a function to print the sentiment of a sentence.
   # 8. Generate sentiment scores and save