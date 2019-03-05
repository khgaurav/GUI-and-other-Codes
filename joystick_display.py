from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
import random
from time import sleep
import socket
import pyproj
from gps3 import gps3
import sys
import numpy as np
x=[]
y=[]
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.login_widget = LoginWidget(self)
        self.login_widget.button.clicked.connect(self.plotter)
        self.central_widget.addWidget(self.login_widget)

    def plotter(self):
        global x,y
        self.data = x
        self.curve = self.login_widget.plot.getPlotItem().plot()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.timer.start(0)

    def updater(self):
        global x,y
        latitude,longitude,angle=transmit.recv(1024).split(',')
        transmit.send("a")
        
        print(latitude,longitude,angle)
        y.append(latitude)
        x.append(longitude)
        self.data.append(self.x)
        self.curve.setData(self.data)

class LoginWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.button = QtGui.QPushButton('Start Plotting')
        layout.addWidget(self.button)
        self.plot = pg.PlotWidget()
        layout.addWidget(self.plot)
        self.setLayout(layout)

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
if __name__ == '__main__':
    g = pyproj.Geod(ellps='WGS84')
    TCP_IP = '192.168.1.70'
    TCP_PORT = 5005
    transmit = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transmit.connect((TCP_IP, TCP_PORT))
    latitude,longitude,angle=transmit.recv(1024).split(',')
    transmit.send("a")
    print(latitude,longitude,angle)
    y.append(latitude)
    x.append(longitude)    
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()