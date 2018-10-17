from bs4 import BeautifulSoup
import html2text

class HewWorkout:
    def __init__(self, workoutElement):
        self.workoutElement = workoutElement

        soup = BeautifulSoup(str(self.workoutElement), features="lxml")
        
        
        #Looking for this: <span class="date">Oct-16-18</span>
        dateElement = soup.findAll('span', 'date')
        #Make sure you have one and only one
        if (len(dateElement) != 1):
            print("TODO: throw error. There are " + str(len(dateElement)) + " date elements. There should be 1.")
            return
        dateSoup = BeautifulSoup(str(dateElement), features="lxml")
        self.date = dateSoup.span.string
        
        #Looking for this: span class="day">ANNA</span>
        workoutTitleElement = soup.findAll('span', 'day')
        #Make sure you have one and only one
        if (len(workoutTitleElement) != 1):
            print("TODO: throw error. There are " + str(len(workoutTitleElement)) + " workout title elements. There should be 1.")
            return
        titleSoup = BeautifulSoup(str(workoutTitleElement), features="lxml")
        self.workoutTitle = titleSoup.span.string
        
        #Looking for this: <div class="row-fluid wrkout-text wod_scroll">
        workoutDescriptionElement = soup.findAll('div', 'row-fluid wrkout-text wod_scroll')
        #Make sure you have one and only one
        if (len(workoutDescriptionElement) != 1):
            print("TODO: throw error. There are " + str(len(workoutDescriptionElement)) + " workout description elements. There should be 1.")
            return
        descriptionSoup = BeautifulSoup(str(workoutDescriptionElement), features="lxml")

        #Take out the extra brackets and line feeds at the beginning and end of the description.
        html = str(descriptionSoup)
        self.workoutDescription = html2text.html2text(html)
        if (self.workoutDescription[0:3] == "[\n\n"):
            self.workoutDescription = self.workoutDescription[3:]
        if (self.workoutDescription[-4:] == "\n]\n\n"):
            self.workoutDescription = self.workoutDescription[:-4]
            
        
    def getDate(self):
        return self.date
        
    def getTitle(self):
        return self.workoutTitle

    def getDescription(self):
        return self.workoutDescription

