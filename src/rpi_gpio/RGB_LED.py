import RPi.GPIO as GPIO
import time as t
import threading

GPIO.setmode(GPIO.BCM)

class RGB_LED:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin

        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)

        self.red_pwm = GPIO.PWM(self.red_pin, 100)
        self.green_pwm = GPIO.PWM(self.green_pin, 100)
        self.blue_pwm = GPIO.PWM(self.blue_pin, 100)

        self.red_pwm.start(0)
        self.green_pwm.start(0)
        self.blue_pwm.start(0)

        self.running = False
        self.rainbow_thread = None

    def set_color(self, hex_color):
        """Set the RGB LED to a specific hex color."""
        try:
            hex_color = hex_color.lstrip('#')
            red = int(hex_color[0:2], 16)
            green = int(hex_color[2:4], 16)
            blue = int(hex_color[4:6], 16)

            # Convert RGB values (0-255) to PWM duty cycle (0-100)
            self.red_pwm.ChangeDutyCycle(red / 255 * 100)
            self.green_pwm.ChangeDutyCycle(green / 255 * 100)
            self.blue_pwm.ChangeDutyCycle(blue / 255 * 100)
        except ValueError:
            print("Invalid hex color format. Please use a hex string (e.g., '#FF00FF').")

    def rainbow_cycle_sequence(self, wait=0.05):
        """Cycle through colors in a rainbow effect until stopped."""
        self.running = True
        position = 0  # Start at the beginning of the color wheel
        while self.running:
            red, green, blue = self.wheel(position % 256)
            self.red_pwm.ChangeDutyCycle(red / 255 * 100)
            self.green_pwm.ChangeDutyCycle(green / 255 * 100)
            self.blue_pwm.ChangeDutyCycle(blue / 255 * 100)
            t.sleep(wait)
            position += 1

    def rainbow_cycle(self, wait=0.05):
        """Start the rainbow cycle in a separate thread if not already running."""
        if self.rainbow_thread is None or not self.rainbow_thread.is_alive():
            self.rainbow_thread = threading.Thread(target=self.rainbow_cycle_sequence, args=(wait,))
            self.rainbow_thread.start()

    def stop_rainbow_cycle(self):
        """Stop the rainbow cycle."""
        self.running = False
        self.off()

    @staticmethod
    def wheel(position=0):
        """Generate rainbow colors across 0-255 positions."""
        if position < 85:
            return (position * 3, 255 - position * 3, 0)
        elif position < 170:
            position -= 85
            return (255 - position * 3, 0, position * 3)
        else:
            position -= 170
            return (0, position * 3, 255 - position * 3)

    def off(self):
        """Turn off the RGB LED."""
        self.red_pwm.ChangeDutyCycle(0)
        self.green_pwm.ChangeDutyCycle(0)
        self.blue_pwm.ChangeDutyCycle(0)

    def __del__(self):
        """Cleanup GPIO pins when the object is deleted."""
        self.off()
        self.red_pwm.stop()
        self.green_pwm.stop()
        self.blue_pwm.stop()
        if self.rainbow_thread and self.rainbow_thread.is_alive():
            self.rainbow_thread.join()
        GPIO.cleanup(self.red_pin, self.green_pin, self.blue_pin)
