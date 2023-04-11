# Natural-language-processing-and-Sentiment-analysis
# Here's what the above class is doing, explained in a concise way:
    1. Read a txt file and save all sentences which are separated by period and remove any new line in a list called "sentences".
    2. Find out sentences in sentences list which contain any keyword in keyword list and save those sentences in a list called "keyword_sentences".
    3. Create an instance of the SentimentIntensityAnalyzer.
    4. Define a function to get the sentiment of a sentence.
    5. Call the function on each list of sentences.
    6. Print the list of scores for the first sentence in each list.
    7. Define a function to print the sentiment of a sentence.
    8. Generate sentiment scores and save

# about SentimentIntensityAnalyzer
    SentimentIntensityAnalyzer is a tool from the Natural Language Toolkit (NLTK) library that is used to analyze the sentiment of a given text.
    It uses a lexicon of words to assign a score to a given text based on the sentiment of the words it contains.
    The score is a value between -1 and 1, with -1 being the most negative sentiment and 1 being the most positive sentiment.

# Lexicon-based
    Lexicon-based sentiment analysis is a type of sentiment analysis that uses a predefined set of words, or lexicon, to identify the sentiment of a given text. 
    This type of sentiment analysis is based on the idea that certain words have a positive or negative connotation, and by counting the number of positive and negative words in a text, the sentiment of the text can be determined. 
    Lexicon-based sentiment analysis is often used in natural language processing (NLP) applications, such as text classification and sentiment analysis.

# Meaning of compound score
    In sentiment analysis, the compound score is a metric that represents the overall sentiment polarity of a piece of text. 
    It is calculated by taking the sum of all the lexicon ratings which have been normalized between -1 (most extreme negative) and +1 (most extreme positive), and then normalized between -1 (most extreme negative) and +1 (most extreme positive).
    The compound score ranges from -1 to 1, where a score of -1 indicates the most negative sentiment, 0 indicates a neutral sentiment, and 1 indicates the most positive sentiment. 
    The compound score is often used to interpret the sentiment of a piece of text as a single number, making it easier to compare and analyze sentiment across different texts.

# sample output for 2022 12students' frank project
![alt text](https://github.com/yiminchen1999/Natural-language-processing-and-Sentiment-analysis/blob/421aa61891257c8c7b43116cbc2c7d92318e46b3/folder%20for%20plot/2022_ver2_frank_sentiment_analysis_scores.png)

# sample output for 2022 12students' omni project
![alt text](https://github.com/yiminchen1999/Natural-language-processing-and-Sentiment-analysis/blob/cbb375a7319717a3b999efad32c80c88ef922def/folder%20for%20plot/2022_ver2_omni_sentiment_analysis_scores.png)

# sample output for 2022 12students' remix project
![alt text](https://github.com/yiminchen1999/Natural-language-processing-and-Sentiment-analysis/blob/cbb375a7319717a3b999efad32c80c88ef922def/folder%20for%20plot/2022_ver2_remix_sentiment_analysis_scores.png)

# sample output for 2022 12students' dream1 project
![alt text](https://github.com/yiminchen1999/Natural-language-processing-and-Sentiment-analysis/blob/cbb375a7319717a3b999efad32c80c88ef922def/folder%20for%20plot/2022_ver2_dream1_sentiment_analysis_scores.png)

# sample output for 2022 12students' rube project
![alt text](https://github.com/yiminchen1999/Natural-language-processing-and-Sentiment-analysis/blob/cbb375a7319717a3b999efad32c80c88ef922def/folder%20for%20plot/2022_ver2_rube_sentiment_analysis_scores.png)

