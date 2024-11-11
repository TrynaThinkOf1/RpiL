# RpiL/LED

import RPi.GPIO as GPIO
import time as t
import threading

GPIO.setmode(GPIO.BCM)

class LED:
    def __init__(self, pin):
        """This uses GPIO pin-number on the pi.\n
        This class is for controlling basic LED's."""
        self.pin = int(pin)

        self.led_thread = None

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

    def blink_sequence(self, duration=6):
        GPIO.output(self.pin, GPIO.LOW)
        for i in range(int(duration)):
            self.on()
            t.sleep(0.5)
            self.off()
            t.sleep(0.5)

    def blink(self, duration=6):
        if self.led_thread and self.led_thread.is_alive():
            self.led_thread.join()

        self.led_thread = threading.Thread(target=self.blink_sequence, args=(duration,))
        self.led_thread.start()

    def __del__(self):
        GPIO.output(self.pin, GPIO.LOW)
        if self.led_thread and self.led_thread.is_alive():
            self.led_thread.join()
        GPIO.cleanup([self.pin])
