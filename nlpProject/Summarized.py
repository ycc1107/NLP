import nltk
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
        self.__maxReturen = 0
        self.docLen = 0
        self.result = ""
        self.process = WordProcess()
        
    def tf(self,target):
        counter = 0
        for word in self.__document.split(None):
            word = self.process.processWord(word)
            if word == target:
                counter += 1
    
        result = counter*1.0/self.docLen
        #print(result)                   
        return result 
         
    
    def tf_idf(self):  
        for word in self.__document.split(None):
            
            word = self.process.processWord(word)

            if not len(word):
                continue
            
            if word in self.__dic[self.__area]:
                if word not in self.__weight.keys():
                    idf = self.__dic[self.__area][word]
            else:
                idf = 0     
            self.__weight[word] = idf * self.tf(word)
                
    def sentenceWeight(self):
        sentDetector = nltk.data.load('tokenizers/punkt/english.pickle')
        actualSentences = sentDetector.tokenize(self.__document)
        #workingSentences = [sentence.lower() for sentence in actualSentences]

        for sentence in actualSentences:
            counter = 0
            sumWeight = 0
            weight  = 0
            upper = -1
            lower = -1
            
            for word in sentence.split(None):
                word = self.process.processWord(word)
                if not len(word):
                    continue
                try:
                    sumWeight += self.__weight[word]
                    counter += 1
                except:
                    continue
            if counter:
                weight = sumWeight / counter
                
            if self.__maxReturen > 0:
                if weight > upper:
                    self.__sent[self.__maxReturen] = sentence
                    self.__maxReturen -=  1
                    upper = weight
                elif weight < upper and weight > lower:
                    self.__sent[self.__maxReturen] = sentence
                    self.__maxReturen -= 1
                    lower = weight
                    
                
        for key,value in self.__sent.items():
            self.result += value
                        
        return self.result
            
    def simpleSummary(self,googleResult,userInput,dic,area,num = 2):
        self.__document = googleResult
        self.__dic = dic
        self.__area = area
        self.__input = userInput
        self.__maxReturen = num
        self.docLen = len(self.__document.split(None)) * 1.0 
        self.tf_idf()
        
        result = self.sentenceWeight()             
        return result 