# 06 - Breathing LED

## Overview 

This project replicates a organic "breathing" or pulsing fade effect on an LED. The goal is to get acquainted with the PWM engiene. 

## Key Takeaways
* **Deep-Dive into PWM Resolution:** Leveraged MicroPython's 16-bit PWM system "duty_u16", mapping brightness across a scale from "0" (min) to "65535" (max). Where "65535" is the biggest possible unnasigned 16-bit number 2^16 - 1 = 65535 hence duty_**u16**
