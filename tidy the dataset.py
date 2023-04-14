import pandas as pd
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
# Load dictionary
dictionary = pd.read_excel("dictionary 2.0.xlsx")
keyword_list = dictionary["traget n-gram"].tolist()

import pandas as pd

# Loop through all CSV files and convert to Excel format
for i in range(1, 13):
    csv_filename = f'frank_2022_SA_{i:02}.csv'  # Format the filename
    excel_filename = f'frank_2022_SA_{i:02}.xlsx'  # Format the filename for the Excel file
    df = pd.read_csv(csv_filename)
    df.to_excel(excel_filename, index=False)

# create an empty list to store the dataframes
df_list = []

# loop through the filenames and read each file into a dataframe
for i in range(1, 13):
    filename = f"huggingface model for comparison/frank_2022_SA_{i:02d}.xlsx"  # format the filename
    df = pd.read_excel(filename)
    df_list.append(df)

# concatenate the dataframes into one
final_df = pd.concat(df_list)


# add a new column to the final dataframe with the file number
# add a new column to the final dataframe with the file number
final_df['file_number'] = [i for i in range(1, 13) for _ in range(len(pd.read_excel(f"huggingface model for comparison/frank_2022_SA_{i:02d}.xlsx")))]

# Separate the "sentiment" column into two columns "label" and "score"
final_df[['label', 'score']] = final_df['sentiment'].str.extract(r"{'label': '(\w+)', 'score': (\d.\d+)}")

# Drop the original "sentiment" column
final_df.drop('sentiment', axis=1, inplace=True)
# save the final dataframe to a new file
final_df.to_excel("frank_2022_SA_01_combined.xlsx", index=False)


