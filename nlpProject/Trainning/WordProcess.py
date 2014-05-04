from nltk.tokenize.punkt import PunktWordTokenizer
class WordProcess():
    def processWord(self,word):
        word = PunktWordTokenizer().tokenize(word)
        punctuations = '''()-[]{}:'"\.,<>/!?@#%^&*_~''' 
        doc = ""
        for char in word[0]:
            if char not in punctuations:
                doc = doc + char
        if len(doc):        
            doc = PunktWordTokenizer().tokenize(doc)[0]
        
        return doc