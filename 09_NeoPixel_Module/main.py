import time
from machine import Pin
from neopixel import myNeopixel
"""

Super cool rainbow animation i got from the internett
Managed to make it work, the point is not to understand every line but to grasp the basics
thats why i created other animations in its own folder

"""


# 1. Setup our 8-LED ring on Pin 16
NUM_LEDS = 8
np = myNeopixel(NUM_LEDS, 16)
np.brightness(20)

# 2. A simple clock variable to keep track of where we are on the color wheel
color_step = 0

while True:
    # This loop goes through each of your 8 LEDs (0 to 7) one by one
    for pixel in range(8):
        
        # We tell each pixel to look exactly 32 steps ahead of the previous one.
        # We use % 255 so that if the number goes past 255, it wraps back to 0.
        pixel_color_pos = (color_step + (pixel * 32)) % 255
        
        # --- THE COLOR WHEEL MACHINE (Direct & Simple) ---
        # Zone 1: Red fading into Green
        if pixel_color_pos < 85:
            r = 255 - (pixel_color_pos * 3)
            g = pixel_color_pos * 3
            b = 0
            
        # Zone 2: Green fading into Blue
        elif pixel_color_pos < 170:
            pixel_color_pos = pixel_color_pos - 85 # Reset zone countdown to 0
            r = 0
            g = 255 - (pixel_color_pos * 3)
            b = pixel_color_pos * 3
            
        # Zone 3: Blue fading back into Red
        else:
            pixel_color_pos = pixel_color_pos - 170 # Reset zone countdown to 0
            r = pixel_color_pos * 3
            g = 0
            b = 255 - (pixel_color_pos * 3)
            
        # Give this specific pixel its calculated color
        np.set_pixel(pixel, r, g, b)

    # 3. Push the colors of all 8 LEDs to the physical ring at the exact same time
    np.show()
    
    # 4. Move the overall rainbow forward by 1 step for the next frame
    color_step = (color_step + 1) % 255
    
    time.sleep_ms(1) # Control how fast the rainbow spins
