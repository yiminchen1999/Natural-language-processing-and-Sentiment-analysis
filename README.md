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

# Meaning of compound score
    In sentiment analysis, the compound score is a metric that represents the overall sentiment polarity of a piece of text. 
    It is calculated by taking the sum of all the lexicon ratings which have been normalized between -1 (most extreme negative) and +1 (most extreme positive), and then normalized between -1 (most extreme negative) and +1 (most extreme positive).
    The compound score ranges from -1 to 1, where a score of -1 indicates the most negative sentiment, 0 indicates a neutral sentiment, and 1 indicates the most positive sentiment. 
    The compound score is often used to interpret the sentiment of a piece of text as a single number, making it easier to compare and analyze sentiment across different texts.