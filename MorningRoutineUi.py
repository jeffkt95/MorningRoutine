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
    GOOGLE_CALENDAR_URL = "https://calendar.google.com"
    DAILY_GOALS_URL = "https://docs.google.com/spreadsheets/d/1X8YEja5RX3p4y--ACK-iQaN2NpC9KrpiZg1QmS79WDY"
    totalGridWidth = 2

    def __init__(self, master, fitnessCalendar, studyCalendar):
        self.master = master
        self.fitnessCalendar = fitnessCalendar
        self.studyCalendar = studyCalendar
        
        self.master.title(self.APPLICATION_NAME)
        frame = Frame(master)
        frame.pack()
        
        currentRow = 0

        #Row 1
        #checkbox with label
        self.logExerciseChecked = IntVar(value=1)
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
        self.exerciseText = ScrolledText(frame, width=64, height=19)
        self.exerciseText.grid(row=currentRow, column=0, rowspan=3, columnspan=2, sticky="w")
        toolTipText = ("First line will be the event summary.\n" +
            "Subsequent lines will be the event description.\n" + 
            "Add multiple events by putting a ';;' on its own line between them.")
        exerciseTextTooltip = ToolTip(self.exerciseText, toolTipText)
        #HEW wod button
        hewWodButton = Button(frame, text="Get WOD from HEW website", command=self.getWorkoutFromHew)
        hewWodButton.grid(row=currentRow, column=2, columnspan=2, sticky="nw")
        
        #Row 4, column 2
        currentRow = currentRow + 1
        #Runkeeper button
        runkeeperButton = Button(frame, text="Get from Runkeeper")
        runkeeperButton.grid(row=currentRow, column=2, columnspan=2, sticky="nw")
        
        #Row 5, column 2
        currentRow = currentRow + 1
        #MyFitnessPal button
        mfpButton = Button(frame, text="Get from MyFitnessPal")
        mfpButton.grid(row=currentRow, column=2, columnspan=2, sticky="nw")
        
        #Row 6
        currentRow = currentRow + 1
        #checkbox with label
        self.logStudyChecked = IntVar(value=1)
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
        #Study text field, multi-line, row span 3
        self.studyText = ScrolledText(frame, width=64, height=19)
        self.studyText.grid(row=currentRow, column=0, columnspan=2, sticky="w")
        studyTextTooltip = ToolTip(self.studyText, toolTipText)
        
        #Row 9
        currentRow = currentRow + 1
        #Open calendar on log
        self.openCalendarChecked = IntVar(value=1)
        openCalendarCheckbox = Checkbutton(frame, text="Open calendar after log", variable=self.openCalendarChecked)
        openCalendarCheckbox.grid(row=currentRow, column=0, sticky="w")
        
        #Row 9, column 2
        #Open daily goals
        self.openDailyGoalsChecked = IntVar(value=1)
        openDailyGoalsCheckbox = Checkbutton(frame, text="Open daily goals", variable=self.openDailyGoalsChecked)
        openDailyGoalsCheckbox.grid(row=currentRow, column=1, sticky="w")
        
        #Row 10
        currentRow = currentRow + 1
        self.launchAllAccountsUpdate = IntVar(value=1)
        launchAllAccountsUpdateCheckbox = Checkbutton(frame, text="Launch AllAccountsUpdate script", variable=self.launchAllAccountsUpdate)
        launchAllAccountsUpdateCheckbox.grid(row=currentRow, column=0, sticky="w")
        
        #Log and close button
        currentRow = currentRow + 1
        logAndCloseButton = Button(frame, text="Log and close", command=self.logAndCloseButtonAction)
        logAndCloseButton.grid(row=currentRow, column=2, sticky="w")
        #cancel button
        cancelButton = Button(frame, text="Cancel", command=self.cancelButtonAction)
        cancelButton.grid(row=currentRow, column=3, sticky="w")
        
    def cancelButtonAction(self):
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
                
        if (self.openCalendarChecked.get() == 1):
            webbrowser.open(self.GOOGLE_CALENDAR_URL)
        
        if (self.openDailyGoalsChecked.get() == 1):
            webbrowser.open(self.DAILY_GOALS_URL)

        if (self.launchAllAccountsUpdate.get() == 1):
            subprocess.Popen("python main.py", cwd="C:/mydata/20_personal/AllMoneySpreadsheetAutomation/AllMoneySpreadsheetAutomation", shell=True)
        
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
