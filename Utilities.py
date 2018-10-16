import datetime

def getTodaysDateAsStr():
    today = datetime.datetime.today()
    return str(today.month) + "/" + str(today.day) + "/" + str(today.year)

def getYesterdaysDateAsStr():
    yesterday = datetime.datetime.today() - datetime.timedelta(1)
    return str(yesterday.month) + "/" + str(yesterday.day) + "/" + str(yesterday.year)

def main():
    print("Today's date is " + getTodaysDateAsStr())
    print("Yesterday's date is " + getYesterdaysDateAsStr())
    
    
if __name__ == "__main__":
    main()
    
    