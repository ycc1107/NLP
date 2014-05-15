from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import nltk

class QueryExpansionProcess():
    def preExpand(self,word):
        word = nltk.word_tokenize(word)
        tagged = nltk.pos_tag(word)[0][1]
        if tagged == "VB":
            result  = wn.VERB
        elif tagged == "RB":
            result  = wn.ADJ
        elif tagged == "JJ":
            result  = wn.ADV
        else :
            result  = wn.NOUN
        return result
        
    def expand(self,query):
        result = ""
        for word in query.split(None):
            result = result + word + " "
            key = self.preExpand(word)
            if word.lower() not in stopwords.words(): 
                datas = wn.synsets(word,pos= key)
                for data in datas:
                    stripedWord = str(data).split('.')[0].split("'")[1]
                    if stripedWord == word:
                        continue
                    result = result + stripedWord + " "
        return (result)
