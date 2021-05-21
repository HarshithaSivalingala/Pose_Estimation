from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QLabel
import cv2

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: lightpink;")
        self.setMinimumSize(QSize(400, 200))

        # setting title
        self.setWindowTitle("You have a message")

        self.label = QLabel('Congratulations!!!', self)
        #self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 15))
        self.label.resize(200, 50)  # (width, height)
        self.label.move(100, 10)

        self.label1 = QLabel("You have reached the target", self)
        self.label1.setFont(QFont('Arial', 12))
        self.label1.resize(400, 30)
        self.label1.move(80, 50)

        self.showbutton()
        self.show()

    def showbutton(self):
        pushButton1 = QPushButton(" Do It Again", self)
        #pushButton.pressed.connect(self.show_popup)
        pushButton1.resize(120, 40)
        pushButton1.move(45, 100)
        pushButton1.setFont(QFont('Times', 10))
        pushButton1.setStyleSheet("QPushButton"
                             "{"
                             "background-color : yellow;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : lightyellow;"
                             "}")

        pushButton2 = QPushButton("Finish", self)
        # pushButton.pressed.connect(self.show_popup)
        pushButton2.resize(120, 40)
        pushButton2.move(230, 100)
        pushButton2.setFont(QFont('Times', 10))
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



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
#window = Window()

# start the app
#sys.exit(App.exec())