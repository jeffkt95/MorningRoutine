from tkinter import *
from Calendar import Calendar
import Utilities
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import webbrowser
from ToolTip import ToolTip
from HewWebsite import HewWebsite
import subprocess

class MorningRoutineUi():
    APPLICATION_NAME = "Morning Routine"
    totalGridWidth = 2

    def __init__(self, master, fitnessCalendar, studyCalendar, sitesToOpenProcessor):
        self.master = master
        self.fitnessCalendar = fitnessCalendar
        self.studyCalendar = studyCalendar
        self.sitesToOpenProcessor = sitesToOpenProcessor
        
        self.master.title(self.APPLICATION_NAME)
        frame = Frame(master)
        frame.pack()
        
        #Variable to easily change default status of all check boxes. Useful for debugging.
        defaultCheckBoxStatus = 1
        
        currentRow = 0

        #Row 1
        #checkbox with label
        self.logExerciseChecked = IntVar(value=defaultCheckBoxStatus)
        logExerciseCheckbox = Checkbutton(frame, text="Log exercise in Google calendar for", variable=self.logExerciseChecked)
        logExerciseCheckbox.grid(row=currentRow, column=0, sticky="w")
        #Date chooser
        self.exerciseDateVariable = StringVar()
        logExerciseDate = Button(frame, textvariable=self.exerciseDateVariable, command=lambda: self.selectDate("exercise"))
        self.exerciseDateVariable.set(Utilities.getTodaysDateAsStr())
        logExerciseDate.grid(row=currentRow, column=1, sticky="w")
        
        #Row 2
        currentRow = currentRow + 1
        #Exercise label
        exerciseLabel = Label(frame, text="Exercise")
        exerciseLabel.grid(row=currentRow, column=0, sticky="w")
        
        #Row 3
        currentRow = currentRow + 1
        #Exercise text field, multi-line, row span 3
        self.exerciseText = ScrolledText(frame, width=55, height=5)
        self.exerciseText.grid(row=currentRow, column=0, rowspan=3, columnspan=2, sticky="w")
        toolTipText = ("First line will be the event summary.\n" +
            "Subsequent lines will be the event description.\n" + 
            "Add multiple events by putting a ';;' on its own line between them.")
        exerciseTextTooltip = ToolTip(self.exerciseText, toolTipText)
        #HEW wod button
        #hewWodButton = Button(frame, text="Get WOD from HEW website", command=self.getWorkoutFromHew)
        #hewWodButton.grid(row=currentRow, column=2, columnspan=2, sticky="nw")
        
        #Row 4, column 2
        currentRow = currentRow + 1
        #Runkeeper button
        #runkeeperButton = Button(frame, text="Get from Runkeeper")
        #runkeeperButton.grid(row=currentRow, column=2, columnspan=2, sticky="nw")
        
        #Row 5, column 2
        currentRow = currentRow + 1
        #MyFitnessPal button
        #mfpButton = Button(frame, text="Get from MyFitnessPal")
        #mfpButton.grid(row=currentRow, column=2, columnspan=2, sticky="nw")
        
        #Row 6
        currentRow = currentRow + 1
        #checkbox with label
        self.logStudyChecked = IntVar(value=defaultCheckBoxStatus)
        logStudyCheckbox = Checkbutton(frame, text="Log study in Google calendar for", variable=self.logStudyChecked)
        logStudyCheckbox.grid(row=currentRow, column=0, sticky="w")
        #Date chooser
        self.studyDateVariable = StringVar()
        self.logStudyDate = Button(frame, textvariable=self.studyDateVariable, command=lambda: self.selectDate("study"))
        self.studyDateVariable.set(Utilities.getYesterdaysDateAsStr())
        self.logStudyDate.grid(row=currentRow, column=1, sticky="w")
        
        #Row 7
        currentRow = currentRow + 1
        #Study label
        studyLabel = Label(frame, text="Study")
        studyLabel.grid(row=currentRow, column=0, sticky="w")
        
        #Row 8
        currentRow = currentRow + 1
        #Study text field, multi-line
        self.studyText = ScrolledText(frame, width=55, height=5)
        self.studyText.grid(row=currentRow, column=0, columnspan=2, sticky="w")
        studyTextTooltip = ToolTip(self.studyText, toolTipText)
        
        #Row 9
        currentRow = currentRow + 1
        #Study label
        sitesToOpenLabel = Label(frame, text="Sites to open")
        sitesToOpenLabel.grid(row=currentRow, column=0, sticky="w")
        
        #Row 10
        currentRow = currentRow + 1
        #Sites to open text field, multi-line
        self.sitesToOpenText = ScrolledText(frame, width=55, height=21)
        self.sitesToOpenText.grid(row=currentRow, column=0, columnspan=2, sticky="w")
        self.sitesToOpenText.insert(END, self.sitesToOpenProcessor.getFileContent())
        toolTipText = ("List URLs for sites to open.\n" +
            "Comment out a line with #.\n" + 
            "Changes are auto-saved.")
        sitesToOpenTextTooltip = ToolTip(self.sitesToOpenText, toolTipText)
        
        #Row 11
        currentRow = currentRow + 1
        self.launchAllAccountsUpdate = IntVar(value=defaultCheckBoxStatus)
        launchAllAccountsUpdateCheckbox = Checkbutton(frame, text="Launch AllAccountsUpdate script", variable=self.launchAllAccountsUpdate)
        launchAllAccountsUpdateCheckbox.grid(row=currentRow, column=0, sticky="w")
        
        #Log and close button
        currentRow = currentRow + 1
        logAndCloseButton = Button(frame, text="Log and close", command=self.logAndCloseButtonAction)
        logAndCloseButton.grid(row=currentRow, column=0, sticky="w")
        #cancel button
        cancelButton = Button(frame, text="Cancel", command=self.cancelButtonAction)
        cancelButton.grid(row=currentRow, column=1, sticky="e")
        
    def cancelButtonAction(self):
        #Even though you cancelled, save changes to sitesToOpenText
        textFromTextField = self.sitesToOpenText.get("1.0", 'end-1c')
        self.sitesToOpenProcessor.writeFileContent(textFromTextField)
        self.master.destroy()

    def addEventsToCalendar(self, calendar, textFromTextField, date):
        eventsArray = Utilities.getTitleDescriptionArray(textFromTextField)
        
        for event in eventsArray:
            if (len(event) > 0):
                title = event[0]
                if (len(event) > 1):
                    description = event[1]
                else:
                    description = ""
                calendar.addAllDayEvent(title, description, date)
        
        
    def logAndCloseButtonAction(self):
        if (self.logExerciseChecked.get() == 1):
            textFromTextField = self.exerciseText.get("1.0", 'end-1c')
            dateOfEvents = Utilities.convertToGoogleDateFormat(self.exerciseDateVariable.get())
            self.addEventsToCalendar(self.fitnessCalendar, textFromTextField, dateOfEvents)
        
        if (self.logStudyChecked.get() == 1):
            textFromTextField = self.studyText.get("1.0", 'end-1c')
            dateOfEvents = Utilities.convertToGoogleDateFormat(self.studyDateVariable.get())
            self.addEventsToCalendar(self.studyCalendar, textFromTextField, dateOfEvents)
                
        if (self.launchAllAccountsUpdate.get() == 1):
            subprocess.Popen("python main.py", cwd="C:/mydata/20_personal/AllMoneySpreadsheetAutomation/AllMoneySpreadsheetAutomation", shell=True)
        
        textFromTextField = self.sitesToOpenText.get("1.0", 'end-1c')
        self.sitesToOpenProcessor.openSites(textFromTextField)
        
        self.sitesToOpenProcessor.writeFileContent(textFromTextField)
        
        self.master.destroy()

    def getWorkoutFromHew(self):
        workoutDate = Utilities.convertToGoogleDateFormat(self.exerciseDateVariable.get())
        hewWebsite = HewWebsite(workoutDate)
        self.exerciseText.insert(END, hewWebsite.getWodAsString())
    
    def selectDate(self, whichButton):
        if(whichButton == "exercise"):
            calendar = Calendar(tk.Toplevel(), self.setExerciseDate)
        elif(whichButton == "study"):
            calendar = Calendar(tk.Toplevel(), self.setStudyDate)
    
    def setExerciseDate(self, date):
        self.exerciseDateVariable.set(str(date['month_selected']) + "/" + str(date['day_selected']) + "/" + str(date['year_selected']))
    
    def setStudyDate(self, date):
        self.studyDateVariable.set(str(date['month_selected']) + "/" + str(date['day_selected']) + "/" + str(date['year_selected']))
    
    def closeWindow(self):
        self.master.destroy()
