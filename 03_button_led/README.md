# 02 - Button enabled LED

This project implements a **Pull-Up resistor** paired with **inverted logic** to control an external LED:

* **Hardware Stabilization:** Two 10kΩ resistor is utilized to ensure no false readings to Pin 13. This prevents the pin from "floating" and ensures a reliable **HIGH** state when the mechanical button is open.
* **Inverted Software Logic:** The MicroPython script is structured so that the LED is active-low:
  * **Button Open (Default):** Input reads "1" (HIGH) $\rightarrow$ LED is **OFF**.
  * **Button Closed (Pressed):** Input is pulled to Ground "0" (LOW) $\rightarrow$ LED turns **ON**.



