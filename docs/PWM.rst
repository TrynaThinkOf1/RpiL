How to control a GPIO pin with Pulse Width Modulation (PWM)
===========================================================

The class accepts three arguments:

* Pin Number
    * The Broadcom GPIO pin number
* Frequency
    * This is an optional argument, it defaults to 1000
* Duty-Cycle
    * This is an optional argument, it defaults to 50

PWM can be used to control the brightness of an LED, the speed of a motor, etc...

***

Here is a quick example:

.. code-block:: Python

    from RpiL import PWM  # import the 'PWM' class from RpiL library
    import time

    pwm_pin = PWM(16)  # I'm not going to set frequency or duty-cycle
    custom_pwm_pin = PWM(11, 730, 100)  # this however might not be ideal

    pwm_pin.start()
    time.sleep(3)  # wait 3 seconds
    pwm_pin.change_duty_cycle(65)  # this changes the duty cycle of the PWM pin
    time.sleep(2)
    pwm_pin.change_frequency(800)  # this changes the frequency of the PWM pin
    time.sleep(5)
    pwm_pin.stop()

***

That example would set up a GPIO pin, GPIO #16, for PWM functionality. It: turns the pin on, waits 3 seconds, changes the pin's duty cycle, waits 2 seconds, changes the pin's frequency, then waits 5 seconds, and finally stops the pin (effectively turning it off).
