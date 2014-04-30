import urllib2
import urllib
import simplejson

class Search():
    def __init__(self):
        self.KEY = "AIzaSyC5WA2gfeLrJrXRvhDkaAuKHLGiPGSpuqY"
        self.CX = "015476964111987883949:xuenin0mbdu"
        
    def googleAPICall(self,userInput):  
        try:  
            userInput = urllib.quote(userInput)        
            for i in range(0,2):
                index = i*10+1 
                url = ('https://scholar.googleapis.com/customsearch/v1?'    
                       'key=%s'
                       '&cx=%s'
                       '&alt=json'
                       '&q=%s'
                       '&num=10'
                       '&start=%d')%(self.KEY,self.CX,userInput,index)   
            
                request = urllib2.Request(url)
                response = urllib2.urlopen(request)
                returnResults = simplejson.load(response)
                webs = returnResults['items'] 
                result = ""
                for web in webs:
                    result += web["link"]+"\n"
        except:
            result = ""
            
        return result
            
            
#   GOOGLE return dict names
#    kind
#    url
#    items
#    context
#    queries
#    searchInformation