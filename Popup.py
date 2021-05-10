from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
#from menu import MainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(400, 200))

        # setting title
        self.setWindowTitle("You have a message!!!!")
        self.showbutton()
        self.show()

    def show_popup(self):
        print("POP")
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText("Congratulations! You have reached the target")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Do_it_again | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.popup_button)
        returnValue = msg.exec_()
        if returnValue == QMessageBox.Cancel:
         #   MainWindow.ActivateDumbbell()
            print("clicked")

    def popup_button(self, i):
        print(i.text())

    def showbutton(self):
        # cv2.putText(img, "yes", (30, 700), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 20)
        pushButton = QPushButton("Congratulations !!!", self)
        pushButton.pressed.connect(self.show_popup)
        pushButton.resize(350, 60)
        pushButton.move(20, 60)
        pushButton.setFont(QFont('Castellar', 15))
        pushButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color : yellow;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : lightyellow;"
                             "}")



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
#window = Window()

# start the app
#sys.exit(App.exec())