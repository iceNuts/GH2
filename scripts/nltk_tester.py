import nltk_process
import file_reader
import json

def write_to_file(dataset, path):
    outf = open(path, 'w');
    outDic = {}
    raw = file_reader.read_folder('../sample_data/'+ dataset)
    wordList = nltk_process.word_count(raw, "N");
    
    outDic['count'] = nltk_process.hist_convert_to_dic(wordList)
    outDic['tree'] = nltk_process.build_similiarity_tree_all(wordList)
    outDic['chain'] = nltk_process.get_related_sentence_all(wordList, raw)
    outf.write(json.dumps(outDic))
    
write_to_file('old_man', '4.json')
print "Write finished"

#raw = file_reader.read_folder('../sample_data/test_articles')
#wordList = nltk_process.word_count(raw, "N");
#print nltk_process.word_count_in_json(raw, "N");
#print json.dumps(nltk_process.build_similiarity_tree(wordList[3], wordList, 2));
#related_sentence = nltk_process.get_related_sentence("freedom", raw);
#for sentence in related_sentence:
#    print sentence.strip();
    
#nltk_process.get_relative_words("freedom", related_sentence[0])


#print nltk_process.build_relative_tree("freedom", raw)
