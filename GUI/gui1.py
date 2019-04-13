# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 510)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mast_camera = App(self.centralwidget)
        self.mast_camera.setGeometry(QtCore.QRect(0, 0, 320, 240))
        self.mast_camera.setObjectName("mast_camera")
        self.axis_1 = axis_1(self.centralwidget)
        self.axis_1.setGeometry(QtCore.QRect(320, 0, 320, 240))
        self.axis_1.setObjectName("axis_1")
        self.axis_2 = axis_2(self.centralwidget)
        self.axis_2.setGeometry(QtCore.QRect(0, 240, 320, 240))
        self.axis_2.setObjectName("axis_2")
        self.axis_3 = axis_3(self.centralwidget)
        self.axis_3.setGeometry(QtCore.QRect(320, 240, 320, 240))
        self.axis_3.setObjectName("axis_3")
        self.motorcode = motor_Code(self.centralwidget)
        self.motorcode.setGeometry(QtCore.QRect(640, 9, 320, 231))
        self.motorcode.setObjectName("motorcode")
        self.axis_4 = axis_4(self.centralwidget)
        self.axis_4.setGeometry(QtCore.QRect(640, 240, 320, 240))
        self.axis_4.setObjectName("axis_4")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(860, 0, 100, 100))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("logo1.png"))
        self.Logo.setObjectName("Logo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

from axis_1 import axis_1
from axis_2 import axis_2
from axis_3 import axis_3
from axis_4 import axis_4
from cam8 import App
from tcp_send import motor_Code
