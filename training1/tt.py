# -*- coding: utf-8 -*-

import re
import nltk
import random
import numpy as np
import sklearn as skl
import pandas as pd
from morfeusz2 import Morfeusz

letters = []

# file = open('/Users/constie/Documents/indexing/training1/sample.txt', 'r', encoding='utf-8')
try:
    with open('/Users/constie/Documents/indexing/training1/sample.txt', 'r') as file:
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
            print(line)

    def print_contents(self):
        for line in self.contents:
            print(line)
    def get_as_str(self, part):
        if part == 'desc':
            return ''.join(self.desc)
        else:
            return ''.join(self.contents)


# def annotation_remover(line):
#     str = ''
#     for letter in line:
#

def letter_parser(letter_list):
    desc = []
    contents = []
    i=0

    while letter_list[i] != '<tresc>':
        # print(letter_list[i])
        desc.append(letter_list[i])
        i = i + 1
    # i = i + 1
    while letter_list[i] != '</tresc>':
        contents.append(letter_list[i])
        i = i + 1
    return(desc, contents)

def empty_line_cleaning(letter_list):
    tmp = []
    for line in letter_list:
        if line != '':
            tmp.append(line)
    return tmp

def remove_tags(letter_contents):
    tmp_list = []
    for stri in letter_contents:
        tmp_str = ''
        i=0
        while i<len(stri):
            if stri[i] == '<':
                while stri[i] != '>' and i<len(stri):
                    i = i + 1
                # i = i + 1
            if stri[i] != '>':
                tmp_str = tmp_str + stri[i]
            i = i + 1
        if tmp_str != '':
            tmp_list.append(tmp_str)
    return tmp_list

chunks = []
for line in text:
    if not line.startswith('List - edycja'):
        chunks[-1].append(line)
    else:
        chunks.append([])
        chunks[-1].append(line)

for letter_list in chunks:
    # remove empty lines
    letter_list = empty_line_cleaning(letter_list)
    # print(letter_list)
    desc, contents = letter_parser(letter_list)
    letters.append(Letter(desc, contents))



# print(str(len(letters)))
# [letter.print_contents() for letter in letters]
letter_contents = letters[0].get_as_str('')
print(letter_contents)


# regex to match anything in tags:
# <([a-z]*)(\s+[a-z]*="\w*((\s+\w*)+)?")?>(.+?)<\/[a-z]*>
# two word compounds:
# <([a-z]*-[a-z]*)(\s+[a-z]*="\w*((\s+\w*)+)?")?>(.+?)<\/[a-z]*-[a-z]*>
# regex to match tags:

tags_word = re.findall(r'<([a-z]*)(\s+[a-z]*="\w*((\s+\w*)+)?")?>(.+?)<\/[a-z]*>', letter_contents)
tags_words = re.findall(r'<([a-z]*-[a-z]*)(\s+[a-z]*="\w*((\s+\w*)+)?")?>(.+?)<\/[a-z]*-[a-z]*>', letter_contents)
# print('one word tags')
# for tag in tags_word:
#     print(tag)
#     print('\n')
# print('two word tags')
# for tag in tags_words:
#     print(tag)
#     print('\n')

def remove_dashes(text):
    tmp_str = ''
    for letter in text:
        if letter != '-':
            tmp_str = tmp_str + letter
    return tmp_str

letter1_no_tags = remove_tags(letters[0].contents)
letter1_nt_str = ' '.join(letter1_no_tags)
# letter_ntnd_str = remove_dashes(letter1_nt_str.decode('utf-8'))
# print(letter_ntnd_str)

morf = Morfeusz()
# print(morf)
print(letter1_nt_str.decode('utf8'))
letter1_analysed = morf.analyse(letter1_nt_str)
print(letter1_analysed)
