from nltk.corpus import stopwords
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
def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)  

def load_obj(name):
    with open(name + '.pkl', 'r') as f:
        return pickle.load(f)
        
def getWordList(path,dataCounter):
    wordProcess = WordProcess()
    doc = open(path,"rb").read().split(None)     
    for word in doc: 
        word = wordProcess.processWord(word)
        print (word)
        if len(word) and len(word) < 50:
            with warnings.catch_warnings(record=True) as w:                
                if word.lower() not in stopwords.words():
                    if len(w):
                        print ("warning ! skip")
                        print (word)
                        continue  
                    dataCounter[word]  =""     
    return dataCounter

def tf_idf():
    myRootPath = "../TrainningData/"
    doucmentSize = 0
    globalWordList  = {}
    dataCounter = {}  #defaultdict(int)
    for (dirpath, dirnames, filenames) in walk("TrainningData/"):
        print (dirpath)
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
                        f = open(filePath).read().split(None)
                        doucmentSize = len(f)
                        print doucmentSize
                        for s in f:
                            if word == s:
                                counter += 1
                    if counter == 0:
                        continue
                    dataCounter[word] = 1.0*counter/ (1.0*doucmentSize)
                    counter = 0         
            globalWordList[dirname] = dataCounter
            dataCounter = {}    
            
    save_obj(globalWordList, "classiferSetV1" ) 

def main():
     
    #tf_idf()
    #print (elapsed)
    dic = load_obj("classiferSetV1")
    print(dic["globalWarmming"]["store"])
    
    print ("done")
            
if __name__ =="__main__":
    main()