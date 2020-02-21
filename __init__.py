#!/usr/bin/env python
"""This script is used to load all the global variables that take time to load during runtime"""
import os
from zipfile import ZipFile

with open("utils/english.txt") as f:
    STOPWORDS = [line.rstrip() for line in f]

EMBEDDINGS = {}
with open("utils/glove.twitter.27B.25d.txt", 'r', encoding='utf8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = values[1:]
        EMBEDDINGS[word] = vector

with open("utils/glove.twitter.27B.25d.2.txt", 'r', encoding='utf8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = values[1:]
        EMBEDDINGS[word] = vector

with open("utils/glove.twitter.27B.25d.3.txt", 'r', encoding='utf8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = values[1:]
        EMBEDDINGS[word] = vector

# word_list = EMBEDDINGS.keys()

# with open ('glove.txt', 'a', encoding='utf-8') as out_file:
#     out_file.write('\n'.join(word_list))

file_path = "utils\glove.zip\glove.txt"
if ".zip\\" in file_path:
    archive_path = os.path.abspath(file_path)
    split = archive_path.split(".zip\\")
    archive_path = split[0] + ".zip"
    path_inside = split[1]
    archive = ZipFile(archive_path, "r")
    WORD_LIST = archive.read(path_inside).decode("utf8").split("\n")

WORD_LIST = [x.strip() for x in WORD_LIST]