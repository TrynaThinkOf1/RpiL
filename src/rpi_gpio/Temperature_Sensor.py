# RpiL/Heat_Sensor

import RPi.GPIO as GPIO
import Adafruit_DHT as DHT

GPIO.setmode(GPIO.BCM)

class Temperature_Sensor:
    def __init__(self, out, sensor_type):
        """This uses GPIO pin-numbers on the pi."""
        self.out = out
        self.sensor_type = sensor_type

        GPIO.setup(self.out, GPIO.IN)

    def temperature(self, measure_mode="C"):
        """measure_mode is for:/n
        'F', 'Fahrenheit', 'C', 'Celsius', 'Centigrade'"""
        humidity, temp = DHT.read_retry(self.sensor_type, self.out)

        if temp is not None:
            if measure_mode in ['F', 'Fahrenheit']:
                return temp * 9.0 / 5.0 + 32.0
            elif measure_mode in ['C', 'Celsius', 'Centigrade']:
                return temp
        else:
            return None

    def humidity(self):
        humidity, _ = DHT.read_retry(self.sensor_type, self.out)

        if humidity is not None:
            return humidity
        else:
            return None

class DHT11(Temperature_Sensor):
    def __init__(self, out):
        super().__init__(out, DHT.DHT11)

class DHT22(Temperature_Sensor):
    def __init__(self, out):
        super().__init__(out, DHT.DHT22)

class AM2302(Temperature_Sensor):
    def __init__(self, out):
        super().__init__(out, DHT.AM2302)
