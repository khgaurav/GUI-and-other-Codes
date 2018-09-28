from pygame import joystick
import pygame
import math
import serial
ser=serial.Serial('/dev/ttyUSB0',9600)

while(1):
	print(ser.write('a'.encode()))
