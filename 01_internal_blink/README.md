# 01 - Onboard Internal Blink

The objective of this first project was to verify the MicroPython environment setup and test the basic syntax of the `machine.Pin` class.

### 💡 Key Engineering Takeaway
* **The "LED" String:** Unlike the original Raspberry Pi Pico (which maps the onboard LED to physical GPIO 25), the **Pico 2 W** routes its onboard LED through the wireless chip. Because of this architecture, we must initialize the pin using the string identifier `"LED"` instead of an integer index: `Pin("LED", Pin.OUT)`.
