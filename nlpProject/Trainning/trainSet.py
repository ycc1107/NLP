from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from os import walk
from WordProcess import WordProcess

import re
import warnings
import nltk
import math
import os
import pickle
import time

def is_binary(filename):
    with open(filename, 'rb') as f:
        for block in f:
            if '\0' in block:
                return True
    return False


def getWordList(path,dataCounter):
    #tokenizer = RegexpTokenizer('\w+')
    wordProcess = WordProcess()
    f = open(path,"rb").read()     
   
    doc = wordProcess.processWord(f)
    
    for word in doc: 
        if len(word) and len(word) < 50:
            with warnings.catch_warnings(record=True) as w:                
                if word.lower() not in stopwords.words():
                    if len(w):
                        print ("warning ! skip")
                        print (word)
                        continue  
                    dataCounter[word]  =""     
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
                    if not is_binary(filePath):
                        getWordList(filePath,dataCounter)
                                    
                for (word,value) in dataCounter.items():
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
    
    start = time.clock()
    #tf_idf()
    elapsed = (time.clock() - start)
    #print (elapsed)
    dic = load_obj("trainedSetV1")

    print(dic["globalWarmming"]["Atmospheric"])

            
if __name__ =="__main__":
    main()