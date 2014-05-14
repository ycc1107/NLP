from bs4 import BeautifulSoup
import mechanize
import urllib2

class Clean():
    def cleanHTML(self,url):
        try:
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.addheaders = [("Uder-agent","Firefox")]
            page = br.open(url).read()
        except:
            return ("","")
        
        soup = BeautifulSoup(page)
        temp = soup.find_all("title")
        title = ""
        for s in temp:
            title = title + s.getText().strip()
            
        keyWord = {"p"}
        text = ""
        contain = ""
        for key in keyWord:
            contain = soup.find_all(key)
            if len(contain) > 0:
                break
        for s in contain:
            text = text + s.getText().strip()
            
        return (text,title)
