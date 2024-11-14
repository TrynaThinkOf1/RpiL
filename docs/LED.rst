How to control an LED
======================

The class accepts one argument:

* Pin Number
    * The Broadcom GPIO pin number

***

Here is a quick example:

.. code-block:: Python

    from RpiL import LED  # import the 'LED' class from RpiL library
    import time

    led1 = LED(19)  # set up a new LED

    led1.on()
    time.sleep(1)
    led1.off()
    time.sleep(2)
    led1.toggle()
    time.sleep(1)
    led1.blink(10)  # this accepts one argument for duration of the blinking sequence, this defaults to 6 more on duration below

***

Duration of blinking:
----------------------

* The duration is how many times the LED will turn on and off in total
    * The LED will turn on for 0.5 seconds, and turn off for 0.5 seconds
* This might get changed to allow customization of how long the LED is on/off for

That example would set up an LED on GPIO #19, turn the LED on, wait 1 second, turn the LED off, wait 2 seconds, toggle the LED (if it's off, turn it on, and vice versa), then wait 1 second, and finally, it will enter a blinking function for 10 seconds.
