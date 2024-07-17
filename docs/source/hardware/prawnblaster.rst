Prawnblaster
============

The Prawnblaster is a microcontroller-based pseudoclock
based on the `Raspberry Pi Pico <https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html>`__.

This device supports up to 4 independent pseudoclock outputs, with up to 30,000 instructions distributed among the outputs.
It has a minimum resolution of 1 clock cycles and a minimum pulse width of 5 clock cycles.
Using the default internal 100 MHz clock, this represents a 10 ns timing resolution and a 50 ns minimum pulse width.
It also supports the ability to time the duration of waits internally.

For arbitrary digital trigger outputs, see the :doc:`PrawnDO <prawndo>` companion device.

The source code and pre-built firmware binaries are available from our `github repository <https://github.com/labscript-suite/PrawnBlaster>`_.