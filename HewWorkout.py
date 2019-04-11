from bs4 import BeautifulSoup
import html2text

class HewWorkout:
    def __init__(self, date, workoutElement):
        self.workoutElement = workoutElement
        self.date = date
        
        descriptionSoup = BeautifulSoup(str(workoutElement), features="lxml")

        html = str(descriptionSoup)       
        workoutText = html2text.html2text(html)

        firstLineAndRest = workoutText.split('\n', 1)
        
        self.workoutTitle = self.getTitleFromFirstLine(firstLineAndRest[0])
        #Replace extra line feeds
        self.workoutDescription = firstLineAndRest[1].replace('\n\n', '\n')
        
    #The title in the first line is formatted as '**Workout Title**'
    #This methods removes the prefix and suffix **
    def getTitleFromFirstLine(self, firstLine):
        workoutTitle = firstLine
        if (workoutTitle[0:2] == "**"):
            workoutTitle = workoutTitle[2:]
        if (workoutTitle[-2:] == "**"):
            workoutTitle = workoutTitle[:-2]
        
        return workoutTitle        
        
    def getDate(self):
        return self.date
        
    def getTitle(self):
        return self.workoutTitle

    def getDescription(self):
        return self.workoutDescription

