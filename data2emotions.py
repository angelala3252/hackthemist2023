""" This file contains
"""

import text2emotion


def give_emotions(text: str) -> tuple:
    """
    Given a chunk of text, return a dictionary containing the scores of each emotion from {'Angry',
    'Fear','Happy','Sad','Surprise'}
    """
    result = text2emotion.get_emotion(text)
    return result


def emotions_to_colour(emotions: dict) -> tuple:
    """
    Convert the emotions in emotions into a tuple of an RGB colour,
    according to the following scales:

    """
