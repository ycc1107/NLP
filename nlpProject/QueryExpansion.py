import pickle
from random import randint

class QueryClassifier():
    def load_obj(self,name):
        with open(name + '.pkl', 'r') as f:
            return pickle.load(f)
        
    def expand(self,userInput):
        fate = randint(0,2) 
        answer = ["globalWarmming","Health","nlp"]
        globalWarmming = 1.0;
        Health = 1.0
        nlp = 1.0
        area = {}
        result = str(answer[fate])
        dic = self.load_obj("classiferSetV1")
          
        for word in userInput.split(None):
            if word in dic["globalWarmming"]:
                if isinstance(dic["globalWarmming"][word], (int, long, float, complex)):
                    globalWarmming = globalWarmming * dic["globalWarmming"][word]
            if word in dic["Health"]:
                if isinstance(dic["Health"][word], (int, long, float, complex)):
                    Health = Health * dic["Health"][word]               
            if word in dic["nlp"]:
                if isinstance(dic["nlp"][word], (int, long, float, complex)):
                    nlp = nlp * dic["nlp"][word]
        area["globalWarmming"] = globalWarmming
        area["Health"] = Health
        area["nlp"] = nlp
        max = 0.0
        
        for key,value in area.iteritems():
            print (key,value)
            if value > max and value != 1:
                max = value
                result  = key
                
        return (result)


