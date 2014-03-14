#!/usr/bin/env python
from html import HTML_PAGE
import webapp2
import jinja2
import os
import re
import sys
from os import walk
from google.appengine.api import search
from google.appengine.ext import ndb
from urllib import urlopen
# global var

page = HTML_PAGE()
          
class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.out.write(template.render())
        self.response.out.write(page.pageChange())
        

class SearchFile():
    def __init__(self,userInput=''):
        self.__input = userInput
        self.__result = {}
        self.__files = []
        self.__filenames =[]
        for (dirpath, dirnames, filenames) in walk("dataFolder"):
            for name in filenames:
                path = dirpath+"/"+name
                self.__files.append(path)
                self.__filenames.append(name)
            break
    def outPutData(self):
        iterator = range(0,len(self.__filenames))
        for i in iterator:
            with open(self.__files[i]) as f:
                for line in f:
                    if self.__input in line:
                        self.__result[self.__filenames[i]] = line
                        break
            f.close()
        return self.__result  

  
class SearchFileHandle(webapp2.RequestHandler):
    def post(self):
        userInput = str(self.request.get('input'))
        self.response.out.write(page.pageChange(userInput))        
        
        search = SearchFile(userInput)
        tramText = CropText()
        
        for key,value in search.outPutData().iteritems():
            keyBold = "<b>%s</b><br>"%(key)
            keyLink = "<a href = \"dataFolder/%s\" name =\"%s\"> %s </a>"%(key,key,keyBold)
            self.response.out.write(keyLink)      
            #print >>sys.stderr, "====>", re.search(regex, value,re.IGNORECASE)
            resultContain = tramText.tram(value,userInput)
            for word in resultContain.split(" "):
                if word in userInput:
                    for keyWord in userInput.split(" "):
                        if word == keyWord:
                            self.response.out.write(" <b>%s</b> "%(word))
                else:
                    self.response.out.write(" %s "%(word))
            self.response.out.write("<br><br><br>")    
        news =  TakeNews()
        for key,value in news.websiteRead(userInput).iteritems():
            keyBold = "<b>%s</b><br>"%(key)
            keyLink = "<a href = %s> %s </a>"%(value,keyBold)
            self.response.out.write(keyLink)
            self.response.out.write("<br><br><br>")
    
    
class WordsProcess():
    def __init__(self,words):
        self.__token = []
        if len(words) > 0:
            for word in words:
                self.__token.append(word) 
        

class CropText():
    def tram(self,text,word):
        regex = r"( .*? )"+re.escape(word)+r"( .*?\.)"
        #print >>sys.stderr, text
        if re.search(regex,text,re.IGNORECASE):
            return re.search(regex,text,re.IGNORECASE).group()
        else:
            return ''
        
        
class TakeNews():
    def __init__(self):
        self.__website = 'http://www.bloomberg.com'
        self.__topNews =''
        self.__topNewsTitle =''
        
    
    def setWebsite(self,website):
        if (website[:10] != 'http://www') and not('http://www' in website):
            website = 'http://www' + website
        self.__website =  website

    
    def websiteRead(self,userInput):
        #website
        webpage = urlopen(self.__website).read()  
        #find where are bloomberg top news in the html
        pathFinderTopNewsTitle = re.compile('<a class=\"icon-article-headline\".*<span class=\'headline\'>(.*)</span>')
        pathFinderTopNews = re.compile('<a class=\"icon-article-headline\" data-id=.* data-type=.* href=\"(.*)\"><span class=\'headline\'>')
        #get the top news highlight
        #pathFinderTopNewsTitle = re.compile('<ul class=\"list01\">.*target=\"_blank\">(.*)</a> <a href.*')
        #pathFinderTopNews = re.compile()
        self.__topNewsTitle =  re.findall(pathFinderTopNewsTitle,webpage)
        self.__topNews = re.findall(pathFinderTopNews,webpage)
        result = {}
        iterator = range(0,len(self.__topNewsTitle))
        for i in iterator:
            if userInput in self.__topNews[i]:
                result[self.__topNewsTitle[i]] = self.__website+"/"+self.__topNews[i]
        return result
      
         
class ContainHandle(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('page.pageChange(ok)')      

                                    
def main():
    app.run()
    

app = webapp2.WSGIApplication([('/',MainPage),
                            ('/searchFile',SearchFileHandle),
                            ('/id',ContainHandle)],
                            debug =True)
                    
if __name__ == "__main__":
    main()







        

                                

