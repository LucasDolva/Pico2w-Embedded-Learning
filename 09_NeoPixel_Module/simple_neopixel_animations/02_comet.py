import time
from machine import Pin
from neopixel import myNeopixel

strip = myNeopixel(num_leds=10, pin=16)
strip.brightness(60) # High base brightness

while True:
    for i in range(10):
        strip.fill(0, 0, 0) # Clear the ring
        
        # Calculate the positions behind the comet (i)
        tail_medium = (i - 1) % 10
        tail_dim = (i - 2) % 10
        
        # Draw the comet from tail to head
        strip.set_pixel(tail_dim, 0, 20, 50)       # Dim Blue tail
        strip.set_pixel(tail_medium, 0, 100, 200)  # Medium Cyan middle
        strip.set_pixel(i, 255, 255, 255)          # Pure White blazing head
        
        strip.show()
        time.sleep_ms(100)
