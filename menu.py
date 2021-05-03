import sys
import cv2
import numpy as np
import time
import pose_module as pm
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 500))
        self.setWindowTitle("Menu")

        dumbbell = QPushButton('Dumbbell', self)
        dumbbell.clicked.connect(self.ActivateDumbbell)
        dumbbell.resize(100, 32)
        dumbbell.move(50, 50)

        squat = QPushButton('Squats', self)
        squat.clicked.connect(self.ActivateSquat)
        squat.resize(100, 32)
        squat.move(200, 50)

        push = QPushButton('Push Ups', self)
        push.clicked.connect(self.ActivatePushUps)
        push.resize(100, 32)
        push.move(350, 50)

        jump = QPushButton('Jumping Jacks', self)
        jump.clicked.connect(self.ActivateJumpingJacks)
        jump.resize(100, 32)
        jump.move(50, 90)

    def ActivateDumbbell(self):
        detector = pm.poseDetector()
        # cap = cv2.VideoCapture("Dataset/curls.mp4")
        cap = cv2.VideoCapture(0)
        dir = 0
        count = 0

        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1000, 800))

            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                # Right Arm
                #angle = detector.findAngle(img, 12, 14, 16)
                # Left Arm
                angle = detector.findAngle(img, 11, 13, 15)
                per = np.interp(angle, (210, 310), (0, 100))
                bar = np.interp(angle, (220, 310), (650, 100))  # (min, max)

                # Check for the dumbbell curls
                color = (255, 0, 255)
                if per == 100:
                    color = (0, 0, 255)
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if per == 0:
                    color = (0, 0, 255)
                    if dir == 1:
                        count += 0.5
                        dir = 0
                # Drawing the box --> Bar
                cv2.rectangle(img, (1100, 200), (1175, 650), color, 3)
                #cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
                cv2.putText(img, f'{int(per)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

                #Curls Count
                cv2.rectangle(img, (0, 570), (250, 760), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (30, 700), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 20)

            cv2.imshow("image", img)
            cv2.waitKey(1)

    def ActivateSquat(self):
        #cap = cv2.VideoCapture("Dataset/squat2.mp4")
        cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1000, 800))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                # Left Leg
                angle1 = detector.findAngle(img, 23, 25, 27)
                per1 = np.interp(angle1, (165, 70), (0, 100))

                # bar = np.interp(angle, (220, 310), (650, 100))  # (min, max)

                # Check for the dumbbell curls
                color = (255, 0, 255)
                if per1 == 100:
                    color = (0, 0, 255)
                    if dir == 1:
                        count += 0.5
                        dir = 0
                if per1 == 0:
                    color = (0, 0, 255)
                    if dir == 0:
                        count += 0.5
                        dir = 1

                cv2.putText(img, str(int(count)), (280, 200), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 6)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

    def ActivatePushUps(self):
        cap = cv2.VideoCapture("Dataset/pushUps2.mp4")

        pTime = 0
        detector = pm.poseDetector()

        dir = 0
        count = 0
        while True:
            success, img = cap.read()
            img = detector.findPose(img, False)

            img = cv2.resize(img, (1400, 800))

            lmList = detector.findPosition(img, False)
            angle = detector.findAngle(img, 11, 13, 15, True)

            perc = np.interp(angle, (204, 305), (0, 100))
            # print(angle, perc)

            if perc == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if perc == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0

            cv2.putText(img, str(int(count)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            # cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            cv2.imshow("Image", img)

            cv2.waitKey(1)

    def ActivateJumpingJacks(self):
        cap = cv2.VideoCapture(0)
        detector = pm.poseDetector()

        dir = 0
        count = 0
        while True:
            success, img = cap.read()
            img = detector.findPose(img, False)

            img = cv2.resize(img, (1400, 800))

            lmList = detector.findPosition(img, False)
            #right hand
            angle_hr = detector.findAngle(img, 14, 12, 24, True)
            # left hand
            angle_hl = detector.findAngle(img, 13, 11, 23, True)

            perc = np.interp(angle_hr, (200, 345), (0, 100))
            print(angle_hr, perc)

            if perc == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if perc == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0

            cv2.putText(img, str(int(angle_hr)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            cv2.putText(img, str(int(count)), (100, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            cv2.imshow("Image", img)

            cv2.waitKey(1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())