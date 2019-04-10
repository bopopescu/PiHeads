import GoogleCalendar as Cal

events = Cal.Get_Google_Calendar("Sean")
def FormatCal():

    #IMPORT AND SEPERATE
    i = 0
    NameFlag = False
    DateTime = ""
    EventName = ""
    for x in events:
        if events[i] is ' ':
            NameFlag = True

        if NameFlag is False:
            DateTime += events[i]

        if NameFlag is True:
            EventName = EventName + events[i]


    ##FORMAT DATE AND TIME
    print(EventName + DateTime)
