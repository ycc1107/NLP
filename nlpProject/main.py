#!/usr/bin/env python

from html import HTML_PAGE
import webapp2
import jinja2
import os
import re
import sys
import urllib
import urllib2

from google.appengine.api import search
from xgoogle.search import GoogleSearch,SearchError

#from xgoogle.search import GoogleSearch, SearchError


page = HTML_PAGE()
          
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(page.pageChange())
        

class SearchFileHandle(webapp2.RequestHandler):
    def post(self):
        userInput = str(self.request.get('input'))
        self.response.out.write(page.pageChange(userInput))  
        googleRes = WebSearch()
        results = googleRes.search(userInput)
        
        length = len(results)
        if len(results) > 20:
            length = 20
        for res in results[0:length]:
            self.response.out.write("%s<br>%s<br>%s"%(res.title.encode('utf8'),res.desc.encode('utf8'),res.url.encode('utf8')))
            self.response.out.write("<br><br><br>")      
        
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
            self.response.out.write("seach failed :%s" %e)
        return results

# TODO
# use differet algorithm to classify the input
# 
class InputOptimal():  
    pass
    
    
# TODO
# summary the return result page
class resultSummary(): 
    pass   
      
    
    
    
    
                                    
def main():
    app.run()
    

app = webapp2.WSGIApplication([('/',MainPage),
                            ('/searchFile',SearchFileHandle)
                            ],
                            debug =True)
                    
if __name__ == "__main__":
    main()







        

                                

