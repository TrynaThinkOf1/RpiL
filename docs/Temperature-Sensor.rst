Using Temperature and Humidity Sensors (DHT11, DHT22, and AM2302)
==================================================================

The `Temperature_Sensor` class in the `RpiL` library is designed for reading temperature and humidity data from DHT sensors (such as DHT11, DHT22, and AM2302) on a Raspberry Pi. This class provides methods to obtain temperature in either Celsius or Fahrenheit and to measure humidity.

Class Overview

The `Temperature_Sensor` class requires two arguments:
* **out** - The GPIO pin number connected to the data output of the sensor.
* **sensor_type** - Defines the type of DHT sensor (DHT11, DHT22, or AM2302).

In addition, `DHT11`, `DHT22`, and `AM2302` classes extend `Temperature_Sensor` with preset sensor types for convenience.

Example Usage

Below is an example of using the `DHT22` subclass to read temperature and humidity data from a DHT22 sensor:

.. code-block:: Python

    from RpiL import DHT22
    import time

    sensor = DHT22(out=4)  # Connect DHT22 sensor to GPIO pin 4

    while True:
        temp = sensor.temperature("C")  # Read temperature in Celsius
        humidity = sensor.humidity()  # Read humidity
        if temp is not None and humidity is not None:
            print(f"Temperature: {temp:.1f}°C, Humidity: {humidity:.1f}%")
        else:
            print("Failed to retrieve data from sensor.")
        time.sleep(2)  # Wait for 2 seconds before the next reading

This example sets up a DHT22 sensor connected to GPIO pin 4, retrieves temperature and humidity readings in a loop, and prints them to the console.

Methods

* **temperature(measure_mode="C")**
    * Retrieves the temperature reading from the sensor.
    * **measure_mode** specifies the temperature unit:
        * `'C'`, `'Celsius'`, `'Centigrade'` - returns temperature in Celsius (default).
        * `'F'`, `'Fahrenheit'` - returns temperature in Fahrenheit.

* **humidity()**
    * Returns the humidity percentage reading from the sensor.

Subclasses

Each of the following classes is initialized with a specific DHT sensor type for ease of use:
* **DHT11** - Automatically initializes with the DHT11 sensor type.
* **DHT22** - Automatically initializes with the DHT22 sensor type.
* **AM2302** - Automatically initializes with the AM2302 sensor type.

Notes
* The `temperature` method will return `None` if data could not be retrieved from the sensor.
* Similarly, the `humidity` method returns `None` if the humidity reading is unavailable.
* It is recommended to call these methods with a delay (e.g., 2 seconds) between readings for reliable data.

Cleanup

The `Temperature_Sensor` class automatically configures and cleans up the GPIO pin setup upon deletion.
