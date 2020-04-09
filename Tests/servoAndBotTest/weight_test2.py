#Credit to https://circuitdigest.com/microcontroller-projects/iot-raspberry-pi-smart-container

import RPi.GPIO as gpio
import serial
import time
import random


import smtplib


DT =27
SCK=17



sample=0


gpio.setwarnings(False)
gpio.setmode(gpio.BCM)


gpio.setup(SCK, gpio.OUT)




def show_weight():
    count= readCount()
    w=0
  
    w=(count-sample)/106
    actualw = w - YOURVALUE
    
    
    
    
    print actualw/YOURRESULT,"g"
   
  return actualw/YOURRESULT






def readCount():
  i=0
  Count=0
  #print Count
  time.sleep(0.5)
  gpio.setup(DT, gpio.OUT)
  gpio.output(DT,1)
  gpio.output(SCK,0)
  gpio.setup(DT, gpio.IN)

  while gpio.input(DT) == 1:
      i=0
  for i in range(24):
        gpio.output(SCK,1)
        Count=Count<<1

        gpio.output(SCK,0)
        #time.sleep(0.001)
        if gpio.input(DT) == 0: 
            Count=Count+1
            #print Count
        
  gpio.output(SCK,1)
  Count=Count^0x800000
  #time.sleep(1)
  gpio.output(SCK,0)
  return Count 
while 1:
  show_weight();
  

