import urllib.request
from bs4 import BeautifulSoup
from HewWorkout import HewWorkout
import Utilities

class HewWebsite:
    baseUrl = "https://hardexerciseworks.com/yourworkout/"
    
    def __init__(self, dateStr):
        urlDate = Utilities.convertGoogleDateToHewUrlDate(dateStr)
        urlWithDate = self.baseUrl + urlDate
    
        with urllib.request.urlopen(urlWithDate) as response:
            html = response.read()
            
        soup = BeautifulSoup(html, features="lxml")
        divElements = soup.findAll('div', 'sqs-block html-block sqs-block-html')

        #TODO: check that you have at least one
        soup = BeautifulSoup(str(divElements[0]), features="lxml")
        
        workoutElements = soup.findAll("div", "sqs-block-content")

        self.workout = HewWorkout(dateStr, workoutElements[0])
     
    def getWodAsString(self):
        str = "CrossFit"
        str = str + "\n" + self.workout.getTitle()
        str = str + "\n" + self.workout.getDescription()
        
        return str
    
def main():
    hewWebsite = HewWebsite("2019-04-11")
    print(hewWebsite.getWodAsString())

    hewWebsite = HewWebsite("2019-04-09")
    print(hewWebsite.getWodAsString())
    
if __name__ == "__main__":
    main()
    
    