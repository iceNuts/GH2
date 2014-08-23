import json

from collections import Counter
from nltk.tag import pos_tag

def word_count(article, wordType, count=50):
    tagged = pos_tag(article.split())
    tagged_dic = [word for word, pos in tagged if pos == wordType]
    hist = Counter(tagged_dic)
    return json.dumps(hist.most_common(count))