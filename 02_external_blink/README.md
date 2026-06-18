# 02 - External Breadboard LED Blink

The goal here was to wire up an external LED on a breadboard and control it using a physical GPIO pin.

### 💡 Key Takeaway
* **Don't Fry the Board:** Microcontroller pins output 3.3V, which is too much for a raw LED. I added a **220Ω resistor** in series to protect the LED and the Pico 2 W from burning out.
* **Pin Mapping:** Instead of using the `"LED"` string like the internal light, external components are controlled using the physical pin number (e.g., `Pin(15, Pin.OUT)`).

### 📹 Demonstration
<img width="640" height="480" alt="IMG_9255" src="https://github.com/user-attachments/assets/2a81d3a0-b71b-4147-8673-835046f8be03" />
