from nltk.tokenize.punkt import PunktWordTokenizer
import unicodedata

class WordProcess():
    def processWord(self,word):
        word = PunktWordTokenizer().tokenize(word)
        punctuations = '''()-[]{}:'"\.,<>/!?@#%^&*_~''' 
        doc = ""
        for char in word:
            if char not in punctuations:
                    doc = doc + char
        doc = PunktWordTokenizer().tokenize(doc)
        doc = str(unicodedata.normalize('NFKD', word[0]).encode('ascii','ignore'))

        return doc