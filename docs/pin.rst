How to Control a GPIO Pin
==========================

The `pin` class in the `RpiL` library allows basic control over a GPIO pin on a Raspberry Pi. This class can configure the pin as either an input or output and provides methods for turning the pin on and off, toggling its state, and reading its current value.

The `pin` class accepts two arguments:

* **Pin Number**
    * The Broadcom GPIO pin number.
* **Mode**
    * Set to either `"IN"` (input mode) or `"OUT"` (output mode).

Here is an example of using the `pin` class:

.. code-block:: Python

    from RpiL import pin

    led_pin = pin(17, "OUT")  # Set GPIO pin 17 as an output
    button_pin = pin(27, "IN")  # Set GPIO pin 27 as an input

    led_pin.on()  # Turn on the pin (high)
    led_pin.toggle()  # Toggle the pin state
    print(button_pin.value())  # Print the current state of the button pin

In this example, GPIO pin 17 is configured as an output, while GPIO pin 27 is configured as an input. The output pin can be toggled on and off, and the input pin’s value is read.

Methods
-------

* **on()**
    * Sets the output pin to high (on). Only works if the pin is configured as an output.

* **off()**
    * Sets the output pin to low (off). Only works if the pin is configured as an output.

* **toggle()**
    * Toggles the state of the output pin. If it is on, it will turn off, and vice versa. Only works if the pin is configured as an output.

* **value()**
    * Returns the current state of the pin:
        - If configured as an input, returns the current pin state (1 for high/on, 0 for low/off).
        - Raises an error if called on an output pin.

Notes
-----

* The `toggle` and `value` methods are mode-dependent. They function only if the pin is configured in the appropriate mode (`OUT` for toggle, `IN` for value).
* The class initializes the GPIO setup for the specified pin and mode.

Cleanup
-------

The `pin` class destructor cleans up the GPIO configuration when the instance is deleted.
