import webbrowser

class SitesToOpenProcessor:
    def __init__(self):
        self.filename = "UrlList.txt"

    def getFileContent(self):
        urlListFile = open(self.filename, "r")
        content = urlListFile.read()
        urlListFile.close()
        return content
        
    def writeFileContent(self, fileContent):
        urlListFile = open(self.filename, "w+")
        urlListFile.write(fileContent)
        urlListFile.close()
    
    def openSites(self, sitesToOpenText):
        urlLines = sitesToOpenText.split('\n')
        for url in urlLines:
            #Remove leading and trailing whitespaces
            url = url.strip()
            
            if (url == ""):
                #Blank line. Skip it.
                continue
            
            if (url[:1] == "#"):
                #Commented out line. Skip it.
                continue

            #Ignore text following ' #'. So I can comment at the end of a line but still have the site opened. Useful for describing what a site is for.
            postUrlComment = url.find(" #")
            if (postUrlComment != -1):
                url = url[:postUrlComment]
                
            webbrowser.open(url)
