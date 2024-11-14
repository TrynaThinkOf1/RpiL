How to Monitor CPU Temperature
==============================

The `CPU` class in the `RpiL` library provides a simple interface for monitoring the CPU temperature on a Raspberry Pi. This class uses the `gpiozero` library to retrieve the temperature and supports multiple units of measurement.

The `CPU` class accepts no arguments upon initialization.

Here is an example of using the `CPU` class:

.. code-block:: Python

    from RpiL import CPU

    cpu = CPU()  # Create an instance of the CPU class

    # Print the CPU temperature in Celsius, Fahrenheit, and Kelvin
    print(f"CPU Temperature in Celsius: {cpu.temperature('C')} °C")
    print(f"CPU Temperature in Fahrenheit: {cpu.temperature('F')} °F")
    print(f"CPU Temperature in Kelvin: {cpu.temperature('K')} K")

In this example, the CPU temperature is retrieved in Celsius, Fahrenheit, and Kelvin.

Methods

* **temperature(measure="C")**
    * Retrieves the current CPU temperature. The `measure` parameter accepts:
        - `"C"` for Celsius (default)
        - `"F"` for Fahrenheit
        - `"K"` for Kelvin

    If an unsupported unit is provided, this method raises a `ValueError`.

Cleanup

The `CPU` class includes a destructor method (`__del__`) that clears the instance upon deletion.
