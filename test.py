from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg
import numpy as np
import socket
import pyproj
from pyqtgraph import functions as fn
from gps3 import gps3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import cv2
from PIL import Image
g = pyproj.Geod(ellps='WGS84')
TCP_IP = '192.168.1.70'
TCP_PORT = 5005
transmit = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
transmit.connect((TCP_IP, TCP_PORT))
img = Image.open( "logo.tiff" )
img = img.rotate(-90)  
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img.load()
logo = np.asarray( img, dtype="int32" )


x=[]
y=[]
endlat=[13.3504820,13.3502770,13.3497990]
endlon=[74.7914680,74.7911590,74.7912990]
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
class MyWidget(pg.GraphicsWindow):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent=parent)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(100) # in milliseconds
        self.timer.start()
        self.timer.timeout.connect(self.onNewData)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        self.plotItem = self.addPlot(title="GPS Plotting")
        self.plotItem.setAspectLocked(lock=True, ratio=1)
        self.plotDataItem = self.plotItem.plot([], size=1, pen=None,symbol='o', symbolBrush=(255,255,255,120))
        self.plotDataItem1 = self.plotItem.plot(endlon,endlat, size=10, pen=None,symbol='o', symbolBrush=(255,0,0,120))

        self.arrow = CenteredArrowItem(angle=0, tipAngle=40, baseAngle=50, headLen=80, tailLen=None, brush=None)

        self.proxy = QtGui.QGraphicsProxyWidget()
        self.im1 = pg.ImageView()
        self.im1.setImage(logo)
        self.proxy.setWidget(self.im1)
        self.addItem(self.proxy)
        self.im1.ui.histogram.hide()
        self.im1.ui.menuBtn.hide()
        self.im1.ui.roiBtn.hide()

        self.proxy1 = QtGui.QGraphicsProxyWidget()
        self.textbox = QLineEdit(self)
        self.proxy1.setWidget(self.textbox)
        self.addItem(self.proxy1)        


    def setData(self, x, y):
        self.plotDataItem.setData(x, y)


    def onNewData(self):
      global x,y
      latitude,longitude,angle=transmit.recv(1024).split(',')
      transmit.send("a")
      print(latitude,longitude,angle)        
      y.append(latitude)
      x.append(longitude)
      self.setData(x, y)
      self.plotItem.removeItem(self.arrow)
      self.arrow = CenteredArrowItem(angle=int(angle)/2+45, tipAngle=40, baseAngle=40, headLen=40, tailLen=None, brush=None)
      
      self.arrow.setPos(float(longitude),float(latitude))        
      self.plotItem.addItem(self.arrow)


def main():
    app = QtWidgets.QApplication([])

    pg.setConfigOptions(antialias=True) # True seems to work as well

    win = MyWidget()
    win.show()
    win.resize(800,600) 
    
    win.raise_()
    app.exec_()

if __name__ == "__main__":
    main()