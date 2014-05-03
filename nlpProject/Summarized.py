import nltk
import operator
from nltk.tokenize import RegexpTokenizer
from WordProcess import WordProcess

class Summary():
    def __init__(self):
        self.__document = ""
        self.__dic = {}
        self.__area = ""
        self.__input = ""
        self.__weight = {}
        self.__sent = {}
        self.__docLen = 0
        self.__result = []
        self.__tfWordCount = {}
        self.process = WordProcess()
        
    def cleanContain(self):
        self.__document = ""
        self.__dic = {}
        self.__area = ""
        self.__input = ""
        self.__weight = {}
        self.__sent = {}
        self.__tfWordCount ={}
        self.docLen = 0
        self.__result = []
        self.process = WordProcess()
            
    def tfCount(self):
        for word in self.__document.split(None):
            word = self.process.processWord(word)
            if word not in self.__tfWordCount.iterkeys():
                self.__tfWordCount[word] = 1
            else:
                self.__tfWordCount[word] += 1
    
                
    def sentenceWeight(self):
        upperband = 0
        lowerband = 0
        sentDetector = nltk.data.load('tokenizers/punkt/english.pickle')
        actualSentences = sentDetector.tokenize(self.__document)
        
        for sentence in actualSentences:
            counter = 0
            sumWeight = 0
            sentenceWeight  = 0
            idf = 0
            
            for word in sentence.split(None):
                word = self.process.processWord(word)
                weight = 0
                if word in self.__dic[self.__area]:
                    idf = self.__dic[self.__area][word]
                    if idf != 0:
                        # augmented frequency, too prevent a bias towards longer documents
                        tf = 0.5 + (0.5 * self.__tfWordCount[word] / self.__docLen)
                        weight = idf * tf
                        
                sumWeight += weight
                counter += 1
            if counter:
                sentenceWeight = sumWeight / counter
            if sentenceWeight > upperband:
                if len(self.__result) >= 1:
                    t = self.__result.pop(0)
                self.__result.append(sentence)
                upperband = sentenceWeight
            elif sentenceWeight < upperband and sentenceWeight  > lowerband:
                if len(self.__result) >=2:
                    self.__result.pop(1)
                self.__result.append(sentence)
                lowerband = sentenceWeight
                
            
    def simpleSummary(self,googleResult,userInput,dic,area,num = 2):
        self.cleanContain()
        
        self.__document = googleResult
        self.__dic = dic
        self.__area = area
        self.__input = userInput
        self.__docLen = len(self.__document.split(None)) * 1.0 
        
        self.tfCount()
        self.sentenceWeight()
        
        tempResult = ""
        result = ""
        for sentence in self.__result :
            print sentence
            tempResult += sentence+" "
        if tempResult.split(None) > 23:
            for word in tempResult.split(None)[0:22]:
                result += word+" "
        else:
            result  = tempResult          
        return result 