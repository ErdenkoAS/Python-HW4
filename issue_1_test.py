# -*- coding: utf-8 -*-
"""issue_1_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r3H-BU3pbVkGMRjGC0PfH5C4RV7kPAFW
"""

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}


def encode(message: str) -> str:

    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)

    """
    tests

    >>> encode('LA LA')
    '.-.. .-   .-.. .-'
    >>> encode('111')
    '.---- .---- .----'
    >>> encode('SOS')
    '... --- ...'
    >>> encode('')
    ''
    >>> encode(1)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
    """