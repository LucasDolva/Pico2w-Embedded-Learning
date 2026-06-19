from machine import Pin
import time

led = Pin(15, Pin.OUT)                   
signal = Pin(13, Pin.IN)    #Create button object from Pin13 , Set GP13 to input
#input means it reads signals, in other words the pin acts as a voltage checker. 

try:
    while True:
        if not signal.value():          #we set up the button so that when it is pressed, the wire goes to ground hence this line
            led.value(1)                #Set led turn on 
        else:
            led.value(0)                #Set led turn off
except:
    pass
