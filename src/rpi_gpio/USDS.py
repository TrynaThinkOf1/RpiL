# RpiL/USDS

import RPi.GPIO as GPIO
import time as t
import threading

GPIO.setmode(GPIO.BCM)

class USDS:
    def __init__(self, trig, echo):
        """This uses GPIO pin-numbers on the pi./n
        USDS stands for Ultra-Sonic Distance Sensor"""
        self.trig = trig
        self.echo = echo

        GPIO.setup(self.trig, GPIO.IN)
        GPIO.setup(self.echo, GPIO.IN)