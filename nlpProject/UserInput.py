import nltk
from HTMLClean import Clean
from xgoogle.search import GoogleSearch,SearchError
from Summarized import Summary

class WebSearch():
    #TODO : findout why there is a limited number of search 
    def search(self,userInput):
        try:
            page = 0
            results = []
            gs = GoogleSearch(userInput)
            gs.results_per_page = 50
            while page <=10:
                gs.page = page
                results += gs.get_results()
                page += 1
        except SearchError,e:
            print ("seach failed :%s" %e)
        return results
    
class UserInput():
    def result(self,userInput):
        userInput = str(userInput)
        classified = InputClassifier()
        classified.classifier(userInput) 
         
        googleRes = WebSearch()
        results = googleRes.search(userInput)  
        length = len(results)
        if len(results) > 20:
            length = 20 
            cleanPage = Clean()
            summ = Summary()
            for res in results[0:length]:
                print res.url.encode('utf8')
                print summ.simpleSummary(cleanPage.cleanHTML(res.url.encode('utf8')), 4) 
                #print cleanPage.clean(res.url.encode('utf8'))
                print    
                
class InputClassifier():
    def __init__(self):
        #f= open('my_classifier.pickle')
        #self.__classifier = pickle.load(f)
        #f.close()
        self.__keyWord = ["adventure",
                   "belles_lettres",  
                   "editorial",
                   "fiction",
                   "government",
                   "hobbies",
                   "humor",
                   "learned",
                   "lore",
                   "mystery",
                   "news",
                   "religion",
                   "reviews",
                   "romance",
                   "science_fiction"]
    def tagging(self,tokenized):
        return nltk.pos_tag(tokenized)    
    def classifier(self,userInput):
        tokenized = nltk.word_tokenize(userInput)  
        print tokenized
        tag = self.tagging(tokenized)
        print tag
        #for i in range(0,len(keyWord)):
            #print keyWord[i]
        #    categoryContent = brown.words(categories = self.__keyWord[i])
            #print nltk.FreqDist(categoryContent)
            
        #    for w in categoryContent:
        #        if w.lower() in tokenized:
        #            cfdist[self.__keyWord[i]].inc(w.lower())
       # print cfdist.conditions()[1]            
       # for i in range(0,len(cfdist)):
       #     print cfdist[i].freq("real")
            
            #fdist = FreqDist([w.lower() for w in categoryContent if w.lower() in tokenized])
            #print keyWord[i] , fdist
        pass