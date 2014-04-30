import nltk

class Summary():
    def __init__(self):
        self.__document = ""
        self.__dic = {}
        self.__area = ""
        self.__input = ""
        self.__weight = {}
        self.__sent = {}
        self.__maxReturen = 0
        self.result = []
        
    def tf(self,target):
        counter = 0

        for word in self.__document:
            if word == target:
                counter += 1
                
        return counter / len(self.__document)
    
    def tf_idf(self):  
        for word in self.__document:
            if word in self.__dic[self.__area] and word not in self.__weight.iterkeys():
                self.__weight[word] = self.__dic[self.__area][word]*self.tf(word)
    
    def sentenceWeight(self):
        sentDetector = nltk.data.load('tokenizers/punkt/english.pickle')
        actualSentences = sentDetector.tokenize(self.__document)
        workingSentences = [sentence.lower() for sentence in actualSentences]
        
        for sentence in workingSentences:
            counter = 0
            sumWeight = 0
            upper = 0
            lower = 0
            for word in sentence:
                sumWeight += self.__weight[word]
                counter += 1
            weight = sumWeight / counter
            if self.__maxReturen > 0:
                if weight > upper:
                    self.__sent[self.__maxReturen] = sentence
                    self.__maxReturen -= 1
                    upper = weight
                elif weight < upper and weight > lower:
                    self.__sent[self.__maxReturen] = sentence
                    self.__maxReturen -= 1
                    lower = weight
                    
        iterator  = range(0,len(self.__sent.itervalues()))                    
        for i in iterator:
            self.result[i] = self.__sent.itervalues()[i]
        
    def simpleSummary(self,googleResult,userInput,dic,area,num = 2):
        self.__document = googleResult
        self.__dic = dic
        self.__area = area
        self.__input = userInput
        self.__maxReturen = num
        print ("in the summarized")
        self.tf_idf()
        self.sentenceWeight()
        print ("out summarized")
        
        return self.result