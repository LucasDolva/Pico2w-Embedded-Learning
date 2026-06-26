from random import randint
import time
from machine import Pin
from neopixel import myNeopixel

# Create a strip of 10 NeoPixels on Pin 16
strip = myNeopixel(num_leds=10, pin=16)
strip.brightness(50) # Set it to a safe, comfortable brightness

while True:
    for i in range(10):
        strip.fill(0, 0, 0)       # Turn all pixels off
        
        # Generate a totally random RGB mix for this step
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        
        strip.set_pixel(i, r, g, b) # Set just ONE pixel to our random color
        strip.show()                # Push the data to the strip
        time.sleep_ms(100)
