import SummarizedCore

class Summary():
    def __init__(self):
        self.__document = ""
        self.__dic = {}
        self.__area = ""
        self.__input = ""
        
    def tf(self,target):
        counter = 0
        
        for word in self.__document:
            if word == target:
                counter += 1
        return counter / len(self.__document)
            
        
        
        for word in self.__input:
            if word in self.__document:
                counter += 1
        return counter / len(self.__document)
        
    def simpleSummary(self,googleResult,userInput,dic,area,num):
        self.__document = googleResult
        self.__dic = dic
        self.__area = area
        self.__input = userInput
        
        for word in self.__document:
            if word in dic[self.__area]:
                dic[self.__area][word]*self.tf(word)
        
        
        return result