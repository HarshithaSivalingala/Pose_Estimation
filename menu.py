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

        buttBridge = QPushButton('Butt Bridge', self)
        buttBridge.clicked.connect(self.ActivateButtBridge)
        buttBridge.resize(100, 32)
        buttBridge.move(50, 90)

        lunges = QPushButton('Lunges', self)
        lunges.clicked.connect(self.ActivateLunges)
        lunges.resize(100, 32)
        lunges.move(200, 90)

        hydrant = QPushButton('Fire Hydrant', self)
        hydrant.clicked.connect(self.ActivateFireHydrant)
        hydrant.resize(100, 32)
        hydrant.move(350, 90)

        plank = QPushButton('Up/Down Plank', self)
        plank.clicked.connect(self.ActivatePlank)
        plank.resize(100, 32)
        plank.move(50, 130)

        crunch = QPushButton('crunches', self)
        crunch.clicked.connect(self.crunches)
        crunch.resize(100, 32)
        crunch.move(50, 130)

    def ActivateDumbbell(self):
        cap = cv2.VideoCapture("Dataset/curls.mp4")
        #cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))

            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                # Right Arm
                angle = detector.findAngle(img, 12, 14, 16)
                # Left Arm
                angle = detector.findAngle(img, 11, 13, 15)
                per = np.interp(angle, (210, 310), (0, 100))
                bar = np.interp(angle, (220, 310), (650, 100))  # (min, max)
                #print(angle, per)

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
                cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
                cv2.putText(img, f'{int(per)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

                # Curls Count
                cv2.rectangle(img, (0, 570), (175, 720), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (30, 700), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 20)
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            #cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

    def ActivateSquat(self):
        cap = cv2.VideoCapture("Dataset/squat_main.mp4")
        # cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))

            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                # Left Leg
                angle1 = detector.findAngle(img, 23, 25, 27)
                # Right Leg
                # angle2 = detector.findAngle(img, 24, 26, 28)
                per1 = np.interp(angle1, (165, 70), (0, 100))
                # per2 = np.interp(angle2, (180, 60), (0, 80))
                bar = np.interp(angle1, (165, 70), (650, 100))  # (min, max)
                #print(angle1, per1)

                # Checking count for squat
                color = (255, 0, 255)
                if per1 == 0:
                    color = (0, 0, 255)
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if per1 == 100:
                    color = (0, 0, 255)
                    if dir == 1:
                        count += 0.5
                        dir = 0

                # creating bar
                # cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                # cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)

                cv2.putText(img, str("Squats Count: "), (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, color, 4)
                # cv2.putText(img, f'{int(per1)}%', (1130, 75), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)
                cv2.putText(img, str(int(count)), (280, 65), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            # cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

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
            angle_rh = detector.findAngle(img, 14, 12, 24, True)
            # left hand
            angle_lh = detector.findAngle(img, 13, 11, 23, True)
            # right leg
            angle_rl = detector.findAngle(img, 23, 24, 26, True)
            angle_ll = detector.findAngle(img, 24, 23, 25, True)

            #perc_hand = np.interp(angle_ll, (180, 330), (0, 100))
            perc_leg = np.interp(angle_ll, (180, 330), (0, 100))

            print(angle_ll, perc)

            if perc == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if perc == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0

            cv2.putText(img, str(int(angle_ll)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            cv2.putText(img, str(int(count)), (100, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            cv2.imshow("Image", img)

            cv2.waitKey(1)

    def ActivateButtBridge(self):
        #cap = cv2.VideoCapture("Dataset/glute_bridge.mp4")
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
                angle = detector.findAngle(img, 11, 23, 25)
                per = np.interp(angle, (128, 180), (0, 100))
                print(angle, per)

            color = (0, 0, 255)
            if round(per) in range(98, 100):
                if dir == 0:
                    count += 0.5
                    dir = 1
            if round(per) in range(0, 10):
                if dir == 1:
                    count += 0.5
                    dir = 0

            #cv2.putText(img, str(int(angle)), (280, 200), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 6)
            cv2.putText(img, str(int(count)), (30, 700), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 20)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

    def ActivateFireHydrant(self):
        cap = cv2.VideoCapture("Dataset/fire_hydrant1.mp4")
        # cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)
            if len(lmList) != 0:
                leg1 = detector.findAngle(img, 23, 25, 27)
                leg = detector.findAngle(img, 24, 26, 28)
                per = np.interp(leg, (88, 295), (0, 100))
                # print(leg, per)

                # Checking count
                color = (255, 0, 255)
                if round(per) in range(95, 100):
                    color = (0, 0, 255)
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if round(per) in range(0, 10):
                    color = (0, 0, 255)
                    if dir == 1:
                        count += 0.5
                        dir = 0

                cv2.putText(img, str("Count: "), (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 4)
                cv2.putText(img, str(int(count)), (170, 65), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            # cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

    def ActivateLunges(self):
        cap = cv2.VideoCapture(0)
        detector = pm.poseDetector()

        dir = 0
        count = 0
        while True:
            success, img = cap.read()
            img = detector.findPose(img, False)
            img = cv2.resize(img, (1400, 800))

            lmList = detector.findPosition(img, False)
            # right leg
            r_angle = detector.findAngle(img, 24, 26, 28, True)
            # left leg
            l_angle = detector.findAngle(img, 23, 25, 27, True)
            perc = np.interp(r_angle, (170, 90), (0, 100))
            print(r_angle, perc)

            if perc == 100:
                if dir == 1:
                    count += 0.5
                    dir = 0
            if perc == 0:
                 if dir == 0:
                    count += 0.5
                    dir = 1

            cv2.putText(img, str(int(r_angle)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            cv2.putText(img, str(int(count)), (100, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            cv2.imshow("Image", img)

            cv2.waitKey(1)

    def ActivatePlank(self):
        #cap = cv2.VideoCapture("Dataset/ud_plank1.mp4")
        cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 800))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)
            if len(lmList) != 0:
                #hand1 = detector.findAngle(img, 11, 13, 15)
                hand = detector.findAngle(img, 12, 14, 16)
                per = np.interp(hand, (90, 180), (0, 100))
                #print(hand, per)

                if round(per) in range(96, 100):
                    color = (0, 0, 255)
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if round(per) in range(0, 8):
                    color = (0, 0, 255)
                    if dir == 1:
                        count += 0.5
                        dir = 0
                #print(count)

                cv2.putText(img, str("Count: "), (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 4)
                cv2.putText(img, str(int(count)), (170, 65), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            # cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

            cv2.imshow("Image", img)
            cv2.waitKey(1)


    def crunches(self):
        #cap = cv2.VideoCapture("")
        cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)
            if len(lmList) != 0:
                side1 = detector.findAngle(img, 12, 24, 26 )
                #side2 = detector.findAngle(img, 11, 23, 25)
                per = np.interp(side1, (60, 135), (0, 100))
                # print(side, per)

                # Checking count
                color = (255, 0, 255)
                if round(per) in range(95, 100):
                    color = (0, 0, 255)
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if round(per) in range(0, 10):
                    color = (0, 0, 255)
                    if dir == 1:
                        count += 0.5
                        dir = 0

                cv2.putText(img, str("Count: "), (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 4)
                cv2.putText(img, str(int(count)), (170, 65), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            # cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())