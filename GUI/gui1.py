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
        MainWindow.resize(800, 600)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.webView = QtWebKitWidgets.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(0, 0, 300, 200))
        self.webView.setWhatsThis("")
        self.webView.setUrl(QtCore.QUrl("19"))
        self.webView.setZoomFactor(0.5)
        self.webView.scroll(0, 10000)
        self.webView.setObjectName("webView")
        self.webView_2 = QtWebKitWidgets.QWebView(self.centralwidget)
        self.webView_2.setGeometry(QtCore.QRect(10, 220, 300, 200))
        self.webView_2.setWhatsThis("")
        self.webView_2.setUrl(QtCore.QUrl("https://www.facebook.com/?gws_rd=ssl"))
        self.webView_2.setZoomFactor(0.5)
        self.webView_2.setObjectName("webView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.webView_2.setAccessibleDescription(_translate("MainWindow", "40"))

from PyQt5 import QtWebKitWidgets
