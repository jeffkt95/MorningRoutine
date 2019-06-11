from GoogleCalendarConnection import GoogleCalendarConnection
import Utilities

class GoogleCalendar:
    def __init__(self, googleCalendarConnection, calendarName):
        self.googleCalendarConnection = googleCalendarConnection
        self.calendarName = calendarName
        
    def addAllDayEvent(self, eventSummary, eventDescription, eventDate):
        #For all day events, Google prefers to have the end date be the day after the start date. In other words,
        #the end date is exclusive.
        dayAfterEventDate = Utilities.getNextDateFromGoogleDate(eventDate)
        event = {
          'summary': eventSummary,
          'description': eventDescription,
          'start': {
            'date': eventDate
          },
          'end': {
            'date': dayAfterEventDate
          },
        }    

        events_result = self.googleCalendarConnection.service.events().insert(
            calendarId=self.calendarName, body=event).execute()
        
        return events_result['id']
    