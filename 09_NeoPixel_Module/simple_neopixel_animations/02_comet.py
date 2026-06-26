import time
from machine import Pin
from neopixel import myNeopixel

strip = myNeopixel(num_leds=8, pin=16)
strip.brightness(60) # High base brightness

while True:
    for i in range(8):
        strip.fill(0, 0, 0) # Clear the ring
        
        # Calculate the positions behind the comet (i)
        tail_medium = (i - 1) % 8  # -1 mod 8 = 7 
        tail_dim = (i - 2) % 8  # -2 mod 8 = 6 and so on
        
        # Draw the comet from tail to head
        strip.set_pixel(tail_dim, 0, 20, 50)       # Dim Blue tail
        strip.set_pixel(tail_medium, 0, 100, 200)  # Medium Cyan middle
        strip.set_pixel(i, 255, 255, 255)          # Pure White blazing head
        
        strip.show()
        time.sleep_ms(100)

