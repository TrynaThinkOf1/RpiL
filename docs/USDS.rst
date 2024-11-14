Using the Ultra-Sonic Distance Sensor (USDS)
============================================

The `USDS` class in the `RpiL` library is designed to measure distances using an ultrasonic sensor connected to the GPIO pins on a Raspberry Pi. This class calculates the distance based on the time delay between sending and receiving an ultrasonic pulse.

### Class Overview

The `USDS` class requires two arguments:
* **trig** - The GPIO pin connected to the Trigger pin of the ultrasonic sensor.
* **echo** - The GPIO pin connected to the Echo pin of the ultrasonic sensor.

The sensor works by emitting an ultrasonic pulse from the trigger pin and measuring the time it takes for the echo to return. The `distance` method returns the calculated distance in centimeters.

### Example Usage

Below is an example of using the `USDS` class to read distance data from an ultrasonic sensor:

.. code-block:: Python

    from RpiL import USDS
    import time

    sensor = USDS(trig=23, echo=24)  # Trigger pin on GPIO 23, Echo pin on GPIO 24

    try:
        while True:
            dist = sensor.distance()  # Measure distance
            print(f"Distance: {dist:.1f} cm")
            time.sleep(1)  # Wait 1 second before the next measurement
    except KeyboardInterrupt:
        pass  # Stops the loop with Ctrl+C

This example sets up an ultrasonic sensor with trigger and echo pins on GPIO pins 23 and 24, respectively. It retrieves distance readings in a loop and prints them to the console.

### Methods

* **distance()**
    * Sends an ultrasonic pulse, measures the time taken for the echo to return, and calculates the distance in centimeters.
    * Returns the measured distance as a float value.

### Notes

* The `distance` method may return inaccurate values if there is interference or an object is too close or too far.
* It is recommended to add a delay (e.g., 1 second) between calls to `distance` to allow for stable readings.

Cleanup
-------

The `USDS` class automatically cleans up the GPIO pin configuration upon deletion.
