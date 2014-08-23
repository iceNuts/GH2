import random
import nltk

from collections import Counter
from nltk.corpus import *
from nltk.tag import pos_tag

def word_count(article, wordType, count=50):
    tagged = pos_tag(nltk.regexp_tokenize(article.lower(), r'\w+', gaps=False))
    tagged_dic = [word for word, pos in tagged if pos[0] == wordType]
    hist = nltk.FreqDist(tagged_dic).items()[0:count]
    return hist

def get_similiarity(word1, word2):
    try:
        synset1 = wordnet.synsets(word1, pos=wordnet.NOUN)[0]
        synset2 = wordnet.synsets(word2, pos=wordnet.NOUN)[0]
        return wordnet.path_similarity(synset1, synset2)
    except:
        return 0

def get_similar_words(original_word, wordList):
    children = []
    for word in wordList:
        if (get_similiarity(original_word, word[0])) > 0.2 and (get_similiarity(original_word, word[0])) < 1:
            children.append(word[0])
    return {'name': original_word, 'children': children};
    
def build_similiarity_tree(original_word, wordList, levelRemains):
    similiarity_tree = get_similar_words(original_word, wordList)
    if levelRemains > 0:
        children = []
        for word in similiarity_tree['children']:
            children.append(build_similiarity_tree(word, wordList, levelRemains-1));
        similiarity_tree['children'] = children;
    return similiarity_tree;

def get_related_sentence(word, raw, sample_size = 5):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    all_sentence = [" ".join(sentence.split()) for sentence in tokenizer.tokenize(raw) if 'freedom' in sentence]
    return random.sample(all_sentence, sample_size)
