from machine import Pin, PWM
import time

"""
Most of the advanced code here is for the Comet effect
It is not necessary to understand every sequence here

the important parts are;
1. Pin Setup
2. Using and learning nested loops and controll variables to avoid cluttered code.

"""
#Setup the pins
pin_numbers = [16, 17, 18, 19, 20, 21, 22, 26, 27, 28]
pwm_leds = []
for num in pin_numbers:
    configured_pwn = PWM(Pin(num), freq=10000)
    pwm_leds.append(configured_pwn)
    


# Baked Wave, this is mainly for a cool effect of the wave, optional fun
dutys = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,       
    65535, 32768, 16384, 8192, 4096,    
    2048, 1024, 512, 256, 128,          
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0        
]
delayTimes = 70 # controlling all delay times with this variable

try:
    while True:
        # Comet lighting from led[9] to led [0]
        for i in range(0, 20):
            for j in range(0, 10):
                # Grabs the specific LED object from our list
                pwm_leds[j].duty_u16(dutys[i + j])
            time.sleep_ms(delayTimes)
            
        # Comet lighting from led [0] to led [9]
        for i in range(0, 20):
            for j in range(0, 10):
                # Subtracting "j" from 9 cleanly reverses the target index
                pwm_leds[9 - j].duty_u16(dutys[i + j])
            time.sleep_ms(delayTimes)

except:
    # Clean up loop sweeping through all 10 engines automatically
    for led in pwm_leds:
        led.duty_u16(0)
        led.deinit()
    print("safely shutting down the PWM engien.")

