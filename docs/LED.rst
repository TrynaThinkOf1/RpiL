How to Control an LED
======================

The `LED` class in the `RpiL` library provides basic control for an LED connected to a Raspberry Pi GPIO pin. This class allows turning the LED on and off, toggling its state, and blinking it with a specified duration.

The `LED` class accepts one argument:

* **Pin Number**
    * The Broadcom GPIO pin number connected to the LED.

Here is an example of using the `LED` class:

.. code-block:: Python

    from RpiL import LED
    import time

    led = LED(18)  # Create an LED instance on GPIO pin 18

    led.on()       # Turn the LED on
    time.sleep(2)  # Wait for 2 seconds
    led.off()      # Turn the LED off
    time.sleep(1)  # Wait for 1 second
    led.blink(10)  # Blink the LED for 10 seconds

This example sets up an LED on GPIO pin 18, turns it on, turns it off, and then blinks it for 10 seconds.

Methods
-------

* **on()**
    * Turns the LED on.

* **off()**
    * Turns the LED off.

* **toggle()**
    * Toggles the LED's state. If it is on, it turns off; if it is off, it turns on.

* **blink(duration=6)**
    * Blinks the LED in a non-blocking manner for the specified duration (default is 6 seconds). This method uses a separate thread to allow other code to run while the LED blinks.

* **blink_sequence(duration=6)**
    * The internal method responsible for blinking the LED by turning it on and off in half-second intervals.

Notes
-----

* The `blink` method initiates a separate thread for non-blocking operation, allowing the LED to blink while other processes continue.
* The `__del__` method ensures that the LED is turned off and the GPIO pin is cleaned up when the `LED` instance is deleted.

Cleanup
-------

The class destructor (`__del__`) turns the LED off, waits for any active blink thread to finish, and cleans up the GPIO pin.
