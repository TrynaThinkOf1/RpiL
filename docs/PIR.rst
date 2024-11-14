PIR Motion Detection with the PIR Class
========================================

The `PIR` class in the `RpiL` library is designed to interface with a Passive Infrared (PIR) motion sensor using the GPIO pins of a Raspberry Pi. It allows you to detect motion in a specific area and take action when motion is detected.

### Class Overview

The `PIR` class requires the following parameter for initialization:

* **pin** - The GPIO pin connected to the PIR sensor's output.

The sensor can be monitored continuously using a background thread that checks for motion, and it provides methods for detecting motion and waiting for motion events.

### Methods

* **motion_detected()**
    * Returns `True` if motion is detected, otherwise returns `False`. This method checks the most recent motion status.

* **wait_for_motion()**
    * Blocks and waits until motion is detected, returning `True` when motion is detected. This is useful for event-driven applications where an action is triggered once motion is detected.

### Example Usage

Here’s how you can use the `PIR` class to detect motion with a PIR sensor:

.. code-block:: Python

    from RpiL import PIR

    # Initialize PIR motion sensor with the GPIO pin number
    pir_sensor = PIR(pin=17)

    # Wait for motion detection
    if pir_sensor.wait_for_motion():
        print("Motion detected!")

    # Check if motion is detected
    if pir_sensor.motion_detected():
        print("Motion detected in the last check!")

### Notes

* The PIR sensor works by detecting infrared radiation, which typically comes from moving objects such as humans or animals.
* The `motion_detected` method returns a boolean indicating if motion has been detected at the last check, while the `wait_for_motion` method is a blocking call that waits until motion is detected before proceeding.
* The motion detection is continuously monitored in a separate background thread, ensuring non-blocking operation in your main program.
* The `PIR` class automatically handles GPIO cleanup when the object is deleted.

### Cleanup

The `PIR` class automatically cleans up the GPIO pin when the object is deleted, ensuring proper release of resources and preventing conflicts with other GPIO tasks.
