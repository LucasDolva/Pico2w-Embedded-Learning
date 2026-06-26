from random import randint
import time
from machine import Pin
from neopixel import myNeopixel

strip = myNeopixel(num_leds=8, pin=16)

while True:
    # Pick a random color for this breath
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    
    # Breathe inn (step 5 brightness up from 10 to 150)
    for level in range(10, 151, 5):
        strip.brightness(level) # 1. Set the new scaling level
        strip.fill(r, g, b)     # 2. Re-draw the pixels with the new scale
        strip.show()            # 3. Push to hardware
        time.sleep_ms(15)
        
    # Breathe out (step 5 brightness back down from 150 to 10)
    for level in range(150, 9, -5):
        strip.brightness(level)
        strip.fill(r, g, b)
        strip.show()
        time.sleep_ms(15)
        
    time.sleep_ms(100) # Pause a moment in the dark before next breath
