# RpiL/PWM

import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class PWM:
    def __init__(self, pin, frequency=1000):
        """This uses GPIO pin-number on the pi.\n
        This class is for Pulse Width Modulation"""
        self.pin = int(pin)
        self.frequency = frequency

        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.frequency)
        self.pwm_started = False

    def start(self, duty_cycle=50):
        """Start the PWM with specified Duty-Cycle"""
        if not self.pwm_started:
            self.pwm.start(duty_cycle)
            self.pwm_started = True
        else:
            self.pwm.ChangeDutyCycle(duty_cycle)

    def change_duty_cycle(self, duty_cycle):
        if self.pwm_started:
            self.pwm.ChangeDutyCycle(duty_cycle)

    def change_frequency(self, frequency, duty_cycle=50):
        if self.pwm_started:
            self.stop()
            self.pwm = GPIO.PWM(self.pin, frequency)
            self.pwm.start(duty_cycle)
            self.pwm_started = True
        self.frequency = frequency

    def stop(self):
        if self.pwm_started:
            self.pwm.stop()
            self.pwm_started = False

    def __del__(self):
        self.stop()
        GPIO.cleanup(self.pin)
