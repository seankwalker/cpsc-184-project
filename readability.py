"""
    readability.py

    Sean Walker

    CPSC 184, Spring 2019
    Final Project

    Implements various readability metrics for text analysis.
"""

import string

from nltk.tokenize import sent_tokenize, word_tokenize
import pyphen


def calculate_fk_ease(text):
    """
    Calculates Flesch-Kincaid readability ease for given text.

    See https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests

    Formula: 206.835 - (1.015 * (total words / total sentences)) - 84.6 * 
             ((total syllables / total words))
    """
    num_sentences = 0
    num_syllables = 0
    num_words = 0

    # initialize a hyphen dictionary (for English): we can use this to count
    # word syllables
    hyph = pyphen.Pyphen(lang="en_US")

    sentences = sent_tokenize(text)

    for sentence in sentences:
        # get count of number of words
        # note: must explicitly not include punctuation, as `word_tokenize`
        # treats punctuation as separate words
        words = word_tokenize(sentence)
        filter(lambda word: word not in string.punctuation, words)

        # tally parameters
        num_sentences += 1
        num_words += len(words)
        for word in words:
            num_syllables += len(hyph.inserted(word).split("-"))

    # calculate metric
    return 206.835 - (1.015 * (num_words / num_sentences)) - (84.6 * (num_syllables / num_words))


def calculate_fk_grade_level(text):
    pass
