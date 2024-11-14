# How to control a GPIO pin.

the class accepts two args:  
* Pin Number  
    * The Broadcom GPIO pin number  
* Pin Mode  
    * Input: 'IN', GPIO.IN  
    * Output: 'OUT', GPIO.OUT  


***
```Python
pin1 = pin(17, 'IN')
pin2 = pin(12, GPIO.IN)

pin3 = pin(5, 'OUT')
pin4 = pin(23, GPIO.OUT)
```
***

Here is a quick example:  
```Python
from RpiL import pin #import the 'pin' class from RpiL library
import time

pin1 = pin(24, 'IN') #set up a new pin

pin1.on()
time.sleep(1)
pin1.off()
time.sleep(2)
pin1.toggle()
time.sleep(1)

if pin1.value() in [GPIO.HIGH, 1]:
    pin1.off()
else:
    pin1.on()
```
That example would set up a GPIO pin in GPIO #24, turn the pin on, wait 1 second, turn the pin off, wait 2 seconds, toggle the pin (if its off, turn it on, and vice versa), then wait 1 second, then check whether the pin is on (GPIO.HIGH, 1), and if it is on, turn it off, and vice versa (kind of like a manual toggle just to demonstrate how the pin.value() function returns a value as GPIO.HIGH, GPIO.LOW, 1, 0.
