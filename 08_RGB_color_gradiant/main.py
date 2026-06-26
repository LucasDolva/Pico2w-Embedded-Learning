from machine import Pin, PWM
import time

#       R    G   B  based on physical implementation on the breadboard
pins = [13, 12, 11]
freq_num = 10000

#Initializing PWM Pins on pin 11, 12, 13
pwmPin13 = PWM(Pin(pins[0]), freq = freq_num)  
pwmPin12 = PWM(Pin(pins[1]), freq = freq_num)
pwmPin11 = PWM(Pin(pins[2]), freq = freq_num)

def set_light(r, g, b):
    # Just remember: 65535 is OFF, 0 is max brightness
    pwmPin13.duty_u16(65535 - r)
    pwmPin12.duty_u16(65535 - g)
    pwmPin11.duty_u16(65535 - b)
    """
    this way is following the pin logic, we have a constant supply 3.3v to the rgb led via the 3v3 OUT pin 
    when we set the pwm pin to 65535 it also supplies 3.3v hence there will we no potential diff, hence no light
    
    if we take red as example, when we set the pwm pin to 65535 it meets the constant supply of 3.3v with 3.3v
    and the result will be that red is off
    
    when the pwm pin is at 0 then the constant supply of 3.3v will be met with 0v from the pwm pin
    and we will have max brightness of red. 
        
    """

try:
    while True:
        # 1. Fade from RED to GREEN
        for i in range(0, 65535, 1000):
            set_light(65535 - i, i, 0)
            time.sleep_ms(10)
            
        # 2. Fade from GREEN to BLUE
        for i in range(0, 65535, 1000):
            set_light(0, 65535 - i, i)
            time.sleep_ms(10)
            
        # 3. Fade from BLUE back to RED
        for i in range(0, 65535, 1000):
            set_light(i, 0, 65535 - i)
            time.sleep_ms(10)
except:
    pwm0.deinit()
    pwm1.deinit()
    pwm2.deinit()

