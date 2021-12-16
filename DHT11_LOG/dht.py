#!/usr/bin/python

import sys
import Adafruit_DHT
import time

start_time = time.time()
seconds = 30

while 1:
    humidity, temperature = Adafruit_DHT.read_retry(11, 2)
    #convert to F
    temperature = temperature * 1.8 + 32
    print ("%s,%.2f,%.2f"%(time.strftime("%m/%d/%Y %H:%M:%S"), humidity, temperature))
    while (time.time()-start_time) < seconds: 
        difftime = time.time()-start_time
        time.sleep(difftime)
    else:
        start_time = time.time() 

