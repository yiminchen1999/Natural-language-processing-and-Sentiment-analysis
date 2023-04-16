import pandas as pd
import os

# Define a list of filenames without extension
file_names = ['01_dream1_SA', '01_dream2_SA', '01_dream3_SA', '01_frank_SA', '01_lofi_SA', '01_omni_SA', '01_remix_SA',
              '01_rube_SA', '01_testing_SA', '01_tool_SA']

# Loop through each filename
for file_name in file_names:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(f'{file_name}.csv')

    # Add a new column with the file name
    df['Name'] = file_name

    # Write the DataFrame to an Excel file with the same name
    df.to_excel(f'{file_name}.xlsx', index=False)

    # Optional: Delete the original CSV file
    #os.remove(f'{file_name}.csv')

import os

# Define a list of filenames without extension
file_names1 = ['01_dream1_SA', '01_dream2_SA', '01_dream3_SA', '01_frank_SA', '01_lofi_SA', '01_omni_SA', '01_remix_SA', '01_rube_SA', '01_testing_SA', '01_tool_SA']

# Create an empty list to store all the DataFrames
dfs = []

# Loop through each filename
for file_name1 in file_names1:
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(f'{file_name1}.xlsx')

    # Append the DataFrame to the list
    dfs.append(df)

# Concatenate all the DataFrames into a single DataFrame
combined_df = pd.concat(dfs)

# Write the combined DataFrame to a new Excel file
combined_df.to_excel('2022_student1_10projects_combined.xlsx', index=False)
