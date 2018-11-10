#!/usr/bin/python
from Tkinter import *
import cv2
import os


def digitalcam9():
	os.system("idle-python2.7 -r cam9.py &")

def digitalcam10():
	os.system("idle-python2.7 -r cam10.py &")


def analogcams():
	os.system("idle-python2.7 -r analogcams.py &")


a = Tk()
a.title("MRM") 																																											
Button(a, text="DigitalCam9", command = digitalcam9, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 0)
Button(a, text="DigitalCam10", command = digitalcam10, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 1)
Button(a, text="AnalogCams", command = analogcams, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 4)


def motorcode():
	os.system("xdotool windowmove 54525987 0 0 &")
	
	os.system("idle-python2.7 -r tcp_send.py &")
	

	
Button(a, text="Motorcode", command = motorcode, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 0,column=2)

def autonomous():
	 os.system("sudo idle-python2.7 -r autnomRec.py &")


Button(a, text="Autonomous", command = autonomous, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 0,column=3)
a.mainloop()

