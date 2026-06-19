from machine import Pin
import time

led = Pin(15, Pin.OUT)                   
signal = Pin(13, Pin.IN)    #Create button object from Pin13 , Set GP13 to input

def switchLED():  #function: if light on turn it off and vice versa
    if led.value():
        led.value(0)                  #Set led turn off
    else:
        led.value(1)                  #Set led turn on
        
try:
    while True:
        if not signal.value():  #if detect button press wait 20ms for the physical bouncing of the button to stop
            time.sleep_ms(20)
            if not signal.value(): #if it still is pressed then it is a legitimate press, switch the light on or off
                switchLED()
                while not signal.value(): #this is for the held button state, here whilst button is held sleep forever essentially
                    time.sleep_ms(20)
except:
    pass
