from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import nltk

class QueryExpansionProcess():
    def expand(self,query):
        result = ""
        for word in query.split(None):
            result = result + word + " "
            if word.lower() not in stopwords.words(): 
                datas = wn.synsets(word)
                for data in datas:
                    stripedWord = str(data).split('.')[0].split("'")[1]
                    if stripedWord == word:
                        continue
                    result = result + stripedWord + " "
        return (result)



