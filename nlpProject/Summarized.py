import SummarizedCore

class Summary():
    def simpleSummary(self,userInput,key):
        ss = SummarizedCore.SimpleSummarizer()
        temp = ss.getSummarized(userInput,key) 
        result = ""
        for line in temp.split("."):
            if not line.strip():
                continue
            result = result +" "+ line
        return result