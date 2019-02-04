

import math
import serial
ser=serial.Serial('/dev/ttyUSB0',38400)

while(1):
	ser.write(input())
	ser.write(input())
	print(ser.read())
	print(ser.read())
	print(ser.read())
