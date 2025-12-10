PrawnDO
=======

The PrawnDO is a microcontroller-based arbitrary digital pattern generator
based on the `Raspberry Pi Pico <https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html>`__.

This device has 16 digital outputs, with up to 30,000 instructions.
It has a minimum resolution of 1 clock cycles and a minimum pulse width of 5 clock cycles.
Using the default internal 100 MHz clock, this represents a 10 ns timing resolution and a 50 ns minimum pulse width.
It is designed to be attached directly to the output of a :doc:`Prawnblaster <prawnblaster>`.
When combined in this way, the Prawnblaster/PrawnDO provide a complete digital pulse specification for experimental timing and triggering.

The source code and pre-built firmware binaries are available from our `github repository <https://github.com/labscript-suite/prawn_digital_output>`_.