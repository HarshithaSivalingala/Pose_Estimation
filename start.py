
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QLabel
import pose_module
import Popup
import menu as osScript

#from menu import MainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Home Workout")
        img = QImage("Dataset/homeworkout.jpeg")
        # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(img))
        self.setPalette(palette)
        #self.setStyleSheet("QWidget {background-image: url(Dataset/homeworkout.jpeg)}")
        self.setMinimumSize(QSize(1250, 900))

        # calling method
        self.UiComponents()
        # showing all the widgets
        self.show()
    # method for widgets
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
        self.panel = osScript.MainWindow()
        self.panel.show()



if __name__ == "__main__":
# create pyqt5 app
    App = QApplication(sys.argv)

# create the instance of our Window
    window = Window()

# start the app
    sys.exit(App.exec())