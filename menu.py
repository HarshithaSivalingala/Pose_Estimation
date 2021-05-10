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
import trial as tr

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 500))
        self.setWindowTitle("Menu")
        self.Dumbbell()
        self.Squat()
        self.PushUp()
        self.Buttbridge()
        self.Lunges()
        self.Hydrant()
        self.Plank()
        self.Crunch()


        self.show()


    def Dumbbell(self):
        # Setting up a combo list
        self.comboBox1 = QComboBox(self)
        self.comboBox1.setGeometry(50, 50, 185, 32)
        list = ["Demo", "Camera"]
        self.comboBox1.addItems(list)
        self.comboBox1.setEditable(True)
        font = QFont('Arial', 11)
        self.comboBox1.setFont(font)

       #role1 = self.comboBox1.setItemData(0)

        # Creating a main button
        dumbbell = QPushButton('Dumbbell', self)
        dumbbell.setFont(QFont('Castellar', 15))
        dumbbell.setStyleSheet("QPushButton"
                               "{"
                               "background-color : yellow;"
                               "}"
                               "QPushButton::hover"
                               "{"
                               "background-color : lightyellow;"
                               "}")
        # dumbbell.setStyleSheet("background-color : yellow")
        dumbbell.pressed.connect(self.comboBox1.showPopup)
        dumbbell.resize(185, 32)
        dumbbell.move(50, 50)


        self.comboBox1.activated[str].connect(self.OnActivateDumbbell)

    def OnActivateDumbbell(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/curls.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Image", img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        elif text == "Camera":
            self.ActivateDumbbell()


    def Squat(self):
        # Setting up a combo list
        self.combo_box2 = QComboBox(self)
        self.combo_box2.setGeometry(50, 100, 150, 32)
        list = ["Demo", "Camera"]
        self.combo_box2.addItems(list)
        self.combo_box2.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box2.setFont(font)

        squat = QPushButton('Squats', self)
        squat.setFont(QFont('Castellar', 15))
        squat.setStyleSheet("QPushButton"
                            "{"
                            "background-color : pink;"
                            "}"
                            "QPushButton::hover"
                            "{"
                            "background-color : lightpink;"
                            "}")
        # squat.setStyleSheet("background-color : pink")
        squat.clicked.connect(self.combo_box2.showPopup)
        squat.resize(150, 32)
        squat.move(50, 100)

        self.combo_box2.activated[str].connect(self.OnActivateSquat)

    def OnActivateSquat(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/squat_main.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Image", img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        elif text == "Camera":
            self.ActivateSquat()

    def PushUp(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(50, 150, 170, 32)
        list = ["Demo", "Camera"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        push = QPushButton('Push Ups', self)
        push.setFont(QFont('Castellar', 15))
        push.setStyleSheet("QPushButton"
                           "{"
                           "background-color : yellow;"
                           "}"
                           "QPushButton::hover"
                           "{"
                           "background-color : lightyellow;"
                           "}")
        # push.setStyleSheet("background-color : yellow")
        push.clicked.connect(self.combo_box.showPopup)
        push.resize(170, 32)
        push.move(50, 150)

        self.combo_box.activated[str].connect(self.OnActivatePushUp)

    def OnActivatePushUp(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/pushUps1.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Image", img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        elif text == "Camera":
            self.ActivatePushUps()

    def Buttbridge(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(50, 200, 225, 32)
        list = ["Demo", "Camera"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        buttBridge = QPushButton('Butt Bridge', self)
        buttBridge.setFont(QFont('Castellar', 15))
        buttBridge.setStyleSheet("QPushButton"
                                 "{"
                                 "background-color : pink;"
                                 "}"
                                 "QPushButton::hover"
                                 "{"
                                 "background-color : lightpink;"
                                 "}")
        # buttBridge.setStyleSheet("background-color : pink")
        buttBridge.clicked.connect(self.combo_box.showPopup)
        buttBridge.resize(225, 32)
        buttBridge.move(50, 200)

        self.combo_box.activated[str].connect(self.OnActivateButtBridge)

    def OnActivateButtBridge(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/glute_bridge.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Image", img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        elif text == "Camera":
            self.ActivateButtBridge()

    def Lunges(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(50, 250, 150, 32)
        list = ["Demo", "Camera"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        # creating a button
        lunges = QPushButton('Lunges', self)
        lunges.setFont(QFont('Castellar', 15))
        lunges.setStyleSheet("QPushButton"
                             "{"
                             "background-color : yellow;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : lightyellow;"
                             "}")
        # lunges.setStyleSheet("background-color : yellow")
        lunges.clicked.connect(self.combo_box.showPopup)
        lunges.resize(150, 32)
        lunges.move(50, 250)

        self.combo_box.activated[str].connect(self.OnActivateLunges)

    def OnActivateLunges(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/lunge1.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Image", img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        elif text == "Camera":
            self.ActivateLunges()

    def Hydrant(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(50, 300, 250, 32)
        list = ["Demo", "Camera"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        # Creating a button
        hydrant = QPushButton('Fire Hydrant', self)
        hydrant.setFont(QFont('Castellar', 15))
        hydrant.setStyleSheet("QPushButton"
                              "{"
                              "background-color : pink;"
                              "}"
                              "QPushButton::hover"
                              "{"
                              "background-color : lightpink;"
                              "}")
        # hydrant.setStyleSheet("background-color : pink")
        hydrant.clicked.connect(self.combo_box.showPopup)
        hydrant.resize(250, 32)
        hydrant.move(50, 300)

        self.combo_box.activated[str].connect(self.OnActivateHydrant)

    def OnActivateHydrant(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/fire_hydrant1.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Image", img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        elif text == "Camera":
            self.ActivateFireHydrant()

    def Plank(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(50, 350, 280, 32)
        list = ["Demo", "Camera"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        # creating a button
        plank = QPushButton('Up/Down Plank', self)
        plank.setFont(QFont('Castellar', 15))
        plank.setStyleSheet("QPushButton"
                            "{"
                            "background-color : yellow;"
                            "}"
                            "QPushButton::hover"
                            "{"
                            "background-color : lightyellow;"
                            "}")
        # plank.setStyleSheet("background-color : yellow")
        plank.clicked.connect(self.combo_box.showPopup)
        plank.resize(280, 32)
        plank.move(50, 350)

        self.combo_box.activated[str].connect(self.OnActivatePlank)

    def OnActivatePlank(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/ud_plank1.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Image", img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        elif text == "Camera":
            self.ActivatePlank()

    def Crunch(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(50, 400, 190, 32)
        list = ["Demo", "Camera"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        # creating a button
        crunch = QPushButton('crunches', self)
        crunch.setFont(QFont('Castellar', 15))
        crunch.setStyleSheet("QPushButton"
                             "{"
                             "background-color : yellow;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : lightyellow;"
                             "}")
        # plank.setStyleSheet("background-color : yellow")
        crunch.clicked.connect(self.combo_box.showPopup)
        crunch.resize(190, 32)
        crunch.move(50, 400)

        self.combo_box.activated[str].connect(self.OnActivateCrunch)

    def OnActivateCrunch(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Dataset/skipping1.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1300, 720))
                if success == True:
                    cv2.imshow("Image", img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        elif text == "Camera":
            self.Activatecrunches()

        # Pose estimating workouts

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
                print(count)

                target = 5

                if count == target:
                    #self.pushButton = QtWidgets.QPushButton("You have a msg")
                    #cv2.rectangle(img, (450, 300), (950, 400), (255, 255, 255), cv2.FILLED)
                    #cv2.putText(img, "You have reached the target", (460, 350), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                    win = tr.Window()
                    cv2.waitKey(30000)


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
                #print(leg2, per2)
                #Right leg
                leg1 = detector.findAngle(img, 24, 26, 28)
                per1 = np.interp(leg1, (190, 290), (0, 100))
                #print(leg1, per1, leg2, per2)

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
                ##print(count)

                cv2.putText(img, str("Count: "), (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 4)
                cv2.putText(img, str(int(count)), (170, 65), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            # cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

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

    def Activatecrunches(self):
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
    App = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())