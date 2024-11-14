Controlling Motors with the motor Class
=======================================

The `motor` class in the `RpiL` library is used to control the forward and backward movement of a motor using two GPIO pins for the forward and backward directions. This class allows you to control a motor directly without the use of a motor driver.

### Class Overview

The `motor` class requires two arguments:
* **forward_pin** - The GPIO pin connected to the motor's forward direction control.
* **backward_pin** - The GPIO pin connected to the motor's backward direction control.

### Methods

* **forward()**
    * Activates the motor to move in the forward direction by setting the forward GPIO pin to HIGH and the backward GPIO pin to LOW.
* **backward()**
    * Activates the motor to move in the backward direction by setting the forward GPIO pin to LOW and the backward GPIO pin to HIGH.
* **stop()**
    * Stops the motor by setting both the forward and backward GPIO pins to LOW.

### Example Usage

Here’s how you can use the `motor` class to control a motor:

.. code-block:: Python

    from RpiL import motor

    # Initialize motor with forward pin on GPIO 17 and backward pin on GPIO 27
    motor_control = motor(forward_pin=17, backward_pin=27)

    motor_control.forward()  # Move motor forward
    time.sleep(2)  # Run motor for 2 seconds

    motor_control.backward()  # Move motor backward
    time.sleep(2)  # Run motor for 2 seconds

    motor_control.stop()  # Stop motor

This example demonstrates how to initialize the motor with specific GPIO pins for forward and backward movement. The motor will run forward for 2 seconds, then backward for 2 seconds, and finally stop.

### Notes

* This class does not control motor speed. If you need to control the motor's speed, you will need a motor driver with PWM (Pulse Width Modulation) capability.
* Always ensure that the GPIO pins used are correctly configured to avoid damaging your Raspberry Pi.

### Cleanup

The `motor` class automatically cleans up the GPIO pins when the object is deleted or the program ends, ensuring proper GPIO pin release.
