from pygame import joystick
import pygame
import math
import serial
ser=serial.Serial('/dev/ttyUSB1',38400)

while(1):
	print(ser.read(12))
