# RpiL/pin

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class pin:
    def __init__(self, pin, mode):
        """This uses GPIO pin-number on the pi.\n
        This class is used to turn a gpio pin on or off.
        Use 'IN' or 'OUT' for input or output mode"""
        self.pin = int(pin)
        if mode.upper() == 'IN':
            self.mode = GPIO.IN
        else:
            self.mode = GPIO.OUT

        GPIO.setup(self.pin, self.mode)

    def on(self):
        if self.mode == GPIO.OUT:
            GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        if self.mode == GPIO.OUT:
            GPIO.output(self.pin, GPIO.LOW)

    def toggle(self):
        if self.mode == GPIO.OUT:
            if GPIO.input(self.pin) == 0:
                self.on()
            else:
                self.off()

    def value(self):
        """Return the gpio pin state (on/off, 1/0)."""
        if self.mode == GPIO.IN:
            return GPIO.input([self.pin])
