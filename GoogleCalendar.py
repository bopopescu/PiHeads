
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def Get_Google_Calendar(name):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 5 events on the user's calendar.
    """

    ##Kyle
    if name is "Kyle":
        kyleEvents = "Kyle's Calendar\n"

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.kyle'):
            with open('token.kyle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.kyle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        ##print('Getting the upcoming 5 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=5, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            kyleEvents += 'No upcoming events found.\n'
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            kyleEvents += (start + " " + event['summary'] + "\n")
        return kyleEvents


    ##Sean
    if name is "Sean":
        seanEvents = "\nSean's Calendar\n"

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.sean'):
            with open('token.sean', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.sean', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        ##print('Getting the upcoming 5 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=5, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            seanEvents += 'No upcoming events found.\n'
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            seanEvents += (start + " " + event['summary']+"\n")
        return seanEvents
    ##Sam
    if name is "Sam":
        samEvents = "\nSam's Calendar\n"

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.sam'):
            with open('token.sam', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.sam', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        ##print('Getting the upcoming 5 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=5, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            samEvents += 'No upcoming events found.\n'
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            samEvents += (start + " " + event['summary'] + "\n")
        return samEvents

    ##print (kyleEvents + seanEvents + samEvents)








if __name__ == '__main__':
    Get_Google_Calendar()