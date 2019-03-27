import sys
import cv2
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
import datetime


class App(QWidget):
    def __init__(self, parent=None):
        super(App, self).__init__(parent=parent)
        self.title = 'PyQt5 Video'
        
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(640,480)
        # create a label
        # create a label
        self.label = QLabel(self)        
        self.label.resize(640, 480)
        self.label1 = QLabel(self)
        self.label1.move(580, 620)

        self.mastCam = QPushButton(self)
        self.mastCam.setObjectName("mastCam")
        self.mastCam.setText("Mast Camera")
        self.mastCam.clicked.connect(self.startThread)
        
    def startThread(self):
        self.th = Thread(self)
        self.th.changePixmap.connect(self.label.setPixmap)
        self.th.changeLabel.connect(self.label1.setText)
        self.th.start()

    def closeEvent(self, event):
        self.th.stop()
        QWidget.closeEvent(self, event)

class Thread(QThread):
    changePixmap = pyqtSignal(QPixmap)
    changeLabel = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.isRunning = True

    def run(self):
        cap = cv2.VideoCapture('rtsp://192.168.1.8/user=admin&password=&channel=1&stream=0.sdp?real_stream--rtp-caching=1')

        while self.isRunning:

            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                now = datetime.datetime.now()
                sec = now.second
                self.changeLabel.emit(str(sec))
        btn.clicked.connect(self.buttonClicked)
    def buttonClicked(self):
        os.system(cmd)
        QtCore.QCoreApplication.instance().quit()


    def stop(self):
        self.isRunning = False
        self.quit()
        self.wait()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     ex.show()
#     sys.exit(app.exec_())
