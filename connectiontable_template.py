from labscript import *
from labscript_devices.PulseBlaster import PulseBlaster

PulseBlaster('pulseblaster_0')

if __name__ == '__main__':
    start()
    stop(1)