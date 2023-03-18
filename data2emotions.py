""" This file contains
"""

import text2emotion
from nltk.sentiment import SentimentIntensityAnalyzer


def give_sentiment(text: str) -> int:
    """
    Return a float that represents the sentiment of the given text.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    result = sentiment['neg']

    # convert for hex
    result = result * 255
    return round(result)


def give_sadness(text: str) -> int:
    """
    Take the Sad decimal associated with the text and
    multiply it by 255.

    """
    result = text2emotion.get_emotion(text)
    sad = result['Sad']
    # get the correct amount
    sad = sad * 255
    sad = round(sad)
    return sad


def emotions_to_colour(emotions: dict) -> tuple:
    """
    Convert the emotions in emotions into a tuple of an RGB colour,
    according to the following scales:


    """
