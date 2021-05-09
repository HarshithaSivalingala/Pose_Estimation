import sys
import cv2
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class references():
    def openDumbbell(self):
        cap = cv2.VideoCapture("Dataset/curls.mp4")
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))
            cv2.imshow("Dumbbell lifting", img)
            cv2.waitKey(40)
            if cv2.getWindowProperty("Dumbbell lifting", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def openHydrant(self):
        cap = cv2.VideoCapture("Dataset/fire_hydrant1.mp4")
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))
            cv2.imshow("Fire Hydrant", img)
            cv2.waitKey(40)
            if cv2.getWindowProperty("Fire Hydrant", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def openPlank(self):
        cap = cv2.VideoCapture("Dataset/ud_plank1.mp4")
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))
            cv2.imshow("Up/Down Plank", img)
            cv2.waitKey(40)
            if cv2.getWindowProperty("Up/Down Plank", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def openLunges(self):
        cap = cv2.VideoCapture("Dataset/lunge1.mp4")
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))
            cv2.imshow("Lunges", img)
            cv2.waitKey(40)
            if cv2.getWindowProperty("Lunges", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def openButtBridge(self):
        cap = cv2.VideoCapture("Dataset/butt_bridge.mp4")
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))
            cv2.imshow("Butt Bridge", img)
            cv2.waitKey(40)
            if cv2.getWindowProperty("Butt Bridge", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def openPushUps(self):
        cap = cv2.VideoCapture("Dataset/pushUps1.mp4")
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))
            cv2.imshow("Push Ups", img)
            cv2.waitKey(40)
            if cv2.getWindowProperty("Push Ups", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def openSquat(self):
        cap = cv2.VideoCapture("Dataset/squat_main.mp4")
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))
            cv2.imshow("Squats", img)
            cv2.waitKey(40)
            if cv2.getWindowProperty("Squats", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    refWin = references()
    #refWin.openDumbbell()
    sys.exit(app.exec_())