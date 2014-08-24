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

def combine_json(target, src1, src2):
    new_dic = {}
    outf = open(target, 'w');
    dic1 = file_reader.read_json(src1);
    dic2 = file_reader.read_json(src2);
    count1 = dic1['count']['numbers']
    count2 = dic2['count']['numbers']
    
    new_count = []
    count1_new = count1[:]
    count2_new = count2[:]
    for word1 in count1:
        for word2 in count2:
            if word1['word'] == word2['word']:
                new_count.append({'word': word1['word'], 'count': word1['count'] + word2['count']})
                count1_new.remove(word1);
                count2_new.remove(word2);
    new_count += count1_new + count2_new
    
    new_dic['count'] = {'numbers': new_count}
    new_dic['tree'] = dic1['tree']
    new_dic['chain'] = dic1['chain']
    outf.write(json.dumps(new_dic))
    
#write_to_file('old_man', '4.json')
#print "Write finished"

#raw = file_reader.read_folder('../sample_data/test_articles')
#wordList = nltk_process.word_count(raw, "N");
#print nltk_process.word_count_in_json(raw, "N");
#print json.dumps(nltk_process.build_similiarity_tree(wordList[3], wordList, 2));
#related_sentence = nltk_process.get_related_sentence("freedom", raw);
#for sentence in related_sentence:
#    print sentence.strip();
    
#nltk_process.get_relative_words("freedom", related_sentence[0])


#print nltk_process.build_relative_tree("freedom", raw)
