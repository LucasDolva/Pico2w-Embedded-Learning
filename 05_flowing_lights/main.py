from machine import Pin
import time

# defining the pins we want to use
pin_numbers = [16, 17, 18, 19, 20, 21, 22, 26, 27, 28]

# 1. Start with an empty list to hold our configured pins
leds = []

# 2. Loop through every pin number in your array
for num in pin_numbers:
    # Set up the physical pin as an OUTPUT so Pin(16, Pin.OUT) and so on
    configured_pin = Pin(num, Pin.OUT)
    
    # Appending leds array with the configured pins
    leds.append(configured_pin)

def showLed(): #defining everything into a function
    # Flow forward
    for led in leds:
        led.value(1)
        time.sleep_ms(20) #sleep 20ms because it looks cool
        led.value(0)
        time.sleep_ms(20)        
        
    # Flow backward
    for led in reversed(leds):
        led.value(1)
        time.sleep_ms(20)
        led.value(0)
        time.sleep_ms(20)
          
while True: #constantly running the function
    showLed()
