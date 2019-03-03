

import math
import serial
ser=serial.Serial('/dev/ttyUSB0',38400)

while 1:
    ser.write('m4x4999y4999z')
