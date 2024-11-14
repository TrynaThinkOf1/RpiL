How to Control a Piezo Buzzer
=============================

The `buzzer` class allows for basic control of a Piezo buzzer connected to a Raspberry Pi GPIO pin.

The class accepts one argument:

* **Pin Number**
    * The Broadcom GPIO pin number for the pin connected to the Piezo buzzer.

The buzzer class provides methods for turning the buzzer on, off, toggling its state, and initiating a beep sequence. The `beep()` function is threaded to allow non-blocking control, making it suitable for integrating the buzzer with other concurrent processes.

Here is a quick example:

.. code-block:: Python

    from RpiL import buzzer  # Import the 'buzzer' class from RpiL library
    import time

    my_buzzer = buzzer(18)  # Instantiate a buzzer object on GPIO pin 18

    my_buzzer.on()  # Turn on the buzzer
    time.sleep(2)   # Wait for 2 seconds
    my_buzzer.off()  # Turn off the buzzer

    my_buzzer.beep(5)  # Start a non-blocking beep sequence that lasts for 5 seconds
    time.sleep(7)   # Wait enough time for the beep sequence to finish

In this example, a `buzzer` object is created for GPIO pin 18. The example demonstrates turning the buzzer on, then off, and then starting a 5-second beep sequence. The `beep()` method toggles the buzzer on and off every 0.5 seconds during the sequence.

Methods

* **on()**
    * Turns the buzzer on by setting the specified GPIO pin to HIGH.

* **off()**
    * Turns the buzzer off by setting the specified GPIO pin to LOW.

* **toggle()**
    * Toggles the buzzer's state; if it’s on, it turns it off, and vice versa.

* **beep(duration)**
    * Starts a beep sequence of a specified duration (in seconds). The sequence alternates between turning the buzzer on and off every 0.5 seconds. This method is non-blocking and uses threading.
