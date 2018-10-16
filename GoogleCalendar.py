from GoogleCalendarConnection import GoogleCalendarConnection

class GoogleCalendar:
    def __init__(self, googleCalendarConnection, calendarName):
        self.googleCalendarConnection = googleCalendarConnection
        self.calendarName = calendarName
        
    def addAllDayEvent(self, eventSummary, eventDescription, eventDate):
        event = {
          'summary': eventSummary,
          'description': eventDescription,
          'start': {
            'date': eventDate
          },
          'end': {
            'date': eventDate
          },
        }    

        events_result = self.googleCalendarConnection.service.events().insert(
            calendarId=self.calendarName, body=event).execute()
        
        return events_result['id']
    