# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(1265, 1, 100, 100))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("logo1.png"))
        self.Logo.setObjectName("Logo")
        self.Plotting = MyWidget(self.centralwidget)
        self.Plotting.setGeometry(QtCore.QRect(6, 107, 1361, 661))
        self.Plotting.setStyleSheet("")
        self.Plotting.setObjectName("Plotting")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Latitude_1 = QtWidgets.QLineEdit(self.widget)
        self.Latitude_1.setText("")
        self.Latitude_1.setObjectName("Latitude_1")
        self.gridLayout.addWidget(self.Latitude_1, 0, 0, 1, 1)
        self.Latitude_2 = QtWidgets.QLineEdit(self.widget)
        self.Latitude_2.setText("")
        self.Latitude_2.setObjectName("Latitude_2")
        self.gridLayout.addWidget(self.Latitude_2, 0, 1, 1, 1)
        self.Latitude_3 = QtWidgets.QLineEdit(self.widget)
        self.Latitude_3.setText("")
        self.Latitude_3.setObjectName("Latitude_3")
        self.gridLayout.addWidget(self.Latitude_3, 0, 2, 1, 1)
        self.Latitude_4 = QtWidgets.QLineEdit(self.widget)
        self.Latitude_4.setText("")
        self.Latitude_4.setObjectName("Latitude_4")
        self.gridLayout.addWidget(self.Latitude_4, 0, 3, 1, 1)
        self.Latitude_5 = QtWidgets.QLineEdit(self.widget)
        self.Latitude_5.setText("")
        self.Latitude_5.setObjectName("Latitude_5")
        self.gridLayout.addWidget(self.Latitude_5, 0, 4, 1, 1)
        self.Latitude_6 = QtWidgets.QLineEdit(self.widget)
        self.Latitude_6.setText("")
        self.Latitude_6.setObjectName("Latitude_6")
        self.gridLayout.addWidget(self.Latitude_6, 0, 5, 1, 1)
        self.Longitude_1 = QtWidgets.QLineEdit(self.widget)
        self.Longitude_1.setText("")
        self.Longitude_1.setObjectName("Longitude_1")
        self.gridLayout.addWidget(self.Longitude_1, 1, 0, 1, 1)
        self.Longitude_2 = QtWidgets.QLineEdit(self.widget)
        self.Longitude_2.setText("")
        self.Longitude_2.setObjectName("Longitude_2")
        self.gridLayout.addWidget(self.Longitude_2, 1, 1, 1, 1)
        self.Longitude_3 = QtWidgets.QLineEdit(self.widget)
        self.Longitude_3.setText("")
        self.Longitude_3.setObjectName("Longitude_3")
        self.gridLayout.addWidget(self.Longitude_3, 1, 2, 1, 1)
        self.Longitude_4 = QtWidgets.QLineEdit(self.widget)
        self.Longitude_4.setText("")
        self.Longitude_4.setObjectName("Longitude_4")
        self.gridLayout.addWidget(self.Longitude_4, 1, 3, 1, 1)
        self.Longitude_5 = QtWidgets.QLineEdit(self.widget)
        self.Longitude_5.setText("")
        self.Longitude_5.setObjectName("Longitude_5")
        self.gridLayout.addWidget(self.Longitude_5, 1, 4, 1, 1)
        self.Longitude_6 = QtWidgets.QLineEdit(self.widget)
        self.Longitude_6.setText("")
        self.Longitude_6.setObjectName("Longitude_6")
        self.gridLayout.addWidget(self.Longitude_6, 1, 5, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(7, 80, 197, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PlotButton = QtWidgets.QPushButton(self.widget1)
        self.PlotButton.setObjectName("PlotButton")
        self.horizontalLayout.addWidget(self.PlotButton)
        self.chgEnd = QtWidgets.QPushButton(self.widget1)
        self.chgEnd.setObjectName("chgEnd")
        self.horizontalLayout.addWidget(self.chgEnd)
        self.Plotting.raise_()
        self.Logo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Latitude_1.setPlaceholderText(_translate("MainWindow", "Latitude"))
        self.Latitude_2.setPlaceholderText(_translate("MainWindow", "Latitude"))
        self.Latitude_3.setPlaceholderText(_translate("MainWindow", "Latitude"))
        self.Latitude_4.setPlaceholderText(_translate("MainWindow", "Latitude"))
        self.Latitude_5.setPlaceholderText(_translate("MainWindow", "Latitude"))
        self.Latitude_6.setPlaceholderText(_translate("MainWindow", "Latitude"))
        self.Longitude_1.setPlaceholderText(_translate("MainWindow", "Longitude"))
        self.Longitude_2.setPlaceholderText(_translate("MainWindow", "Longitude"))
        self.Longitude_3.setPlaceholderText(_translate("MainWindow", "Longitude"))
        self.Longitude_4.setPlaceholderText(_translate("MainWindow", "Longitude"))
        self.Longitude_5.setPlaceholderText(_translate("MainWindow", "Longitude"))
        self.Longitude_6.setPlaceholderText(_translate("MainWindow", "Longitude"))
        self.PlotButton.setText(_translate("MainWindow", "Plot"))
        self.chgEnd.setText(_translate("MainWindow", "Next Co-ods"))

from RPi_data import MyWidget
import xz_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
