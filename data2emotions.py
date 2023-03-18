""" This file contains
"""

import text2emotion


def sadness(text: str) -> int:
    """
    take the Sad decmal associated with the text
    multiply it by 255

    """
    result = text2emotion.get_emotion(text)
    sad = result['Sad']
    # get the correct amount
    sad = sad * 255
    sad = round(sad)
    return sad
