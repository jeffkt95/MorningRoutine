import urllib.request
from bs4 import BeautifulSoup
from HewWorkout import HewWorkout
import Utilities

class HewWebsite:
    URL = "https://hardexerciseworks.com/#wod"
    def __init__(self):
        with urllib.request.urlopen(self.URL) as response:
            html = response.read()
            
        soup = BeautifulSoup(html, features="lxml")
        divElements = soup.findAll('div', 'list_carousel hp-green')
        
        #TODO: check that you have at least one
        soup = BeautifulSoup(str(divElements[0]), features="lxml")
        
        workoutElements = soup.findAll("li", "item")
        
        self.workouts = []
        for workoutElement in workoutElements:
            hewWorkout = HewWorkout(workoutElement)
            self.workouts.append(hewWorkout)
 
    #Date str is expected to be in google api format, i.e. 2008-01-01
    def getWod(self, dateStr):
        hewFormattedDate = Utilities.convertGoogleDateToHewDate(dateStr)
        
        for workout in self.workouts:
            if (workout.getDate() == hewFormattedDate):
                print("Found workout for date " + hewFormattedDate + "! Workout title is " + workout.getTitle())
                return workout
    
        print("Unable to find workout for " + hewFormattedDate + ". Returning None.")
        return None
        
    def getWodAsString(self, dateStr):
        wod = self.getWod(dateStr)
        
        str = "CrossFit"
        str = str + "\n" + wod.getTitle()
        str = str + "\n" + wod.getDescription()
        
        return str
    
def main():
    hewWebsite = HewWebsite()
    
    wod = hewWebsite.getWod("2008-10-01")

    wod = hewWebsite.getWod("2018-10-16")
    print("Workout description is " + wod.getDescription())

    wod = hewWebsite.getWod("2018-10-15")
    print("Workout description is " + wod.getDescription())
    
if __name__ == "__main__":
    main()
    
    