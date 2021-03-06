import sys
from GoogleCalendarConnection import GoogleCalendarConnection
from GoogleCalendar import GoogleCalendar
from MorningRoutineUi import MorningRoutineUi
from tkinter import *
from SitesToOpenProcessor import SitesToOpenProcessor

fitnessCalendarId = "mcgrt50kckuejks4b7eoqqpn40@group.calendar.google.com"
studyCalendarId = "7tl4cdst8krtam1lhj8tbuu51g@group.calendar.google.com"

def main():
    googCalConnection = GoogleCalendarConnection()
    mainCalendar = GoogleCalendar(googCalConnection, "jeffkt95@gmail.com")
    fitnessCalendar = GoogleCalendar(googCalConnection, fitnessCalendarId)
    studyCalendar = GoogleCalendar(googCalConnection, studyCalendarId)
    sitesToOpenProcessor = SitesToOpenProcessor()
    
    root = Tk()
    app = MorningRoutineUi(root, fitnessCalendar, studyCalendar, sitesToOpenProcessor)
    root.mainloop()
    
if __name__ == "__main__":
    main()
    
    