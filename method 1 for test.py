import nltk
nltk.download('punkt')  # download the punkt tokenizer if needed

# define your keywords
keywords = ['keyword1', 'keyword2', 'keyword3']

# assuming your dataset is a dictionary where the keys are years and the values are lists of texts for that year
dataset = {
    2021: ['text1', 'text2', 'text3'],
    2022: [''],
    2023: ['']
}

import os

# Set the directory containing the data files
data_dir = "/path/to/data/files"

# Set the keywords you want to extract
keywords = ["keyword1", "keyword2", "keyword3"]

# Set the output file name
output_file = "output.txt"

# Iterate through each year
for year in range(2000, 2023):
    year_texts = []
    year_file = os.path.join(data_dir, f"{year}.txt")

    # Read in the texts for the year
    with open(year_file, "r") as f:
        year_texts = f.read().split("\n\n")

    # Iterate through each text for the year
    for text in year_texts:
        # Extract the sentences containing the keywords
        sentences = []
        for sentence in text.split("."):
            for keyword in keywords:
                if keyword in sentence:
                    sentences.append(sentence.strip())
                    break

        # Write the extracted sentences to the output file
        if sentences:
            with open(output_file, "a") as f:
                f.write(f"Year: {year}\n")
                f.write(f"Text: {text}\n")
                f.write("Sentences:\n")
                for sentence in sentences:
                    f.write(f"\t- {sentence}\n")
                f.write("\n")
