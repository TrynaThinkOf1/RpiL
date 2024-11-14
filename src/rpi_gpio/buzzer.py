# RpiL/buzzer

import RPi.GPIO as GPIO
import time as t
import threading

GPIO.setmode(GPIO.BCM)

class buzzer:
    """This uses GPIO pin-number on the pi.\n
    This class is for controlling basic Piezo Buzzers."""
    def __init__(self, pin):
        self.pin = pin

        self.beep_thread = None

        GPIO.setup(pin, GPIO.OUT)

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

    def beep_sequence(self, duration):
        GPIO.output(self.pin, GPIO.LOW)
        for i in range(int(duration)):
            self.on()
            t.sleep(0.5)
            self.off()
            t.sleep(0.5)

    def beep(self, duration):
        """Uses threads to make Beep() a non-blocking function"""
        if self.beep_thread and self.beep_thread.is_alive():
            self.beep_thread.join()

        self.beep_thread = threading.Thread(target=self.beep_sequence, args=(duration,))
        self.beep_thread.start()

    def __del__(self):
        GPIO.output(self.pin, GPIO.LOW)
        if self.beep_thread and self.beep_thread.is_alive():
            self.beep_thread.join()
        GPIO.cleanup(self.pin)
