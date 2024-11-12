# RpiL/PIR

import RPi.GPIO as GPIO
import threading
import time as t

GPIO.setmode(GPIO.BCM)

class PIR:
    def __init__(self, pin):
        self.pin = pin
        self.motion_detected_flag = False
        self.motion_thread = None

        GPIO.setup(pin, GPIO.IN)

        self.motion_thread = threading.Thread(target=self._monitor_motion)
        self.motion_thread.daemon = True
        self.motion_thread.start()

    def _monitor_motion(self):
        while True:
            if GPIO.input(self.pin):
                self.motion_detected_flag = True
            else:
                self.motion_detected_flag = False
            t.sleep(0.25)

    def motion_detected(self):
        return self.motion_detected_flag

    def wait_for_motion(self):
        """Returns a Boolean when motion is detected"""
        while not self.motion_detected_flag:
            t.sleep(0.25)
        return True

    def __del__(self):
        GPIO.cleanup([self.pin])