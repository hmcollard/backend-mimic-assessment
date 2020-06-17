#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Haley Collard with help from Ruben Espino and Joanne M. Fixed error in second part with help from study group demo"

import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    with open(filename, 'r') as f:
        text = f.read()
        all_words = text.split()
        mimic_dict = {'': [all_words[0]]}
        for i, word in enumerate(all_words):
            if i < len(all_words)-1:
                next_word = i + 1
                if word in mimic_dict:
                    mimic_dict[word].append(all_words[next_word])
                else:
                    mimic_dict[word] = [all_words[next_word]]
    return mimic_dict


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    silly_sentence = []
    silly_sentence.append(start_word)
    for _ in range(200):
        new_word = random.choice(mimic_dict.get(start_word))
        if not new_word:
            new_word = ''
        silly_sentence.append(new_word)
        start_word = new_word
    print(' '.join(silly_sentence))
# Provided main(), calls mimic_dict() and print_mimic()


def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
