# RpiL/CPU

from gpiozero import CPUTemperature

class CPU:
    def __init__(self):
        self.self = self
        self.cpu = CPUTemperature()

    def temperature(self, measure="C"):
        """Measure should be in F-Fahrenheit, C-Celsius, K-Kelvin"""
        if measure == "C":
            return self.cpu.temperature()
        elif measure == "F":
            return self.cpu.temperature() * (9 / 5 + 32)
        elif measure == "K":
            return self.cpu.temperature() + 273.15
        else:
            raise ValueError("measure must be C-Celsius, F-Fahrenheit, K-Kelvin")

    def __del__(self):
        self.self = None