Installation
============

To install the **RpiL** library, follow the instructions below based on your system.

Installing on Non-Raspberry Pi Systems
--------------------------------------

For non-Raspberry Pi systems, you can install **RpiL** using the following command:

.. code-block:: bash

    pip3 install RpiL

This will install the library for general use on systems other than the Raspberry Pi.

Installing on a Raspberry Pi
----------------------------

For Raspberry Pi systems, you need to install the library with Raspberry Pi-specific dependencies by using the following command:

.. code-block:: bash

    pip3 install RpiL[rpi]

This will install the library along with the necessary dependencies specifically required for Raspberry Pi hardware, enabling full compatibility with GPIO and other Raspberry Pi features.
