Controlling RGB LEDs with the RGB_LED Class
==========================================

The `RGB_LED` class in the `RpiL` library is designed to control an RGB LED using three GPIO pins. It provides methods for setting specific colors, cycling through a rainbow of colors, and turning the LED on or off.

### Class Overview

The `RGB_LED` class requires three GPIO pin numbers as arguments:
* **red_pin** - The GPIO pin connected to the red component of the RGB LED.
* **green_pin** - The GPIO pin connected to the green component of the RGB LED.
* **blue_pin** - The GPIO pin connected to the blue component of the RGB LED.

PWM (Pulse Width Modulation) is used to control the brightness of each color component of the LED.

### Methods

* **set_color(hex_color)**
    * Sets the RGB LED to a specific color based on a hex string (e.g., '#FF00FF').
    * Converts the hex color into individual red, green, and blue components, and adjusts the PWM duty cycle accordingly.

* **rainbow_cycle(wait=0.05)**
    * Starts a rainbow color cycling effect in a separate thread. The LED will continuously cycle through rainbow colors.
    * The `wait` parameter controls the speed of the color transitions (in seconds).

* **stop_rainbow_cycle()**
    * Stops the rainbow color cycling effect and turns off the LED.

* **wheel(position=0)**
    * A static method that generates a color based on the position in the 0-255 range. This creates a smooth rainbow effect.
    * `position` is an integer between 0 and 255 that determines the current color.

* **off()**
    * Turns off the RGB LED by setting all PWM duty cycles to 0.

### Example Usage

Here’s how you can use the `RGB_LED` class to control an RGB LED:

.. code-block:: Python

    from RpiL import RGB_LED

    # Initialize RGB LED with red pin on GPIO 17, green pin on GPIO 27, blue pin on GPIO 22
    led = RGB_LED(red_pin=17, green_pin=27, blue_pin=22)

    led.set_color('#FF00FF')  # Set color to purple
    time.sleep(2)  # Keep LED on for 2 seconds

    led.rainbow_cycle()  # Start rainbow effect
    time.sleep(10)  # Run rainbow for 10 seconds
    led.stop_rainbow_cycle()  # Stop rainbow effect

    led.off()  # Turn off the LED

### Notes

* This class uses PWM to control the brightness of each color component of the RGB LED. The duty cycle (0-100) corresponds to the brightness of the LED.
* To create a smooth color transition, the `rainbow_cycle` method cycles through a range of colors. The `wheel` method generates the appropriate RGB values for each position.
* The `set_color` method accepts a hex string, which is a standard format for representing colors (e.g., '#FF00FF' for purple).

### Cleanup

The `RGB_LED` class automatically cleans up the GPIO pins when the object is deleted, ensuring proper release of the resources. If the rainbow cycle is running, it is also stopped before cleanup.
