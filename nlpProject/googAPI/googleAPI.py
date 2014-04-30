import urllib2
import urllib
import simplejson
from bs4 import BeautifulSoup

def cleanHTML(self,url):
        try:
            page = urllib2.urlopen(url).read()
        except:
            pass
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

def googleAPICall():    
    userInput = urllib.quote("global warming")    
    KEY = "AIzaSyC5WA2gfeLrJrXRvhDkaAuKHLGiPGSpuqY"
    CX = "015476964111987883949:xuenin0mbdu"
    
    f = open("linkContain.txt","wb")
    
    for i in range(0,3):
        index = i*10+1 
        url = ('https://scholar.googleapis.com/customsearch/v1?'    
               'key=%s'
               '&cx=%s'
               '&alt=json'
               '&q=%s'
               '&num=10'
               '&start=%d')%(KEY,CX,userInput,index)
        #print(url)   
            
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        results = simplejson.load(response)
        webs = results['items']
    
        for web in webs:
            f.write(web["link"]+"\n")      
    f.close()
    print ("done")

def main():
        googleAPICall()
        
        f = open("linkContain.txt","rb")
        linkList = f.read()
        f.close()
        fileName = 1
        for link in linkList:   
            print (link)                                         
            text  = cleanHTML(link)
            name  = "../data/text"+fileName+".txt"
            fs = open(name,"wb")
            fs.write(text)
            fs.close()
            fileName += 1
          

        

    
    

if __name__=="__main__":
    main()
        
#    kind
#    url
#    items
#    context
#    queries
#    searchInformation