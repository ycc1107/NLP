from bs4 import BeautifulSoup
import urllib2

class Clean():
    def cleanHTML(self,url):
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