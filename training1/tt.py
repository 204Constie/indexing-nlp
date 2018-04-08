import re
import nltk
import random
import numpy as np
import sklearn as skl
import pandas as pd

letters = []

# file = open('/Users/constie/Documents/indexing/training1/sample.txt', 'r', encoding='utf-8')
try:
    with open('/Users/constie/Documents/indexing/training1/sample.txt', 'r', encoding='utf-8') as file:
        text = file.readlines()
        file.close()
except OSError:
    # 'File not found' error message.
    print("File not found")


# remove \n
text = [x.strip() for x in text]


class Letter:
    def __init__(self, letter_desc, letter_contents):
        self.desc = letter_desc
        self.contents = letter_contents

    def print_desc(self):
        for line in self.desc:
            print(line.encode('utf-8'))

    def print_contents(self):
        for line in self.contents:
            print(line.encode('utf-8'))

def letter_parser():
    desc = []
    contents = []

    for letter_line in letter_list:
        if not letter_line.startswith('<tresc>'):
            desc.append(letter_line)
        else:
            if not letter_line.startswith('</tresc>'):
                contents.append(letter_line)
            else:
                return desc, contents
    return desc, contents


chunks = []
chunks.append([])
for line in text:
    if not line.startswith('List'):
        chunks[-1].append(line)
    else :
        chunks.append([])
        chunks[-1].append(line)
for letter_list in chunks:
    desc, contents = letter_parser()
    letters.append(Letter(desc, contents))



print(str(len(letters)))
[letter.print_contents() for letter in letters]


# for chunk in chunks:
#     for word in chunk:
#         print(word.encode('utf-8'))
