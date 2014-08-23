import json

from nltk.probability import FreqDist
from nltk.tag import pos_tag

def word_count(article, wordType, count=50):
    tagged = pos_tag(article.split())
    tagged_dic = [word for word, pos in tagged if pos == wordType]
    fdist = FreqDist(tagged_dic)
    return json.dumps(fdist)