
#把每一年里的每个text都提取一遍 然后每个text里含keyword的句子都提取出来
#先把2023的学生1，2，3先做test，然后跑出来一个sample
#hugging face

from typing import List
import numpy as np
import nltk
from itertools import chain
nltk.download('punkt')


# import libraries
import pandas as pd
import os

# # combine txt files that start with "01" in the folder "Year_2021_corpus" into one txt file called "Year_2021_corpus_01.txt" and so on.
# for i in range(7):
#     with open("Year_2021_corpus_0" + str(i+1) + ".txt", "w") as f:
#         for file_name in os.listdir("Year_2021_corpus"):
#             if file_name.startswith("0"+str(i+1)):
#                 with open("Year_2021_corpus/" + file_name, "r") as f1:
#                     f.write(f1.read())

# read a file from local folder and save it as a data frame called "dictionary"
dictionary = pd.read_excel("dictionary 2.0.xlsx")
# extract keyword list from dictionary
keyword_list = dictionary["traget n-gram"].tolist()
print(keyword_list)

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


Year_2021_s1 = keyword_sentence("Year_2021_corpus_01.txt")
Year_2021_s2 = keyword_sentence("Year_2021_corpus_02.txt")
Year_2021_s3 = keyword_sentence("Year_2021_corpus_03.txt")
Year_2021_s4 = keyword_sentence("Year_2021_corpus_04.txt")
Year_2021_s5 = keyword_sentence("Year_2021_corpus_05.txt")
Year_2021_s6 = keyword_sentence("Year_2021_corpus_06.txt")
Year_2021_s7 = keyword_sentence("Year_2021_corpus_07.txt")

def get_keyword_sentences(year):
    return [keyword_sentence(f"Year_{year}_corpus_{i:02}.txt") for i in range(1, 8)]
