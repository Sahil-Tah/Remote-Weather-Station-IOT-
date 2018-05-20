#!/usr/bin/python
import os
import datetime
import sys
import Adafruit_DHT
import urllib2
import csv

currentDT = datetime.datetime.now()
time = currentDT.strftime("%Y-%m-%d %H:%M:%S")
date=currentDT.strftime("%d%b%Y")

baseURL = 'https://api.thingspeak.com/update?api_key=<your_api_key>'  
#ThingSpeak -> Channels -> Api keys -> Select the one with 'Update a channel feed

'''
def getCPUtemperature():
        res =os.popen('vcgencmd measure_temp').readline()
        return(res.replace("temp="," ").replace("'C\n "," "))
'''

def createCSV():
        with open(date+'.csv','w') as csv_file:
                fieldName = [" Temperature C "," Humidity % "," Time "]
                csv_writer = csv.writer(csv_file)
                #csv_writer.writeheader()
                for i in range(1,1000):
                        csv_writer.writerow([temperature,humidity,time])


while True:

        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        f1 = urllib2.urlopen(baseURL+"&field1=%s" % (temperature)+ "&field2=%s" % (humidity))
        f1.close()
        #cpuTemp=int(float(getCPUtemperature()))
        output = 'Temp: {0:0.1f} C  Humidity: {1:0.1f} % '.format(temperature, humidity)+(currentDT.strftime("%Y-%m-%d %H:%M:%S"))
        print (output)

        createCSV()          

sys.exit()
