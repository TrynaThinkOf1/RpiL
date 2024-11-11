# RpiL/motor

import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class motor:
    def __init__(self, forward_pin, backward_pin):
        """This uses GPIO pin-numbers for the pi.\n
        This class is to run a motor without a driver"""
        self.forward_pin = forward_pin
        self.backward_pin = backward_pin

        GPIO.setup(self.forward_pin, GPIO.OUT)
        GPIO.setup(self.backward_pin, GPIO.OUT)

    def forward(self):
        GPIO.output(self.forward_pin, GPIO.HIGH)
        GPIO.output(self.backward_pin, GPIO.LOW)

    def backward(self):
        GPIO.output(self.forward_pin, GPIO.LOW)
        GPIO.output(self.backward_pin, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.forward_pin, GPIO.LOW)
        GPIO.output(self.backward_pin, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup(self.forward_pin, self.backward_pin)
