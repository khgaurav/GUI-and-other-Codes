
import time
import math
import socket
import serial
def map1(x,in_min,in_max,out_min,out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
UDP_IP = '172.16.16.94' # this IP of my pc. When I want raspberry pi 2`s as a server, I replace it with its IP '169.254.54.195'
UDP_PORT = 5005
BUFFER_SIZE = 1024 # Normally 1024, but I want fast response

ser=serial.Serial('/dev/ttyUSB0',460800)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1)

#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((UDP_IP, UDP_PORT))
while(1):
    data=s.recvfrom(20)
    x_joy=int(data[0][4:8])
    y_joy=int(data[0][0:4])
    x_joy=map1(x_joy,1000,2000,0,16000)
    y_joy=map1(y_joy,1000,2000,0,16000)
    print(x_joy, y_joy)
    x1 = 0b00001111 & (x_joy >> 10)
    x1 |= 0b00100000

    x2 = 0b000011111 & (x_joy >> 5)
    x2 |= 0b01000000

    x3 = 0b00000000011111 & (x_joy >> 0)
    x3 |= 0b01100000

    y1 = 0b00001111 & (y_joy >> 10)
    y1 |= 0b10000000

    y2 = 0b000011111 & (y_joy >> 5)
    y2 |= 0b10100000

    y3 = 0b00000000011111 & (y_joy >> 0)
    y3 |= 0b11000000

    gear=5
    gear_pack = (0b00001111 & gear)
    gear_pack |= 0b00010000
    ser.write(chr(gear_pack))
    ser.write(chr(x1))
    ser.write(chr(x2))
    ser.write(chr(x3))
    ser.write(chr(y1))
    ser.write(chr(y2))
    ser.write(chr(y3))
    time.sleep(0.05)

s.close()

