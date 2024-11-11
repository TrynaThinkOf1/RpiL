# RpiL/Motor_Driver

import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Motor_Driver:
    def __init__(self, in1=0, in2=0, ena=0, in3=0, in4=0, enb=0):
        """This uses GPIO pin-number on the pi.\n
        This class is for the L298N Motor Driver"""
        self.in1 = int(in1)
        self.in2 = int(in2)
        self.ena = int(ena)

        self.in3 = int(in3)
        self.in4 = int(in4)
        self.enb = int(enb)

        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.output(self.in2, GPIO.LOW)

        GPIO.setup(self.ena, GPIO.OUT)

        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.setup(self.in4, GPIO.OUT)
        GPIO.output(self.in4, GPIO.LOW)

        GPIO.setup(self.enb, GPIO.OUT)

        self.en_a = GPIO.PWM(self.ena, 100)
        self.en_a.start(0)

        self.en_b = GPIO.PWM(self.enb, 100)
        self.en_b.start(0)

    def forward(self, speed=90):
        """Turns IN1 and IN3 on"""
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        self.en_a.ChangeDutyCycle(speed)

        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)
        self.en_b.ChangeDutyCycle(speed)

    def backward(self, speed=75):
        """Turns IN2 and IN4 on"""
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        self.en_a.ChangeDutyCycle(speed)

        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)
        self.en_b.ChangeDutyCycle(speed)

    def turn_right(self, speed=90):
        """Turns IN2 and IN3 on"""
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        self.en_a.ChangeDutyCycle(speed)

        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)
        self.en_b.ChangeDutyCycle(speed)

    def turn_left(self, speed=90):
        """Turns IN1 and IN4 on"""
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        self.en_a.ChangeDutyCycle(speed)

        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)
        self.en_b.ChangeDutyCycle(speed)

    def stop(self):
        """Turns all IN# off and turns off ena and enb PWM"""
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        self.en_a.stop()

        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
        self.en_b.stop()

    def __del__(self):
        self.stop()
        GPIO.cleanup(self.in1, self.in2, self.ena, self.in3, self.in4, self.enb)
