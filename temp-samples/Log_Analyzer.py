from ip2geotools.databases.noncommercial import DbIpCity
from datetime import datetime,timedelta
import csv

class Log_Analyzer:
    def convert_string_to_datetime(self, inputDateString):
        dateTimeObj = datetime.strptime(inputDateString, '%Y-%m-%d %H:%M:%S.%f')
        return dateTimeObj
    
    def print_report(self, inputIP, inputNumberOfHits):
        try:
            location = DbIpCity.get(inputIP, api_key='free')
        except:
            location = "private IP address"
        print(f'\n\n{inputNumberOfHits} failed attempts from location: {location}\n\n ----')

    def check_logs(self):

        timeArray = []
        ipArray = []
        previousTime = datetime.now()
        with open('logfile.csv', 'r', newline='\n') as logfile:
            #read log file
            reader = csv.reader(logfile, delimiter=',')
            for row in reader:
                timeArray.append(self.convert_string_to_datetime(row[1]))
                ipArray.append(row[0])

        #java style for loop
        numberOftimes = len(timeArray)
        counter = 1
        baseDate = timeArray[0]
        baseIndex = 0
        numberOfHitsWithinFive = 0
        reportCalled = False
        while (counter < numberOftimes ):
            baseDate
            secondTime = timeArray[counter]
            timeDifference = secondTime - baseDate
            fiveMinutes = timedelta(minutes=5)
            if (timeDifference <= fiveMinutes):
                #second time is within 5
                numberOfHitsWithinFive += 1
                reportCalled = False
            else:
                if (numberOfHitsWithinFive >= 10):
                    #had 5 or more hits, preform an analysis
                    baseIP = ipArray[baseIndex]
                    reportCalled = True
                    self.print_report(baseIP, numberOfHitsWithinFive)
                baseDate = secondTime
                baseIndex = counter
                numberOfHitsWithinFive = 0
                #second time is farther than 5 minutes apart
            #iterate Counter
            counter += 1
        if (numberOfHitsWithinFive >= 10 and reportCalled == False):
            baseIP = ipArray[baseIndex]
            self.print_report(baseIP, numberOfHitsWithinFive)
