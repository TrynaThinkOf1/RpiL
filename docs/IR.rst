How to Control an Infrared (IR) Receiver and IR LED
===================================================

The `IR_Receiver` and `IR_LED` classes in the `RpiL` library provide control for an infrared receiver and transmitter (IR LED) connected to the Raspberry Pi GPIO pins.

IR communication is commonly used in remote controls, where the IR receiver decodes incoming signals, and the IR LED can send signals. This setup supports the NEC protocol for transmitting and decoding IR data.

IR Receiver
-----------

The `IR_Receiver` class accepts one argument:

* **Pin Number**
    * The Broadcom GPIO pin number connected to the IR receiver.

The `IR_Receiver` class initializes the IR receiver, detects pulse data from incoming IR signals, and decodes them.

Here is an example of using `IR_Receiver`:

.. code-block:: Python

    from RpiL import IR_Receiver
    import time

    ir_receiver = IR_Receiver(17)  # Instantiate an IR receiver on GPIO pin 17

    while True:
        signal = ir_receiver.read_signal()  # Attempt to read an IR signal
        if signal:
            print(f"Received Signal: {signal}")
        time.sleep(1)  # Wait before reading again

This example sets up an IR receiver on GPIO pin 17, which reads and prints the received signal when one is detected.

IR Receiver Methods

* **read_signal(protocol="NEC")**
    * Reads the IR signal and decodes it based on the specified protocol (default is "NEC").

* **_decode_nec(pulse_data)**
    * Decodes NEC-formatted pulse data into a hexadecimal code.

IR LED
------

The `IR_LED` class accepts one argument:

* **Pin Number**
    * The Broadcom GPIO pin number connected to the IR LED.

The `IR_LED` class allows for sending IR signals using the NEC protocol. The `send_signal` method can be used to transmit hexadecimal codes as IR signals.

Here is an example of using `IR_LED`:

.. code-block:: Python

    from RpiL import IR_LED
    import time

    ir_led = IR_LED(27)  # Instantiate an IR LED on GPIO pin 27

    # Send a hexadecimal code using the NEC protocol
    ir_led.send_signal("0x1FE48B7")  # Example NEC signal in hex

In this example, an IR LED is created on GPIO pin 27 and used to send an IR signal with a specified hex code.

IR LED Methods

* **send_signal(hex_code, protocol="NEC", frequency=38000)**
    * Sends an IR signal using the specified protocol (default is NEC) and frequency.

* **_send_nec(data, frequency=38000)**
    * Sends NEC-formatted binary data as an IR signal, using the specified frequency in Hz.

Notes

Both `IR_Receiver` and `IR_LED` classes require the `pigpio` daemon to be running on the Raspberry Pi to control the IR hardware.

Cleanup

Both classes have a destructor method (`__del__`) that stops the `pigpio` connection and cleans up the specified GPIO pin.

