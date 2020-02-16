#!/usr/bin/env python
"""This script is used to load all the global variables that take time to load during runtime"""

with open("utils/english.txt") as f:
    STOPWORDS = [line.rstrip() for line in f]

EMBEDDINGS = {}
with open("utils/glove.twitter.27B.25d.txt", 'r', encoding='utf8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = values[1:]
        EMBEDDINGS[word] = vector
