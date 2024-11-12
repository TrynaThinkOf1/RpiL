# RpiL/IR

import RPi.GPIO as GPIO
import pigpio
import time as t

GPIO.setmode(GPIO.BCM)

class IR_Receiver:
    def __init__(self, pin):
        self.pin = pin
        self.pi = pigpio.pi()

        if not self.pi.connected:
            raise Exception('could not connect to pigpio daemon')

        self.pi.set_mode(self.pin, pigpio.INPUT)
        self.code= []

        self.callback = self.pi.callback(self.pin, pigpio.EITHER_EDGE, self._callback)

    def _callback(self, pin, level, tick):
        self.code.append(tick)

    def _get_signal(self):
        t.sleep(0.1)

        if len(self.code) > 0:
            pulse_data = self.code
            self.code = []

            return pulse_data
        else:
            return None

    def read_signal(self, protocal="NEC"):
        pulse_data = self._get_signal()
        if pulse_data:
            if protocal == "NEC":
                return self._decode_nec(pulse_data)
            else:
                return ValueError("Unsupported protocol")
        return None

    def _decode_nec(self, pulse_data):
        bits = []
        for i in range(1, len(pulse_data), 2):
            high_time = pulse_data[i] - pulse_data[i-1]
            low_time = pulse_data[i+1] - pulse_data[i]
            if high_time > 900:
                bits.append(1)
            else:
                bits.append(0)

        hex_value = ''.join(str(b) for b in bits)
        hex_code = hex(int(hex_value, 2))
        return hex_code

    def __del__(self):
        self.callback.cancel()
        self.pi.stop()
        GPIO.cleanup([self.pin])

class IR_LED:
    def __init__(self, pin):
        self.pin = pin
        self.pi = pigpio.pi()

        if not self.pi.connected:
            raise Exception('could not connect to pigpio daemon')

        self.pi.set_mode(self.pin, pigpio.OUTPUT)

    def send_signal(self, hex_code, protocol="NEC", frequency=38000):
        if protocol == "NEC":
            data = self._hex_to_bin(hex_code)
            self._send_nec(data, frequency)
        else:
            raise Exception('unsupported protocol')

    def _send_nec(self, data, frequency=38000):
        self.pi.set_PWM_frequency(self.pin, frequency)
        self.pi.set_PWM_dutycycle(self.pin, 128)

        self._send_pulse(9000, 4500)

        for i in range(32):
            bit = (data >> (31 - i)) & 1
            if bit == 1:
                self._send_pulse(560, 1690)
            else:
                self._send_pulse(560, 560)

        self.pi.set_PWM_dutycycle(self.pin, 0)

    def _send_pulse(self, high_time, low_time):
        self.pi.gpio_trigger(self.pin, high_time, 1)
        t.sleep(low_time / 1000000.0)

    def _hex_to_bin(self, hex_code):
        hex_code = hex_code.lstrip("0x").zfill(8)
        bin_code = bin(int(hex_code, 16))[2:].zfill(32)
        return bin_code

    def __del__(self):
        self.pi.stop()
        GPIO.cleanup([self.pin])