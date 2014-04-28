import SummarizedCore

class Summary():
    def simpleSummary(self,googleResult,key):
        ss = SummarizedCore.SimpleSummarizer()
        temp = ss.getSummarized(googleResult,key) 
        result = ""
        try:
            for line in temp.split("."):
                if not line.strip():
                    continue
                result = result +" "+ line
        except:
            pass
        
        return result