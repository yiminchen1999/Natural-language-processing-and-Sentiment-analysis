import pandas as pd

# Loop through all CSV files and convert to Excel format
for i in range(1, 13):
    csv_filename = f'frank_2022_SA_{i:02}.csv'  # Format the filename
    excel_filename = f'frank_2022_SA_{i:02}.xlsx'  # Format the filename for the Excel file
    df = pd.read_csv(csv_filename)
    df.to_excel(excel_filename, index=False)
