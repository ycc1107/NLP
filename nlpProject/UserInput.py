import nltk
import pickle
from QueryExpansion import QueryExpansion
from HTMLClean import Clean
from Search import Search
from Summarized import Summary
    
class UserInput():
    def result(self,userInput):
        userInput = str(userInput)
        userInput = self.tagging(userInput)
        
        try:
            googleRes = Search()
            cleanPage = Clean()
            summ = Summary()
            query = QueryExpansion()
            idf = self.LoadTrainedSet()  
        except:
            print "error"
            
        userInput = query.expand(userInput) 
        results = googleRes.search(userInput)  
        # Only return 20 results
        length = len(results)
        if len(results) > 20:
            length = 20    
       
        for res in results[0:length]:
            document  = cleanPage.cleanHTML(res)
            print res
            print summ.simpleSummary(document,userInput,idf,area,2) 
            print cleanPage.clean(res.url.encode('utf8'))
            print   
            
    def tagging(self,tokenized):
        return nltk.pos_tag(tokenized) 
    
    def loadSet(self,name):
        with open('../' + name + '.pkl', 'r') as f:
            return pickle.load(f)
           
   
