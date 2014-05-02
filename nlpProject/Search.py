import urllib2
import urllib
import simplejson

class Search():
    def __init__(self):
        self.KEY = "AIzaSyC5WA2gfeLrJrXRvhDkaAuKHLGiPGSpuqY"
        self.CX = "015476964111987883949:xuenin0mbdu"
        self.result = []
        
    def googleAPICall(self,userInput):  
        try:  
            userInput = urllib.quote(userInput)        
            for i in range(0,1):
                index = i*10+1 
                url = ('https://www.googleapis.com/customsearch/v1?'    
                       'key=%s'
                       '&cx=%s'
                       '&alt=json'
                       '&num=10'
                       '&start=%d'
                       '&q=%s')%(self.KEY,self.CX,index,userInput)   
            
                request = urllib2.Request(url)
                response = urllib2.urlopen(request)
                returnResults = simplejson.load(response)
                webs = returnResults['items'] 
    
                for web in webs:
                    self.result.append(web["link"])
        except:
            print ("search error")
            self.result.append("http://en.wikipedia.org/wiki/Climate_change")
            
        return self.result
            
            
#   GOOGLE return dict names
#    kind
#    url
#    items
#    context
#    queries
#    searchInformation