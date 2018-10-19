import datetime
import calendar

def getTodaysDateAsStr():
    today = datetime.datetime.today()
    return str(today.month) + "/" + str(today.day) + "/" + str(today.year)

def getYesterdaysDateAsStr():
    yesterday = datetime.datetime.today() - datetime.timedelta(1)
    return str(yesterday.month) + "/" + str(yesterday.day) + "/" + str(yesterday.year)

#Converts from MM/DD/YYYY to YYYY-MM-DD. Required for google api call
#              0123456789
def convertToGoogleDateFormat(dateStr):
    firstBracketPos = dateStr.find('/')
    if (firstBracketPos == -1):
        return "ERROR"
        
    dayYear = dateStr[firstBracketPos+1:]
    secondBracketPos = dayYear.find('/')
    if (secondBracketPos == -1):
        return "ERROR"
        
    month = dateStr[0:firstBracketPos]
    day = dayYear[0:secondBracketPos]
    year = dayYear[secondBracketPos+1:]
    
    #If month and day are only one digit, prepend with 0
    if (len(month) == 1):
        month = "0" + month
    if (len(day) == 1):
        day = "0" + day
    
    return year + "-" + month + "-" + day
     
#Converts 2008-01-10 to Jan-10-08
#         0123456789
def convertGoogleDateToHewDate(dateStr):
     year = dateStr[2:4]
     month = dateStr[5:7]
     day = dateStr[8:]
     
     monthShort = calendar.month_abbr[int(month)]
     
     return monthShort + "-" + day + "-" + year

#Takes text field input and turns it into an array of events. Expects format:
#Event title 1
#Event 1 description line 1
#Event 1 description line 2
#;;
#Event title 2
#Event 2 description line 1
#Event 2 description line 2
#;;
#Event title 3
#Event 3 description line 1
#Event 3 description line 2
def getTitleDescriptionArray(str):
    events = str.split(";;")
    eventArray = []
    for event in events:
        #Remove any leading line feeds
        if (event[:1] == '\n'):
            event = event[1:]
            
        #Splits on the new line. First element is title, second is description
        newEvent = event.split('\n', 1)
        eventArray.append(newEvent)
        
    return eventArray
     

def main():
    print("Today's date is " + getTodaysDateAsStr())
    print("Yesterday's date is " + getYesterdaysDateAsStr())
    
    dateBefore = "10/1/2018"
    print("Date before conversion: " + dateBefore + ". Date after: " + convertToGoogleDateFormat(dateBefore))

    dateBefore = "2/1/2018"
    print("Date before conversion: " + dateBefore + ". Date after: " + convertToGoogleDateFormat(dateBefore))
    
    dateBefore = "12/12/2018"
    print("Date before conversion: " + dateBefore + ". Date after: " + convertToGoogleDateFormat(dateBefore))
    
    dateBefore = "1/28/2018"
    print("Date before conversion: " + dateBefore + ". Date after: " + convertToGoogleDateFormat(dateBefore))
    
    dateBefore = "Homer Simpson"
    print("Date before conversion: " + dateBefore + ". Date after: " + convertToGoogleDateFormat(dateBefore))

    dateBefore = "Homer/Simpson"
    print("Date before conversion: " + dateBefore + ". Date after: " + convertToGoogleDateFormat(dateBefore))
    
    googleDate = "2018-01-10"
    print("Date before google-to-Hew conversion: " + googleDate + ". Date after: " + convertGoogleDateToHewDate(googleDate))
    
    googleDate = "2008-12-12"
    print("Date before google-to-Hew conversion: " + googleDate + ". Date after: " + convertGoogleDateToHewDate(googleDate))
    
    googleDate = "2018-10-01"
    print("Date before google-to-Hew conversion: " + googleDate + ". Date after: " + convertGoogleDateToHewDate(googleDate))
    
    googleDate = "2018-05-05"
    print("Date before google-to-Hew conversion: " + googleDate + ". Date after: " + convertGoogleDateToHewDate(googleDate))
    
    events = (
        "Event title 1\n" + 
        "Event 1 description line 1\n" + 
        "Event 1 description line 2\n" + 
        ";;\n" + 
        "Event title 2\n" + 
        "Event 2 description line 1\n" + 
        "Event 2 description line 2\n" + 
        ";;\n" + 
        "Event title 3\n" + 
        "Event 3 description line 1\n" + 
        "Event 3 description line 2\n") 
    eventArray = getTitleDescriptionArray(events)
    print("Events input: " + events)
    print("Event array: " + str(eventArray))

    #Missing descriptions
    events = (
        "Event title 1\n" + 
        ";;\n" + 
        "Event title 2\n" + 
        ";;\n" + 
        "Event title 3\n" + 
        "Event 3 description line 2\n")
    eventArray = getTitleDescriptionArray(events)
    print("Events input: " + events)
    print("Event array: " + str(eventArray))

    #Just one event
    events = (
        "Event title 1\n" + 
        "Event 1 description line 1\n" + 
        "Event 1 description line 2")
    eventArray = getTitleDescriptionArray(events)
    print("Events input: " + events)
    print("Event array: " + str(eventArray))


if __name__ == "__main__":
    main()
    
    