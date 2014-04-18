import summarize

class Summary():
    def simpleSummary(self,userInput,key):
        ss = summarize.SimpleSummarizer()
        temp = ss.summarize(userInput,key) 
        result = ""
        for line in temp.split("."):
            if not line.strip():
                continue
            result = result +" "+ line
        return result