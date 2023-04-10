
#把每一年里的每个text都提取一遍 然后每个text里含keyword的句子都提取出来
#先把2023的学生1，2，3先做test，然后跑出来一个sample
#hugging face

from typing import List
import numpy as np


import glob
from transformers import AutoTokenizer, TFXLMRobertaForSequenceClassification


# import libraries
import pandas as pd
import os
import pandas as pd
from transformers import pipeline
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
    with open(file_name, "r") as f:
        content = f.read()
        sentences = content.split(".")
        sentences = [sentence.strip() for sentence in sentences]

    keyword_sentences = []
    for sentence in sentences:
        for keyword in keyword_list:
            if keyword in sentence:
                keyword_sentences.append(sentence)

    return keyword_sentences



def simplify_and_save(year):
    year_str = str(year)
    file_pattern = f"Year {year_str}/*.txt"
    file_list = glob.glob(file_pattern)

    # create a dictionary to group sentences by student name
    result = {
        "omni": [],
        "frank": [],
        "remix": [],
        "rube": []
    }

    for file in file_list:
        student = file.split("_")[1].split(".")[0]  # extract student name from file name
        sentences = keyword_sentence(file)
        result[student].extend(sentences)

    # write the results to separate files for each student
    for student, sentences in result.items():
        with open(f"{year_str}_{student}.txt", "w") as file:
            file.write('\n'.join(sentences) + '\n')

    return result


#Year_2023_s1 = keyword_sentence("Year 2023/01_frank.txt")
#Year_2023_s2 = keyword_sentence("Year 2023/01_omni.txt")
#Year_2023_s3 = keyword_sentence("Year 2023/01_remix.txt")
#Year_2023_s4 = keyword_sentence("Year 2023/01_rube.txt")



results = simplify_and_save(2023)


classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")
with open("2023_frank.txt", "r") as f:
    text = f.read()
    result_frank = classifier(text)
print(result_frank)

with open("2023_omni.txt", "r") as f:
    text = f.read()
    result_omni = classifier(text)
print(result_omni)

with open("2023_rube.txt", "r") as f:
    text = f.read()
    result_rube = classifier(text)
print(result_rube)