

import math
import serial
ser=serial.Serial('/dev/ttyUSB1',38400)

while 1:
    ser.write('s')
