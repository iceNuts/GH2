import nltk_process

f = open('testfile.txt')
raw = f.read()
wordList =  nltk_process.word_count(raw, "N");
#print wordList
#print nltk_process.build_similiarity_tree("freedom", wordList, 2);
related_sentence = nltk_process.get_related_sentence("freedom", raw);
for sentence in related_sentence:
    print sentence.strip();

# related_sentence = [sentence + '.' for sentence in raw.split('[\.\n]') if 'freedom' in sentence]
# for sentence in related_sentence:
#     print sentence.strip();