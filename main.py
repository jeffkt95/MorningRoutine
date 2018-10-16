import sys
from GoogleCalendarConnection import GoogleCalendarConnection
from GoogleCalendar import GoogleCalendar
from MorningRoutineUi import MorningRoutineUi
from tkinter import *

fitnessCalendarId = "mcgrt50kckuejks4b7eoqqpn40@group.calendar.google.com"
studyCalendarId = "7tl4cdst8krtam1lhj8tbuu51g@group.calendar.google.com"

def main():
    googCalConnection = GoogleCalendarConnection()
    mainCalendar = GoogleCalendar(googCalConnection, "jeffkt95@gmail.com")
    fitnessCalendar = GoogleCalendar(googCalConnection, fitnessCalendarId)
    studyCalendar = GoogleCalendar(googCalConnection, studyCalendarId)
    
    #eventId = mainCalendar.addAllDayEvent("Test Event Summary", "Test adsf Description", "2018-11-03")
    #eventId = fitnessCalendar.addAllDayEvent("Test to fitness", "Test aasq33asd  assdf  Description", "2018-11-03")
    #eventId = studyCalendar.addAllDayEvent("Test study", "Test aa a a a a Description", "2018-11-03")

    root = Tk()
    app = MorningRoutineUi(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
    
    