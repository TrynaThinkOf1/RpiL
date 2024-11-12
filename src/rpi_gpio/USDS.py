# RpiL/USDS

import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)

class USDS:
    def __init__(self, trig, echo):
        """This uses GPIO pin-numbers on the pi./n
        USDS stands for Ultra-Sonic Distance Sensor"""
        self.trig = trig
        self.echo = echo

        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def distance(self):
        """Measures distance in cm"""
        GPIO.output(self.trig, GPIO.LOW)
        t.sleep(0.5)

        GPIO.output(self.trig, GPIO.HIGH)
        t.sleep(0.00001)
        GPIO.output(self.trig, GPIO.LOW)

        start = t.time()
        while GPIO.input(self.echo) == 0:
            start = t.time()

        stop = t.time()
        while GPIO.input(self.echo) == 1:
            stop = t.time()

        elapsed = stop - start
        distance_ = (elapsed * 34300) / 2

        return distance_

    def __del__(self):
        GPIO.cleanup([self.trig, self.echo])