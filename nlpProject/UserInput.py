import nltk
import pickle
import time
from QueryExpansion import QueryClassifier
from HTMLClean import Clean
from Search import Search
from Summarized import Summary
from queryProcess import QueryExpansionProcess
from Answer import AnswerQuertion 

class UserInput():
    def result(self,userInput):
        result = []
        qna = ""
        userInput = str(userInput)        
        googleRes = Search()
        cleanPage = Clean()
        summ = Summary()
        query = QueryClassifier()
        queryExpand = QueryExpansionProcess()
        expandedQuery = queryExpand.expand(userInput)
        idf = self.loadSet("trainedSetV1")  
        answer = AnswerQuertion()
        area = query.expand(userInput) 
        results = googleRes.googleAPICall(userInput)  
        # Only return 20 results
        length = len(results)
        if len(results) > 20:
            length = 20
        
        for res in results[0:length]:
            document,title = cleanPage.cleanHTML(res)
            if answer.isWikipage(res,document):
               qna = answer.answer()
            result.append(title)
            result.append(res)
            result.append(summ.simpleSummary(document,userInput,idf,area,expandedQuery))
        return (result,qna)
            
              
            
    def tagging(self,tokenized):
        return nltk.pos_tag(tokenized) 
    
    def loadSet(self,name):
        with open( name + '.pkl', 'r') as f:
            return pickle.load(f)
           
   
