import sys
import cv2
import numpy as np
import time
import pose_module as pm
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox

import Popup as po

class Instructions(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(1250, 900))

        # setting title
        self.setWindowTitle("INSTRUCTIONS")
        img = QImage("Dataset/instructions.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(img))
        self.setPalette(palette)
        self.show()

App = QApplication(sys.argv)
#window = Instructions()
#sys.exit(App.exec())



