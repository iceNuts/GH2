import nltk_process
import file_reader
import json

#raw = file_reader.read_file('../sample_data/I_have_a_dream.txt')
raw = file_reader.read_folder('../sample_data/test_articles')
wordList =  nltk_process.word_count(raw, "N");
print wordList
print json.dumps(nltk_process.build_similiarity_tree(wordList[3], wordList, 2));
#related_sentence = nltk_process.get_related_sentence("freedom", raw);
#for sentence in related_sentence:
#    print sentence.strip();
    
#nltk_process.get_relative_words("freedom", related_sentence[0])