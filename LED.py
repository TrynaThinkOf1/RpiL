# RpiL/LED

import Rpi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)

class LED:
    def __init__(self, pin):
        """This uses GPIO pin-number on the pi.\n
        This class is for controlling basic LED's."""
        self.pin = int(pin)

        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        if GPIO.input(self.pin) == 0:
            GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        if GPIO.input(self.pin) == 1:
            GPIO.output(self.pin, GPIO.LOW)

    def toggle(self):
        if GPIO.input(self.pin) == 0:
            self.on()
        else:
            self.off()

    def blink(self, duration=6):
        GPIO.output(self.pin, GPIO.LOW)
        for i in range(int(duration)):
            self.on()
            t.sleep(0.5)
            self.off()
            t.sleep(0.5)

    def __del__(self):
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.cleanup(self.pin)
