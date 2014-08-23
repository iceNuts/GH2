import nltk_process
from nltk.corpus import *

f = open('testfile.txt')
raw = f.read()
wordList =  nltk_process.word_count(raw, "N");
print wordList
print nltk_process.build_similiarity_tree("freedom", wordList, 2);