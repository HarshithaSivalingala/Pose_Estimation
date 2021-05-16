import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QLabel
import pose_module
import Popup
import menu as osScript

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home Workout")
        img = QImage("Dataset/homeworkout.jpeg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(img))
        self.setPalette(palette)
        self.setMinimumSize(QSize(1250, 900))

        self.UiComponents()
        self.show()

    def UiComponents(self):
        start = QPushButton("Let's Begin", self)
        start.resize(200, 60)
        start.move(650, 600)
        start.setFont(QFont('Times', 20))
        start.setStyleSheet("QPushButton"
                                  "{"
                                  "background-color : white;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "background-color : lightyellow;"
                                  "}")
        start.clicked.connect(self.launch_script)


    def launch_script(self):
        self.hide()
        self.panel = osScript.MainWindow()
        self.panel.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())