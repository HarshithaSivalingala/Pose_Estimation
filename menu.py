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

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1250, 1000))
        #self.setStyleSheet("background-color: grey;")
        self.setWindowTitle("Menu")
        self.Dumbbell()
        self.Squat()
        self.PushUp()
        self.Buttbridge()
        self.Lunges()
        self.Hydrant()
        self.Plank()
        self.SitUps()
        self.show()

    def Dumbbell(self):
        # Setting up a combo list
        self.comboBox1 = QComboBox(self)
        self.comboBox1.setGeometry(400, 200, 350, 50)
        list = ["Demo", "Exercise"]
        self.comboBox1.addItems(list)
        self.comboBox1.setEditable(True)
        font = QFont('Arial', 11)
        self.comboBox1.setFont(font)

        dumbbell = QPushButton('Dumbbell', self)
        dumbbell.setFont(QFont('Castellar', 20))
        dumbbell.setStyleSheet("QPushButton"
                               "{"
                               "background-color : lightgreen;"
                               "}"
                               "QPushButton::hover"
                               "{"
                               "background-color : lightyellow;"
                               "}")
        # dumbbell.setStyleSheet("background-color : yellow")
        dumbbell.pressed.connect(self.comboBox1.showPopup)
        dumbbell.resize(350, 50)
        dumbbell.move(400, 200)

        self.comboBox1.activated[str].connect(self.OnActivateDumbbell)

    def OnActivateDumbbell(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/dumbbell.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success:
                    cv2.imshow("Dumbbell lifting", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Dumbbell lifting", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.ActivateDumbbell()

    def Squat(self):
        # Setting up a combo list
        self.combo_box2 = QComboBox(self)
        self.combo_box2.setGeometry(400, 280, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box2.addItems(list)
        self.combo_box2.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box2.setFont(font)

        squat = QPushButton('Squats', self)
        squat.setFont(QFont('Castellar', 20))
        squat.setStyleSheet("QPushButton"
                            "{"
                            "background-color : lightgreen;"
                            "}"
                            "QPushButton::hover"
                            "{"
                            "background-color : lightyellow;"
                            "}")
        # squat.setStyleSheet("background-color : pink")
        squat.clicked.connect(self.combo_box2.showPopup)
        squat.resize(350, 50)
        squat.move(400, 280)

        self.combo_box2.activated[str].connect(self.OnActivateSquat)

    def OnActivateSquat(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/squats.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Squat", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Squat", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.ActivateSquat()

    def PushUp(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(400, 360, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        push = QPushButton('Push Ups', self)
        push.setFont(QFont('Castellar', 20))
        push.setStyleSheet("QPushButton"
                           "{"
                           "background-color : lightgreen;"
                           "}"
                           "QPushButton::hover"
                           "{"
                           "background-color : lightyellow;"
                           "}")
        # push.setStyleSheet("background-color : yellow")
        push.clicked.connect(self.combo_box.showPopup)
        push.resize(350, 50)
        push.move(400, 360)

        self.combo_box.activated[str].connect(self.OnActivatePushUp)

    def OnActivatePushUp(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/pushups.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Push Ups", img)
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Push Ups", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.ActivatePushUps()

    def Buttbridge(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(400, 440, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        buttBridge = QPushButton('Butt Bridge', self)
        buttBridge.setFont(QFont('Castellar', 20))
        buttBridge.setStyleSheet("QPushButton"
                                 "{"
                                 "background-color : lightgreen;"
                                 "}"
                                 "QPushButton::hover"
                                 "{"
                                 "background-color : lightyellow;"
                                 "}")
        # buttBridge.setStyleSheet("background-color : pink")
        buttBridge.clicked.connect(self.combo_box.showPopup)
        buttBridge.resize(350, 50)
        buttBridge.move(400, 440)

        self.combo_box.activated[str].connect(self.OnActivateButtBridge)

    def OnActivateButtBridge(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/buttbridge.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Butt Bridge", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Butt Bridge", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.ActivateButtBridge()

    def Lunges(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(400, 520, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        # creating a button
        lunges = QPushButton('Lunges', self)
        lunges.setFont(QFont('Castellar', 20))
        lunges.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightgreen;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : lightyellow;"
                             "}")
        # lunges.setStyleSheet("background-color : yellow")
        lunges.clicked.connect(self.combo_box.showPopup)
        lunges.resize(350, 50)
        lunges.move(400, 520)

        self.combo_box.activated[str].connect(self.OnActivateLunges)

    def OnActivateLunges(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/lunges.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Lunges", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Lunges", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.ActivateLunges()

    def Hydrant(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(400, 600, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        # Creating a button
        hydrant = QPushButton('Fire Hydrant', self)
        hydrant.setFont(QFont('Castellar', 20))
        hydrant.setStyleSheet("QPushButton"
                              "{"
                              "background-color : lightgreen;"
                              "}"
                              "QPushButton::hover"
                              "{"
                              "background-color : lightyellow;"
                              "}")
        # hydrant.setStyleSheet("background-color : pink")
        hydrant.clicked.connect(self.combo_box.showPopup)
        hydrant.resize(350, 50)
        hydrant.move(400, 600)

        self.combo_box.activated[str].connect(self.OnActivateHydrant)

    def OnActivateHydrant(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/fh.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Fire Hydrant", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Fire Hydrant", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.ActivateFireHydrant()

    def Plank(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(400, 680, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        # creating a button
        plank = QPushButton('Up/Down Plank', self)
        plank.setFont(QFont('Castellar', 20))
        plank.setStyleSheet("QPushButton"
                            "{"
                            "background-color : lightgreen;"
                            "}"
                            "QPushButton::hover"
                            "{"
                            "background-color : lightyellow;"
                            "}")
        # plank.setStyleSheet("background-color : yellow")
        plank.clicked.connect(self.combo_box.showPopup)
        plank.resize(350, 50)
        plank.move(400, 680)

        self.combo_box.activated[str].connect(self.OnActivatePlank)

    def OnActivatePlank(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/ud_plank.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Up/Down Plank", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Up/Down Plank", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.ActivatePlank()

    def SitUps(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(400, 760, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        Sit_ups = QPushButton('Sit Ups', self)
        Sit_ups.setFont(QFont('Castellar', 20))
        Sit_ups.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightgreen;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : lightyellow;"
                             "}")
        # Sit_ups.setStyleSheet("background-color : yellow")
        Sit_ups.clicked.connect(self.combo_box.showPopup)
        Sit_ups.resize(350, 50)
        Sit_ups.move(400, 760)

        self.combo_box.activated[str].connect(self.OnActivateSitUps)

    def OnActivateSitUps(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/crunches.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Sit_ups", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Sit_ups", cv2.WND_PROP_VISIBLE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.ActivateSitUps()

    def ActivateDumbbell(self):
        cap = cv2.VideoCapture("Dataset/curls.mp4")
        #cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0

        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))

            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                # Right Arm
                #angle = detector.findAngle(img, 12, 14, 16)

                # Left Arm
                angle = detector.findAngle(img, 11, 13, 15)
                per = np.interp(angle, (210, 310), (0, 100))

                # Check for the dumbbell curls
                if per == 100:
                    if dir == 0:
                        count += 0.5
                        dir = 1

                if per == 0:
                    if dir == 1:
                        count += 0.5
                        dir = 0

                target = 4

                if count == target:
                    win = po.Window()
                    cv2.waitKey(30000)

                cv2.rectangle(img, (0, 570), (175, 720), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (30, 700), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 20)

            cv2.imshow("Dumbbell", img)
            cv2.waitKey(1)

            if cv2.getWindowProperty("Dumbbell", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivateSquat(self):
        #cap = cv2.VideoCapture("Dataset/squat_main.mp4")
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


                cv2.putText(img, str("Squats Count: "), (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, color, 4)
                cv2.putText(img, str(int(count)), (280, 65), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

            cv2.imshow("Squats", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Squats", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivatePushUps(self):
        cap = cv2.VideoCapture(0)

        pTime = 0
        detector = pm.poseDetector()

        dir = 0
        count = 0
        while True:
            success, img = cap.read()
            img = detector.findPose(img, False)

            img = cv2.resize(img, (1400, 800))
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                angle = detector.findAngle(img, 11, 13, 15, True)

                perc = np.interp(angle, (208, 290), (0, 100))

                if perc == 100:
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if perc == 0:
                    if dir == 1:
                        count += 0.5
                        dir = 0

                cv2.putText(img, str("Count: "), (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 4)
                cv2.putText(img, str(int(count)), (170, 65), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

            cv2.imshow("Push Ups", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Push Ups", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivateButtBridge(self):
        cap = cv2.VideoCapture("Dataset/glute_bridge.mp4")
        #cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 720))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                angle = detector.findAngle(img, 11, 23, 25)
                per = np.interp(angle, (190, 220), (0, 100))

                color = (0, 0, 255)
                if per == 100:
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if per == 0:
                    if dir == 1:
                        count += 0.5
                        dir = 0

                cv2.putText(img, str("Count: "), (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 4)
                cv2.putText(img, str(int(count)), (170, 65), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

            cv2.imshow("Butt Bridge", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Butt Bridge", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivateFireHydrant(self):
        cap = cv2.VideoCapture("Dataset/fire_hydrant1.mp4")
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

            cv2.imshow("Fire Hydrant", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Fire Hydrant", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivateLunges(self):
        cap = cv2.VideoCapture("Dataset/lunge1.mp4")
        #cap = cv2.VideoCapture(0)
        detector = pm.poseDetector()
        count = 0
        dir = 0
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1300, 750))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)
            if len(lmList) != 0:
                # Left Leg
                leg2 = detector.findAngle(img, 23, 25, 27)
                per2 = np.interp(leg2, (190, 280), (0, 100))
                #Right leg
                leg1 = detector.findAngle(img, 24, 26, 28)
                per1 = np.interp(leg1, (190, 290), (0, 100))

                # Checking count
                color = (255, 0, 255)
                if (round(per1) in range(80, 100)) and (round(per2) in range(40, 75)):
                    color = (0, 0, 255)
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if (round(per1) in range(0, 10)) and (round(per2) in range(0, 10)):
                    color = (0, 0, 255)
                    if dir == 1:
                        count += 0.5
                        dir = 0

                cv2.putText(img, str("Count: "), (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 4)
                cv2.putText(img, str(int(count)), (170, 65), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

            cv2.imshow("Lunges", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Lunges", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivatePlank(self):
        cap = cv2.VideoCapture("Dataset/ud_plank1.mp4")
        #cap = cv2.VideoCapture(0)

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

                cv2.putText(img, str("Count: "), (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 4)
                cv2.putText(img, str(int(count)), (170, 65), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

            cv2.imshow("Up/Down Plank", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Up/Down Plank", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivateSitUps(self):
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

            cv2.imshow("Crunches", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Crunches", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    App = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())