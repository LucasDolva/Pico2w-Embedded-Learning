from machine import Pin, PWM
import time

#set PWM pin to gp15
pwm = PWM(Pin(15))
#setting the speed to 10 000 hz, so the Pico actually flips the pin on and off 10k times a second
pwm.freq(10000) 

try:
    while True:
        """
        micropython uses 16-bit number to control the duty cycle
        so to get 100% brightness we need a Duty-Cycle of 2^16 - 1 = 65535
        if we wanted 50% brightness we would have 65535 // 2 = 32767 (floor division)
        
        so this script sets the Duty-Cycle from low to high and then back down again
        the step in the loop and the sleep is manaly desided by the effect i liked the most
        
        """
        for i in range(0, 65535, 4): 
            pwm.duty_u16(i) #function set duty cycle, u16 is unnasigned 16-bit int
            time.sleep_us(50) #sleep so we can physically see the effect
        for i in range(65535, 0, -4):
            pwm.duty_u16(i)
            time.sleep_us(50)
except:
    #error handeling, when i stop the script just turn off the pwm pins
    pwm.deinit()


