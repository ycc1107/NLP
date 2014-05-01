import nltk
import pickle
import time
from QueryExpansion import QueryExpansion
from HTMLClean import Clean
from Search import Search
from Summarized import Summary
    
class UserInput():
    def result(self,userInput):
        userInput = str(userInput)
        #userInput = self.tagging(userInput)
        
        
        googleRes = Search()
        cleanPage = Clean()
        summ = Summary()
        query = QueryExpansion()
        idf = self.loadSet("trainedSetV1")  

        area = query.expand(userInput) 
        results = googleRes.googleAPICall(userInput)  
        # Only return 20 results
        length = len(results)
        if len(results) > 20:
            length = 20
            
        for res in results[0:length]:
            document  = cleanPage.cleanHTML(res)
            print res
            start = time.clock()
            print summ.simpleSummary(document,userInput,idf,area,2)    
            elapsed = (time.clock() - start)    
            print (elapsed)
            print   
            
    def tagging(self,tokenized):
        return nltk.pos_tag(tokenized) 
    
    def loadSet(self,name):
        with open( name + '.pkl', 'r') as f:
            return pickle.load(f)
           
   
