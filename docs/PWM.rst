How to Control a GPIO Pin with Pulse Width Modulation (PWM)
===========================================================

The `PWM` class in the `RpiL` library enables Pulse Width Modulation (PWM) control on a Raspberry Pi GPIO pin. This class allows you to set and modify the frequency and duty cycle of the PWM signal, which is commonly used for applications such as controlling the brightness of an LED or adjusting the speed of a motor.

The `PWM` class accepts three arguments:

* **Pin Number**
    * The Broadcom GPIO pin number.
* **Frequency**
    * An optional argument to set the PWM frequency, defaults to 1000 Hz.
* **Duty Cycle**
    * An optional argument to set the PWM duty cycle, defaults to 50%.

Example

Below is an example of using the `PWM` class:

.. code-block:: Python

    from RpiL import PWM
    import time

    pwm_pin = PWM(16)  # Initialize pin 16 for PWM with default frequency and duty cycle
    custom_pwm_pin = PWM(11, 730, 100)  # Initialize pin 11 with a custom frequency and duty cycle

    pwm_pin.start()  # Start PWM on pin 16
    time.sleep(3)  # Wait 3 seconds
    pwm_pin.change_duty_cycle(65)  # Change the duty cycle to 65%
    time.sleep(2)  # Wait 2 seconds
    pwm_pin.change_frequency(800)  # Change the frequency to 800 Hz
    time.sleep(5)  # Wait 5 seconds
    pwm_pin.stop()  # Stop PWM on pin 16

This example demonstrates how to initialize a GPIO pin for PWM, start the PWM signal, modify its duty cycle and frequency, and stop it.

Methods

* **start()**
    * Starts PWM on the specified pin with the current duty cycle.

* **change_duty_cycle(duty_cycle)**
    * Changes the duty cycle of the PWM signal. Only effective if the PWM is currently running.

* **change_frequency(frequency)**
    * Changes the frequency of the PWM signal. If PWM is running, it restarts with the new frequency and the current duty cycle.

* **stop()**
    * Stops the PWM signal on the specified pin.

Notes
* `start()` must be called before changing the duty cycle or frequency for the PWM effect to take place.
* The class initializes and sets up the pin for output, and the `__del__` method cleans up the GPIO configuration.

Cleanup

The `PWM` class automatically stops the PWM signal and cleans up the GPIO pin configuration when the instance is deleted.
