from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from os import walk
import warnings
import nltk
import math
import os
import pickle


def getWordList(path,dataCounter):
    tokenizer = RegexpTokenizer('\w+')
    f = open(path,"rb").read().split(None) 
    for word in f:
        word = tokenizer.tokenize(word)
        if len(word) and len(word) < 2:
            #print (word[0])
            with warnings.catch_warnings(record=True) as w:                
                if word[0].lower() not in stopwords.words():
                    if len(w):
                        print ("warning ! skip")
                        print (word[0])
                        continue      
                    dataCounter[str(word[0])]  ="" 

        
    return dataCounter

def save_obj(obj, name ):
    with open('../'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)            

def load_obj(name):
    with open('../' + name + '.pkl', 'r') as f:
        return pickle.load(f)

def tf_idf():
    myRootPath = "../TranningData/"
    globalWordList  = {}
    dataCounter = {}  #defaultdict(int)

    for (dirpath, dirnames, filenames) in walk(myRootPath):
        for dirname in dirnames:
            path = os.path.join(dirpath, dirname)
            counter = 0
            print(dirname) 
            for (path, names, fileNames) in walk(path):
                docListLen = len(fileNames)
                for name in fileNames:
                    filePath = os.path.join(path, name)
                    getWordList(filePath,dataCounter)
                iterator = dataCounter.iteritems()
                
                for (word,value) in iterator:
                    for name in fileNames: 
                        filePath = os.path.join(path, name)
                        f = open(filePath).read()
                        if word in f:
                            counter += 1
                    if counter == 0:
                        continue
                    idf = math.log(docListLen/float(counter))
                    dataCounter[word] = idf
                    counter = 0         
            globalWordList[dirname] = dataCounter
            dataCounter = {}    
            
    save_obj(globalWordList, "trainedSetV1" ) 

def main(): 
    #tf_idf()
    dic = load_obj("trainedSetV1")

    print (dic["Health"]["brain"])

            
if __name__ =="__main__":
    main()