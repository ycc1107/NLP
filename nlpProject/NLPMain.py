import urllib2
import re
import nltk
import summarize
import pickle
from types import *
from bs4 import BeautifulSoup
from nltk.corpus import brown
from nltk.probability import *
from nltk import ConditionalFreqDist
from nltk.tag import UnigramTagger
from xgoogle.search import GoogleSearch,SearchError
from nltk.tag.brill import SymmetricProximateTokensTemplate, ProximateTokensTemplate
from nltk.tag.brill import ProximateTagsRule, ProximateWordsRule, FastBrillTaggerTrainer
    
class TrainningMode():
    def train(self):
        pass

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

# clean and find the contain in html code    
class HTMLClean():
    def clean(self,url):
        try:
            page = urllib2.urlopen(url).read()
        except:
            print "error"
            return ""
        soup = BeautifulSoup(page)
        temp = soup.find_all("title")
        for s in temp:
            print s.getText().strip()
            
        keyWord = {"p","b"}
        text = ""
        contain = ""
        for key in keyWord:
            contain = soup.find_all(key)
            if len(contain) > 0:
                break
        for s in contain:
            text = text + s.getText().strip()
            
        #tokenizedText = nltk.word_tokenize(text)
        #taggedText = nltk.pos_tag(tokenizedText)
        return text



class Summary():
    def simpleSummary(self,userInput,key):
        ss = summarize.SimpleSummarizer()
        temp = ss.summarize(userInput,key) 
        result = ""
        for line in temp.split("."):
            if not line.strip():
                continue
            result = result +" "+ line
        return result
        
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
            cleanPage = HTMLClean()
            summ = Summary()
            for res in results[0:length]:
                print res.url.encode('utf8')
                print summ.simpleSummary(cleanPage.clean(res.url.encode('utf8')), 2) 
                #print cleanPage.clean(res.url.encode('utf8'))
                print    

def main():
    test = UserInput()
    test.result("the born place of Mo ZeDong")
    print "done"
    

if __name__=="__main__":
    main()


    
