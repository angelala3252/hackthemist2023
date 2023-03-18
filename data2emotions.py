""" This file converts a sentence's mood into a RBG colour.
"""

import text2emotion
from nltk.sentiment import SentimentIntensityAnalyzer


def give_sentiment(text: str) -> int:
    """
    Return an int between 0 and 255 inclusive representing the sentiment from text, where
    255 represents the most negative sentiment.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    result = sentiment['neg']

    # convert for hex
    result = result * 255
    return round(result)


def give_sadness(text: str) -> int:
    """
    Return an int between 0 and 255 inclusive representing the amount of sadness in text, where
    255 represents the most sad.
    """
    result = text2emotion.get_emotion(text)
    sad = result['Sad']
    # get the correct amount
    sad = sad * 255
    sad = round(sad)
    return sad


def give_passion(text: str) -> int:
    """
    Return an int between 0 and 255 inclusive representing the amount of passion in text,
    calculated as the percentage of text (not including the spaces) that is a capital letter or
    exclamation mark. Stretches of question marks together (more than 1) also count.
    """

    # Tokenize using whitespaces
    tokens = text.split()
    passion_chars = 0
    for token in tokens:
        for i in range(0, len(token)):
            if token[i].isupper() or token[i] == '!':
                passion_chars += 1
            elif i < len(token) - 1 and token[i] == '?' and token[i + 1] in {'?', '!'}:
                passion_chars += 1
            elif i > 0 and token[i] == '?' and token[i - 1] in {'?', '!'}:
                passion_chars += 1

    num_chars = sum([len(token) for token in tokens])
    passion = passion_chars / num_chars

    return round(passion * 255)
