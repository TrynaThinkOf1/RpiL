Motor Driver Control with the Motor_Driver Class
================================================

The `Motor_Driver` class in the `RpiL` library is designed to control an L298N motor driver using GPIO pins on a Raspberry Pi. It provides methods for controlling the direction and speed of two motors connected to the motor driver.

### Class Overview

The `Motor_Driver` class requires the following GPIO pin numbers for initialization:

* **in1** - The GPIO pin connected to IN1 on the L298N driver (default: 0).
* **in2** - The GPIO pin connected to IN2 on the L298N driver (default: 0).
* **ena** - The GPIO pin connected to ENA on the L298N driver (default: 0).
* **in3** - The GPIO pin connected to IN3 on the L298N driver (default: 0).
* **in4** - The GPIO pin connected to IN4 on the L298N driver (default: 0).
* **enb** - The GPIO pin connected to ENB on the L298N driver (default: 0).

PWM (Pulse Width Modulation) is used to control the speed of the motors connected to the driver.

### Methods

* **forward(speed=90)**
    * Makes both motors move forward at the specified speed.
    * The `speed` parameter defines the motor speed (0-100).

* **backward(speed=75)**
    * Makes both motors move backward at the specified speed.
    * The `speed` parameter defines the motor speed (0-100).

* **turn_right(speed=90)**
    * Makes the motor turn right by rotating one motor forward and the other backward.
    * The `speed` parameter defines the motor speed (0-100).

* **turn_left(speed=90)**
    * Makes the motor turn left by rotating one motor backward and the other forward.
    * The `speed` parameter defines the motor speed (0-100).

* **stop()**
    * Stops both motors by turning off all control pins and stopping the PWM signals for ENA and ENB.

### Example Usage

Here’s how you can use the `Motor_Driver` class to control a motor connected to an L298N motor driver:

.. code-block:: Python

    from RpiL import Motor_Driver

    # Initialize motor driver with appropriate GPIO pins
    motor_driver = Motor_Driver(in1=17, in2=27, ena=22, in3=23, in4=24, enb=25)

    motor_driver.forward(speed=90)  # Move motors forward at speed 90
    time.sleep(2)  # Keep motors running forward for 2 seconds

    motor_driver.turn_right(speed=75)  # Turn the motors right at speed 75
    time.sleep(2)  # Keep motors turning right for 2 seconds

    motor_driver.stop()  # Stop the motors

### Notes

* The `Motor_Driver` class controls two motors, one for each side of the L298N motor driver. The motors are connected via the IN1, IN2, IN3, and IN4 pins. The ENA and ENB pins control the motor speed via PWM.
* The speed is defined as a percentage (0-100), where 0 means no speed and 100 means full speed.
* The directions are controlled by setting appropriate IN pins HIGH or LOW. The forward and backward methods set these pins accordingly to drive the motors in the desired direction.
* The `turn_left` and `turn_right` methods are useful for differential steering, where one motor moves forward and the other moves backward.

### Cleanup

The `Motor_Driver` class automatically cleans up the GPIO pins when the object is deleted, ensuring proper release of the resources and preventing potential conflicts with other GPIO tasks.
