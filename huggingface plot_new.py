import pandas as pd

# Read in the input file
df = pd.read_excel("frank_2022_SA_01_combined.xlsx")

# Pivot the data to have one row per file number with columns for each label's score
df_pivoted = df.pivot_table(index="file_number", columns="label", values="score", aggfunc="first").reset_index()

# Rename the columns
df_pivoted.columns.name = None
df_pivoted.columns = ["file_number", "negative", "neutral", "positive"]

# Write the output file
df_pivoted.to_excel("frank_2022_SA_01_combined_new.xlsx", index=False)



