from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QLabel
import cv2
import pose_module
import Popup
import menu as osScript

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        img = QImage("Dataset/last.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(img))
        self.setPalette(palette)
        self.setMinimumSize(QSize(600, 400))

        # setting title
        self.setWindowTitle("YAYYY!!! You have reached the target")
        self.showbutton()
        self.show()

    def showbutton(self):
        pushButton1 = QPushButton("Back", self)
        #pushButton.pressed.connect(self.show_popup)
        pushButton1.resize(120, 40)
        pushButton1.move(250, 250)
        pushButton1.setFont(QFont('Times', 11))
        pushButton1.setStyleSheet("QPushButton"
                             "{"
                             "background-color : yellow;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : lightyellow;"
                             "}")
        pushButton1.pressed.connect(self.launch_script)

        pushButton2 = QPushButton("Quit", self)
        # pushButton.pressed.connect(self.show_popup)
        pushButton2.resize(120, 40)
        pushButton2.move(430, 250)
        pushButton2.setFont(QFont('Times', 11))
        pushButton2.setStyleSheet("QPushButton"
                                  "{"
                                  "background-color : yellow;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "background-color : lightyellow;"
                                  "}")
        pushButton2.pressed.connect(self.AppClose)

    def AppClose(self):
        self.close()
        cv2.destroyAllWindows()

    def launch_script(self):
        self.close()
        cv2.destroyAllWindows()
        self.panel = osScript.MainWindow()
        self.panel.show()



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
#window = Window()

# start the app
#sys.exit(App.exec())
