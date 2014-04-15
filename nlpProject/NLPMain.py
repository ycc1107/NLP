import urllib2
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


class TaggingInput():
    def tagging(self,tokenized):
        try:
            #cfd = ConditionalFreqDist()
            countTable = {}
            for sent in brown.tagged_sents():
                for word, tag in sent:
                    for tok in tokenized:
                        if word == tok:
                            cfd[tok].inc(tag)  
            cpd = ConditionalProbDist(cfd, MLEProbDist)
            tag = list()
            for i in range(0,len(tokenized)):
                tag.insert(tokenized[i],cpd[tokenized[i]].max())
            return tag
        except:
            return nltk.pos_tag(tokenized)
  
class InputClassifier():
    def __init__(self):
        f= open('my_classifier.pickle')
        self.__classifier = pickle.load(f)
        f.close()
    def classifier(self,userInput):
        tokenized = nltk.word_tokenize(userInput)  
        keyWord = ["adventure",
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
        print tokenized
        tagger = TaggingInput()
        tag = tagger.tagging(tokenized)
        print tag
        #for i in range(0,len(keyWord)):
            #print keyWord[i]
        #    categoryContent = brown.words(categories = keyWord[i])
            #print nltk.FreqDist(categoryContent)
            
        #    for w in categoryContent:
        #        if w.lower() in tokenized:
        #            cfdist[keyWord[i]].inc(w.lower())
       # print cfdist.conditions()[1]            
       # for i in range(0,len(cfdist)):
       #     print cfdist[i].freq("real")
            
            #fdist = FreqDist([w.lower() for w in categoryContent if w.lower() in tokenized])
            #print keyWord[i] , fdist

        pass
class HTMLClean():
    def clean(self,url):
        try:
            page = urllib2.urlopen(url).read()
        except:
            print "error"
            return ""
        soup = BeautifulSoup(page)
        print soup.find_all("title")
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
        return taggedText

class Summery():
    def simpleSummery(self,userInput,key):
        ss = summarize.SimpleSummarizer()
        return ss.summarize(userInput,key)
        

class WebSearch():
    def search(self,userInput):
        try:
            page = 0
            results = []
            gs = GoogleSearch(userInput)
            gs.results_per_page = 25
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
        
        #for token in tokenized:
        #    print ("This is a token : %s" %token)      
        #    print   
         
        googleRes = WebSearch()
        results = googleRes.search(userInput)  
        length = len(results)
        if len(results) > 20:
            length = 20 
            cleanPage = HTMLClean()
            #print cleanPage.clean(results[0].url.encode('utf8'))
            for res in results[0:length]:
                print res.url.encode('utf8')
                print (cleanPage.clean(res.url.encode('utf8')))    
                print    

def main():
    test = UserInput()
    test.result("i eat sushi with tuna")
    print "done"
    

if __name__=="__main__":
    main()


    
