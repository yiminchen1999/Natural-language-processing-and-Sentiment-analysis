
#把每一年里的每个text都提取一遍 然后每个text里含keyword的句子都提取出来
#先把2023的学生1，2，3先做test，然后跑出来一个sample
#hugging face

from typing import List
import numpy as np


import glob

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
        content = f.read()
        sentences = content.split(".")
        sentences = [sentence.strip() for sentence in sentences]

    # find out sentences in sentences list which contain any keyword in keyword list and save those sentences in a list called "keyword_sentences"
    keyword_sentences = []
    for sentence in sentences:
        for keyword in keyword_list:
            if keyword in sentence:
                keyword_sentences.append(sentence)

    # join the keyword sentences with '\n' to form a single string
    result = '\n'.join(keyword_sentences)
    return result


def simplify_and_save(year):
    year_str = str(year)
    file_pattern = f"{year_str}/*.txt"
    file_list = glob.glob(file_pattern)
    result = []
    for file in file_list:
        sentence = keyword_sentence(file)
        result.extend(sentence)
    with open(f"{year_str}_results.txt", "w") as file:
        file.write('\n'.join(result) + '\n')
    return result



Year_2023_s1 = keyword_sentence("Year 2023/01_frank.txt")
print(Year_2023_s1)
#Year_2023_s2 = keyword_sentence("Year 2023/01_omni.txt")
#Year_2023_s3 = keyword_sentence("Year 2023/01_remix.txt")
#Year_2023_s4 = keyword_sentence("Year 2023/01_rube.txt")



results = simplify_and_save(2023)
print(results)
