from tkinter import *
from Calendar import Calendar

import Utilities
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class MorningRoutineUi():
    APPLICATION_NAME = "Morning Routine"
    totalGridWidth = 2

    def __init__(self, master):
        self.master = master
        self.master.title(self.APPLICATION_NAME)

        frame = Frame(master)
        frame.pack()
        
        currentRow = 0
        
        #topLabel.grid(row=currentRow, column=0, columnspan=self.totalGridWidth)

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
        exerciseText = ScrolledText(frame, width=32, height=10)
        exerciseText.grid(row=currentRow, column=0, rowspan=3, columnspan=2, sticky="w")
        #HEW wod button
        hewWodButton = Button(frame, text="Get WOD from HEW website")
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
        studyText = ScrolledText(frame, width=32, height=10)
        studyText.grid(row=currentRow, column=0, columnspan=2, sticky="w")
        
        #Row 9
        currentRow = currentRow + 1
        #Log and close button
        logAndCloseButton = Button(frame, text="Log and close", command=self.logAndCloseButtonAction)
        logAndCloseButton.grid(row=currentRow, column=2, sticky="w")
        #cancel button
        cancelButton = Button(frame, text="Cancel", command=self.cancelButtonAction)
        cancelButton.grid(row=currentRow, column=3, sticky="w")
        
    def cancelButtonAction(self):
        self.master.destroy()

    def logAndCloseButtonAction(self):
        print("TODO: Log")
        self.master.destroy()

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
