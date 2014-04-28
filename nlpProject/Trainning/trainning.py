from os import listdir
from os.path import isfile, join
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from os import walk

import nltk
import operator
import math
import os


def getWordList(path,dataCounter):
    tokenizer = RegexpTokenizer('\w+')
    f = open(path,"rb").read()        
    f = tokenizer.tokenize(f)
    for word in f:
        if word not in stopwords.words('english'):
            dataCounter[word]  =""     
    return dataCounter
            

def main():
    
    
    myRootPath = "../TranningData/"

    globalWordList  = {}
    dataCounter = {}  #defaultdict(int)
    
    a = 1
    
    for (dirpath, dirnames, filenames) in walk(myRootPath):
        for dirname in dirnames:
            path = os.path.join(dirpath, dirname)
            counter = 0
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
                    idf = math.log(docListLen/float(counter))
                    counter = 0
                    print( "looping : ", a)
                    a = a + 1
                    #print ("the word is :",word)
                    #print ("the idf value :",idf)
                    
                    dataCounter[word] = idf
                      
            globalWordList[dirname] = dataCounter
            dataCounter = {}    
   
    print(globalWordList["limited"])
        

                    #tfIdf(filePath)
            
    

if __name__ =="__main__":
    main()