import socket
import pyproj
from gps3 import gps3
import sys
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore

import pyqtgraph as pg
from pyqtgraph import functions as fn
from time import sleep
endlat=[13.3483330]
endlon=[74.7920043]

g = pyproj.Geod(ellps='WGS84')
TCP_IP = '192.168.1.70'
TCP_PORT = 5005
transmit = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
transmit.connect((TCP_IP, TCP_PORT))
latitude,longitude,angle=transmit.recv(1024).split(',')
transmit.send("a")
print(latitude,longitude,angle)

def map1(x,in_min,in_max,out_min,out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class CenteredArrowItem(pg.ArrowItem):
    def setStyle(self, **opts):
        # http://www.pyqtgraph.org/documentation/_modules/pyqtgraph/graphicsItems/ArrowItem.html#ArrowItem.setStyle
        self.opts.update(opts)

        opt = dict([(k,self.opts[k]) for k in ['headLen', 'tipAngle', 'baseAngle', 'tailLen', 'tailWidth']])
        tr = QtGui.QTransform()
        path = fn.makeArrowPath(**opt)
        tr.rotate(self.opts['angle'])
        p = -path.boundingRect().center()
        tr.translate(p.x(), p.y())
        self.path = tr.map(path)
        self.setPath(self.path)

        self.setPen(fn.mkPen(self.opts['pen']))
        self.setBrush(fn.mkBrush(self.opts['brush']))

        if self.opts['pxMode']:
            self.setFlags(self.flags() | self.ItemIgnoresTransformations)
        else:
            self.setFlags(self.flags() & ~self.ItemIgnoresTransformations)

app = pg.QtGui.QApplication([])  
window = pg.GraphicsWindow(size=(800, 400))
window.setAntialiasing(True)
tracker = window.addPlot(row=0, col=0,title='GPS Position')
tracker.setGeometry(250,180,500,600)
arrow = CenteredArrowItem(angle=360, headLen=40, tipAngle=45, baseAngle=30)   
arrow1 = CenteredArrowItem(angle=360, headLen=40, tipAngle=45, baseAngle=30)
tracker.addItem(arrow)
tracker.addItem(arrow1)
tracker.hideAxis('bottom')
tracker.hideAxis('left')
p2 = window.addPlot(row=1, col=0)

p2.plot([endlon], [endlat],size=10, pen=None,symbol='o', symbolBrush=(255,0,0))
p2.setAspectLocked(lock=True, ratio=1)
#p2.setAutoPan(x=True, y=True)
x=[]
y=[]
proxy = QtGui.QGraphicsProxyWidget()
button = QtGui.QPushButton('Point 1')
button.move(20,80)
button.resize(20,80)
proxy.setWidget(button)
textbox = QtGui.QLineEdit()
proxy.setWidget(textbox)
p3 = window.addLayout(row=2, col=0)
p3.addItem(proxy,row=0,col=1)
p3.addItem(textbox,row=0,col=1)

def get_heading():
	global longitude, latitude, endlat, endlon
	(az12, az21, dist) = g.inv(longitude, latitude, endlon, endlat)
	if az12<0:
		az12=az12+360
	return az12, dist
def compassgps():
    global arrow,arrow1
    while True:
    	#compass()

    	latitude,longitude,angle=transmit.recv(1024).split(',')
    	transmit.send("a")
    	if not latitude: break
    	print(latitude,longitude,angle)
        y.append(latitude)
        x.append(longitude)
        s1 = p2.plot(x,y,size=10, pen=None,symbol='o', symbolBrush=(255,255,255,120))
        
    	#print(transmit.recv(1024).split(','))

        tracker.removeItem(arrow)
        tracker.removeItem(arrow1)
        p2.removeItem(arrow)
        adjusted_angle,distance = get_heading()
        arrow = CenteredArrowItem(angle=int(angle)/2+45, tipAngle=20, baseAngle=50, headLen=80, tailLen=None, brush=None)   
        arrow1 = CenteredArrowItem(angle=int(adjusted_angle)/2+45, tipAngle=20, baseAngle=50, headLen=80, tailLen=None, brush='w')

        tracker.setTitle(str(distance))
        tracker.addItem(arrow)
        tracker.addItem(arrow1)
        #arrow.setPos(float(longitude),float(latitude))
        #p2.addItem(arrow)
        app.processEvents()
        sleep(0.02)
        


#def compass():
compassgps()


       

