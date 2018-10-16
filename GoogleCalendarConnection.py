from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

#Python calendar API: https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/
class GoogleCalendarConnection:

    def __init__(self):
        # Setup the Calendar API
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
            creds = tools.run_flow(flow, store)
        
        self.service = build('calendar', 'v3', http=creds.authorize(Http()))
