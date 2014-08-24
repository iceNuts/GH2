import random
import nltk

from sets import Set
from nltk.corpus import *
from nltk.tag import pos_tag

def word_count(article, wordType, count=30):
    tagged = pos_tag(nltk.regexp_tokenize(article.lower(), r'\w+', gaps=False))
    tagged_dic = [word for word, pos in tagged if len(word)>1 and pos[0] == wordType]
    hist = nltk.FreqDist(tagged_dic).items()[0:count]
    return hist

def hist_convert_to_dic(hist):
    numbers = []
    for entry in reversed(hist):
        numbers.append({'word': entry[0], 'count': entry[1]})
    return {'numbers': numbers}

def word_count_in_json(article, wordType, count=30):
    hist = word_count(article, wordType, count)
    return hist_convert_to_dic(hist)

def get_similiarity(word1, word2):
    try:
        synset1 = wordnet.synsets(word1, pos=wordnet.NOUN)[0]
        synset2 = wordnet.synsets(word2, pos=wordnet.NOUN)[0]
        return wordnet.path_similarity(synset1, synset2)
    except:
        return 0
    
def turple_to_dic(word):
    return {'name': word[0], 'size': word[1]}

def get_similar_words(original_word, wordList):
    children = []
    for word in wordList:
        if (get_similiarity(original_word[0], word[0])) > 0.15 and (get_similiarity(original_word[0], word[0])) < 1:
            children.append((word[0], word[1]))
    return {'name': original_word[0], 'size': original_word[1], 'children': children};
    
def build_similiarity_tree(original_word, wordList, levelRemains = 3):
    similiarity_tree = get_similar_words(original_word, wordList)
    if levelRemains > 0:
        children = []
        for word in similiarity_tree['children']:
            children.append(build_similiarity_tree(word, wordList, levelRemains-1));
    else:
        children = []
        for word in similiarity_tree['children']:
            children.append(turple_to_dic(word))
    similiarity_tree['children'] = children;
    return similiarity_tree;

def build_similiarity_tree_all(wordList, count=30):
    tree = []
    for word in wordList:
        tree.append({'word': word[0], 'tree': build_similiarity_tree(word, wordList)})
    return tree

def get_related_sentence(word, raw, sample_size = 5):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    all_sentence = [" ".join(sentence.split()) for sentence in tokenizer.tokenize(raw) if word[0] in sentence]
    return random.sample(all_sentence, min(sample_size, len(all_sentence)))

def get_related_sentence_all(wordList, raw):
    chain = []
    for word in wordList:
        chain.append({'word': word[0], 'chain': get_related_sentence(word, raw)})
    return chain

def get_relative_words(original_word, sentence):
    tagged = pos_tag(nltk.word_tokenize(sentence.lower()));
    tagged_dic = Set()
    for word, pos in tagged:
        if pos[0] == 'N' and word != original_word:
            tagged_dic.add(word)
    return tagged_dic

def build_relative_tree(original_word, raw, levelRemains = 5):
    sentences = get_related_sentence(original_word, raw)
    relative_words = Set()
    for sentence in sentences: 
        relative_words |= get_relative_words(original_word, sentence)
    print relative_words


    