from random import randint
import time
from machine import Pin
from neopixel import myNeopixel

strip = myNeopixel(num_leds=10, pin=16)
strip.brightness(50) # setting baseline brightness down

while True:
    
    #radar sweep we want 3 sweeps
    sweep = 1
    while sweep <= 3:
        # the internal logic for the radar sweep animation
        for pixel in range(10):
            strip.fill(0, 0, 0)
            
            # Calculate trailing pixels behind the head
            trail_1 = (pixel - 1) % 10
            trail_2 = (pixel - 2) % 10
            
            # Draw the trailing radar beam (Sonar Green)
            strip.set_pixel(trail_2, 0, 20, 0)   # Faint green afterglow
            strip.set_pixel(trail_1, 0, 60, 0)   # Medium green mid-beam
            strip.set_pixel(pixel, 0, 200, 0)    # Bright green radar head
            
            strip.show()
            time.sleep_ms(50) #delay between next pixel
        sweep+=1
    
    #warning sweep
    for pixel in range(10):
        strip.fill(0,0,0)
        strip.set_pixel(pixel,200,70,0)
        strip.show()
        time.sleep_ms(30) 
    
    #danger sweep
    for blink in range(2):
        strip.fill(0,0,0)
        strip.show()
        time.sleep_ms(100) #delay between dark and red light
        strip.fill(150,0,0)
        strip.show()
        time.sleep_ms(100) # delay between red and dark
