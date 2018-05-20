#!/usr/bin/python
import csv
import datetime

currentDT = datetime.datetime.now()
date = (currentDT.strftime("%d%b%Y"))

print("\nReports are named as per date, which report would you like to see?")
print("\nFile name format is as follows: "+ date)
print("\nEnter the date (DDMonYYY): ")
file = raw_input()
file=file+".csv"


with open (file,'r') as csv_file:
        #fieldname= ['Temp C', 'Humidity %','Time']
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
                print(line)
