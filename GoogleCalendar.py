
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
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        today = int(str(datetime.date.today())[8:10])
        tomorrow = int(str(datetime.date.today() + datetime.timedelta(1))[8:10])
        todayEvents = 0
        tomorrowEvents = 0
        if not events:
            kyleEvents += 'No upcoming events found.\n'
        for event in events:
            if find_date(today, event['start'].get('dateTime', event['start'].get('date'))) and todayEvents < 5:
                if todayEvents == 0:
                    kyleEvents += "Today:\n\n"
                # print(event['start'].get('dateTime', event['start'].get('date')))
                start = parse_event(event['start'].get('dateTime', event['start'].get('date')))
                end = parse_event(event['end'].get('dateTime', event['start'].get('date')))
                kyleEvents += (start + " - " + end + "\n" + event['summary'] + "\n\n") # (start + " " + event['summary']+ end + "\n")
                todayEvents += 1
            elif find_date(tomorrow, event['start'].get('dateTime', event['start'].get('date'))) and tomorrowEvents < 5:
                if tomorrowEvents == 0:
                    kyleEvents += "\nTomorrow:\n\n"
                # print(event['start'].get('dateTime', event['start'].get('date')))
                start = parse_event(event['start'].get('dateTime', event['start'].get('date')))
                end = parse_event(event['end'].get('dateTime', event['start'].get('date')))
                kyleEvents += (start + " - " + end + "\n" + event['summary'] + "\n\n") # (start + " " + event['summary']+ end + "\n")
                tomorrowEvents += 1
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
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        today = int(str(datetime.date.today())[8:10])
        tomorrow = int(str(datetime.date.today() + datetime.timedelta(1))[8:10])
        todayEvents = 0
        tomorrowEvents = 0
        if not events:
            seanEvents += 'No upcoming events found.\n'
        for event in events:
            if find_date(today, event['start'].get('dateTime', event['start'].get('date'))) and todayEvents < 5:
                if todayEvents == 0:
                    seanEvents += "Today:\n\n"
                # print(event['start'].get('dateTime', event['start'].get('date')))
                start = parse_event(event['start'].get('dateTime', event['start'].get('date')))
                end = parse_event(event['end'].get('dateTime', event['start'].get('date')))
                seanEvents += (start + " - " + end + "\n" + event['summary'] + "\n\n") # (start + " " + event['summary']+ end + "\n")
                todayEvents += 1
            elif find_date(tomorrow, event['start'].get('dateTime', event['start'].get('date'))) and tomorrowEvents < 5:
                if tomorrowEvents == 0:
                    seanEvents += "\nTomorrow:\n\n"
                # print(event['start'].get('dateTime', event['start'].get('date')))
                start = parse_event(event['start'].get('dateTime', event['start'].get('date')))
                end = parse_event(event['end'].get('dateTime', event['start'].get('date')))
                seanEvents += (start + " - " + end + "\n" + event['summary'] + "\n\n") # (start + " " + event['summary']+ end + "\n")
                tomorrowEvents += 1
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
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        today = int(str(datetime.date.today())[8:10])
        tomorrow = int(str(datetime.date.today() + datetime.timedelta(1))[8:10])
        todayEvents = 0
        tomorrowEvents = 0
        if not events:
            samEvents += 'No upcoming events found.\n'
        for event in events:
            if find_date(today, event['start'].get('dateTime', event['start'].get('date'))) and todayEvents < 5:
                if todayEvents == 0:
                    samEvents += "Today:\n\n"
                # print(event['start'].get('dateTime', event['start'].get('date')))
                start = parse_event(event['start'].get('dateTime', event['start'].get('date')))
                end = parse_event(event['end'].get('dateTime', event['start'].get('date')))
                samEvents += (start + " - " + end + "\n" + event[
                    'summary'] + "\n\n")  # (start + " " + event['summary']+ end + "\n")
                todayEvents += 1
            elif find_date(tomorrow, event['start'].get('dateTime', event['start'].get('date'))) and tomorrowEvents < 5:
                if tomorrowEvents == 0:
                    samEvents += "\nTomorrow:\n\n"
                # print(event['start'].get('dateTime', event['start'].get('date')))
                start = parse_event(event['start'].get('dateTime', event['start'].get('date')))
                end = parse_event(event['end'].get('dateTime', event['start'].get('date')))
                samEvents += (start + " - " + end + "\n" + event[
                    'summary'] + "\n\n")  # (start + " " + event['summary']+ end + "\n")
                tomorrowEvents += 1
        return samEvents

def parse_event(time):
    i = time.find("T")
    out = time[i + 1:i + 6]
    hour = int(out[0:2])
    if hour > 12:
        out = str(hour - 12) + out[-3:] + " PM"
    else:
        out += " AM"
    return out

def find_date(day, time):
    if day == int(time[8:10]):
        return True
    return False


    ##print (kyleEvents + seanEvents + samEvents)
if __name__ == '__Get_Google_Calendar__':
    Get_Google_Calendar()
