
# import libraries
import pandas as pd
import os
from transformers import pipeline

# # combine txt files that start with "01" in the folder "Year_2021_corpus" into one txt file called "Year_2021_corpus_01.txt" and so on.
# for i in range(7):
#     with open("Year_2021_corpus_0" + str(i+1) + ".txt", "w") as f:
#         for file_name in os.listdir("Year_2021_corpus"):
#             if file_name.startswith("0"+str(i+1)):
#                 with open("Year_2021_corpus/" + file_name, "r") as f1:
#                     f.write(f1.read())


# run following code if you get SSL certificate error
import ssl
#try:
    #_create_unverified_https_context = ssl._create_unverified_context
#except AttributeError:
    #pass
#else:
    #ssl._create_default_https_context = _create_unverified_https_context
#nltk.download()


# read a file from local folder and save it as a data frame called "dictionary"
dictionary = pd.read_excel("dictionary 2.0.xlsx")
# extract keyword list from dictionary
keyword_list = dictionary["traget n-gram"].tolist()
# print(keyword_list)

def keyword_sentence(file_name):
    # read a txt file save all sentences which are separated by period and remove any new line in a list called "sentences"
    with open(file_name, "r") as f:
        sentences = f.read().split(".")
        sentences = [sentence.strip() for sentence in sentences]

    # find out sentences in sentences list which contain any keyword in keyword list and save those sentences in a list called "keyword_sentences"
    keyword_sentences = []
    for sentence in sentences:
        for keyword in keyword_list:
            if keyword in sentence:
                keyword_sentences.append(sentence)

    return keyword_sentences

#frank project
Year_2022_s1 = keyword_sentence("Year 2022/01_frank.txt")
Year_2022_s2 = keyword_sentence("Year 2022/02_frank.txt")
Year_2022_s3 = keyword_sentence("Year 2022/03_frank.txt")
Year_2022_s4 = keyword_sentence("Year 2022/04_frank.txt")
Year_2022_s5 = keyword_sentence("Year 2022/05_frank.txt")
Year_2022_s6 = keyword_sentence("Year 2022/06_frank.txt")
Year_2022_s7 = keyword_sentence("Year 2022/07_frank.txt")
Year_2022_s8 = keyword_sentence("Year 2022/08_frank.txt")
Year_2022_s9 = keyword_sentence("Year 2022/09_frank.txt")
Year_2022_s10 = keyword_sentence("Year 2022/10_frank.txt")
Year_2022_s11 = keyword_sentence("Year 2022/11_frank.txt")
Year_2022_s12 = keyword_sentence("Year 2022/12_frank.txt")

#classifer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")
#res = classifer(Year_2021_s1)
#print(res)
print(Year_2022_s1)

import nltk

nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#importing the necessary libraries
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#creating an instance of the SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


#defining a function to get the sentiment of a sentence
def sentiment_analyzer_scores(sentences):
    # create an empty list to store the scores for each sentence
    scores_list = []
    for sentence in sentences:
        # get the sentiment score for the sentence
        score = sid.polarity_scores(sentence)
        # add the score to the list
        scores_list.append(score)
    # return the list of scores
    return scores_list


# call the function on each list of sentences
scores_2022_s1 = sentiment_analyzer_scores(Year_2022_s1)
scores_2022_s2 = sentiment_analyzer_scores(Year_2022_s2)
# repeat for each list of sentences

# print the list of scores for the first sentence in each list
print(scores_2022_s1[0])
print(scores_2022_s2[0])
# repeat for each list of scores

def print_sentiment_scores(sentences):
    for sentence in sentences:
        # calculate the sentiment score for the sentence
        score = sid.polarity_scores(sentence)
        # print the sentence and its score
        print(f"{sentence}: {score}")
        print("\n")

# sample call to the function
Year_2022_s1 = keyword_sentence("Year 2022/01_frank.txt")
print_sentiment_scores(Year_2022_s1)

import pandas as pd


def sentiment_scores_to_dataframe(sentences):
    scores = []
    for sentence in sentences:
        # calculate the sentiment score for the sentence
        score = sid.polarity_scores(sentence)
        scores.append(score)

    # create a DataFrame from the scores
    df = pd.DataFrame(scores)
    # add a column with the sentence text
    df["Sentence"] = sentences
    # reorder the columns
    df = df[["Sentence", "neg", "neu", "pos", "compound"]]

    return df


# generate sentiment scores and save them to an Excel file for each file
for i in range(1, 13):
    filename = f"Year 2022/{i:02d}_frank.txt"
    sentences = keyword_sentence(filename)
    df = sentiment_scores_to_dataframe(sentences)
    output_filename = f"{i:02d}_frank_sentiment_scores.xlsx"
    df.to_excel(output_filename, index=False)


#Here's what the above class is doing, explained in a concise way:


   # 1. Read a txt file and save all sentences which are separated by period and remove any new line in a list called "sentences".
   # 2. Find out sentences in sentences list which contain any keyword in keyword list and save those sentences in a list called "keyword_sentences".
   # 3. Create an instance of the SentimentIntensityAnalyzer.
   # 4. Define a function to get the sentiment of a sentence.
   # 5. Call the function on each list of sentences.
   # 6. Print the list of scores for the first sentence in each list.
   # 7. Define a function to print the sentiment of a sentence.
   # 8. Generate sentiment scores and save