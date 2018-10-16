import unittest
from GoogleCalendarConnection import GoogleCalendarConnection
from GoogleCalendar import GoogleCalendar

class TestGoogleCalendar(unittest.TestCase):

    def setUp(self):
        googleCalendarConnection = GoogleCalendarConnection()
        self.googleCalendar = GoogleCalendar(googleCalendarConnection, "jeffkt95@gmail.com")
        
    def test_addAllDayEvent(self):
        eventId = self.googleCalendar.addAllDayEvent("Test Event Summary", "Test Event Description", "2018-11-02")
        pass
    
if (__name__) == "__main__":
    unittest.main()
    