import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QLabel
import pose_module
import Popup
import menu as osScript
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtMultimedia import QSound
from pygame import mixer
import instructions as script

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
        play = QPushButton("", self)
        play.setGeometry(1070, 40, 60, 60)
        play.setStyleSheet("border-radius : 30")
        play.clicked.connect(self.play_music)

        stop = QPushButton("", self)
        stop.setGeometry(1160, 40, 60, 60)
        stop.setStyleSheet("border-radius : 30")
        stop.setFont(QFont('Times', 7))
        stop.clicked.connect(self.stop_music)



        start = QPushButton("Let's Begin", self)
        start.resize(300, 70)
        start.move(650, 600)
        start.setFont(QFont('Garamond', 20))
        start.setStyleSheet("QPushButton"
                                  "{"
                                  "background-color : white;"
                                  "}"
                                  "QPushButton::hover"
                                  "{"
                                  "background-color : lightyellow;"
                                  "}")
        start.clicked.connect(self.launch_script)
        start = QPushButton("Instructions", self)
        start.resize(300, 70)
        start.move(650, 700)
        start.setFont(QFont('Garamond', 20))
        start.setStyleSheet("QPushButton"
                            "{"
                            "background-color : white;"
                            "}"
                            "QPushButton::hover"
                            "{"
                            "background-color : lightyellow;"
                            "}")
        start.clicked.connect(self.instructions)

    def launch_script(self):
        self.hide()
        self.panel = osScript.MainWindow()
        self.panel.show()
    def instructions(self):
        self.panel = script.Instructions()
        self.panel.show()

    def play_music(self):
        mixer.init()
        mixer.music.set_volume(0.7)
        mixer.music.load("Dataset/sound2.wav")
        mixer.music.play()

    def stop_music(self):
        mixer.music.stop()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    #sound = QSound("Dataset\sound2.wav")
    #sound.play()
    window = Window()
    sys.exit(App.exec())