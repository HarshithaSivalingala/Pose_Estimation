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
        img = QImage("Dataset/menu3.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(img))
        self.setPalette(palette)
        self.setMinimumSize(QSize(1250, 900))
        #self.setStyleSheet("background-color: grey;")
        self.setWindowTitle("Menu")
        self.Dumbbell()
        self.Squat()
        # self.PushUp()
        self.Buttbridge()
        # self.Hydrant()
        self.Plank()
        self.SitUps()
        self.show()

    def Dumbbell(self):
        # Setting up a combo list
        self.comboBox1 = QComboBox(self)
        self.comboBox1.setGeometry(200, 200, 350, 50)
        list = ["Demo", "Exercise"]
        self.comboBox1.addItems(list)
        self.comboBox1.setEditable(True)
        font = QFont('Arial', 11)
        self.comboBox1.setFont(font)

        dumbbell = QPushButton('Dumbbell', self)
        dumbbell.setFont(QFont('Castellar', 17))
        dumbbell.setStyleSheet("QPushButton"
                               "{"
                               "background-color : black; color: white"
                               "}"
                               "QPushButton::hover"
                               "{"
                               "background-color : darkgrey;"
                               "}")
        # dumbbell.setStyleSheet("background-color : yellow")
        dumbbell.pressed.connect(self.comboBox1.showPopup)
        dumbbell.resize(350, 50)
        dumbbell.move(200, 200)

        self.comboBox1.activated[str].connect(self.OnActivateDumbbell)

    def OnActivateDumbbell(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Resources/dumbbell1.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1250, 900))
                if success:
                    cv2.imshow("Dumbbell lifting", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Dumbbell lifting", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.hide()
            self.ActivateDumbbell()

    def Squat(self):
        # Setting up a combo list
        self.combo_box2 = QComboBox(self)
        self.combo_box2.setGeometry(200, 280, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box2.addItems(list)
        self.combo_box2.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box2.setFont(font)

        squat = QPushButton('Squats', self)
        squat.setFont(QFont('Castellar', 17))
        squat.setStyleSheet("QPushButton"
                            "{"
                            "background-color : black; color: white"
                            "}"
                            "QPushButton::hover"
                            "{"
                            "background-color : darkgrey;"
                            "}")
        # squat.setStyleSheet("background-color : pink")
        squat.clicked.connect(self.combo_box2.showPopup)
        squat.resize(350, 50)
        squat.move(200, 280)

        self.combo_box2.activated[str].connect(self.OnActivateSquat)

    def OnActivateSquat(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Resources/squats1.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1250, 900))
                if success == True:
                    cv2.imshow("Squat", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Squat", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.hide()
            self.ActivateSquat()

    def PushUp(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(200, 360, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        push = QPushButton('Push Ups', self)
        push.setFont(QFont('Castellar', 17))
        push.setStyleSheet("QPushButton"
                           "{"
                           "background-color : black; color: white"
                           "}"
                           "QPushButton::hover"
                           "{"
                           "background-color : darkgray;"
                           "}")

        push.clicked.connect(self.combo_box.showPopup)
        push.resize(350, 50)
        push.move(200, 360)

        self.combo_box.activated[str].connect(self.OnActivatePushUp)

    def OnActivatePushUp(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Resources/pushups1.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1250, 900))
                if success == True:
                    cv2.imshow("Push Ups", img)
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Push Ups", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.hide()
            self.ActivatePushUps()

    def Buttbridge(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(200, 360, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        buttBridge = QPushButton('Butt Bridge', self)
        buttBridge.setFont(QFont('Castellar', 17))
        buttBridge.setStyleSheet("QPushButton"
                                 "{"
                                 "background-color : black; color: white"
                                 "}"
                                 "QPushButton::hover"
                                 "{"
                                 "background-color : darkgrey;"
                                 "}")
        # buttBridge.setStyleSheet("background-color : pink")
        buttBridge.clicked.connect(self.combo_box.showPopup)
        buttBridge.resize(350, 50)
        buttBridge.move(200, 360)

        self.combo_box.activated[str].connect(self.OnActivateButtBridge)

    def OnActivateButtBridge(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Resources/butt bridge1.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1250, 900))
                if success == True:
                    cv2.imshow("Butt Bridge", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Butt Bridge", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.hide()
            self.ActivateButtBridge()

    def Hydrant(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(200, 520, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        # Creating a button
        hydrant = QPushButton('Fire Hydrant Right', self)
        hydrant.setFont(QFont('Castellar', 17))
        hydrant.setStyleSheet("QPushButton"
                              "{"
                              "background-color : black; color: white"
                              "}"
                              "QPushButton::hover"
                              "{"
                              "background-color : darkgrey;"
                              "}")
        # hydrant.setStyleSheet("background-color : pink")
        hydrant.clicked.connect(self.combo_box.showPopup)
        hydrant.resize(350, 50)
        hydrant.move(200, 520)

        self.combo_box.activated[str].connect(self.OnActivateHydrant)

    def OnActivateHydrant(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Resources/fire hydrant1.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1250, 900))
                if success == True:
                    cv2.imshow("Fire Hydrant", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Fire Hydrant", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.hide()
            self.ActivateFireHydrant()

    def Plank(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(200, 440, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        # creating a button
        plank = QPushButton('Up/Down Plank', self)
        plank.setFont(QFont('Castellar', 17))
        plank.setStyleSheet("QPushButton"
                            "{"
                            "background-color : black; color: white"
                            "}"
                            "QPushButton::hover"
                            "{"
                            "background-color : darkgrey;"
                            "}")
        # plank.setStyleSheet("background-color : yellow")
        plank.clicked.connect(self.combo_box.showPopup)
        plank.resize(350, 50)
        plank.move(200, 440)

        self.combo_box.activated[str].connect(self.OnActivatePlank)

    def OnActivatePlank(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Resources/up and down1.mp4")
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1250, 900))
                if success == True:
                    cv2.imshow("Up/Down Plank", img)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                if cv2.getWindowProperty("Up/Down Plank", cv2.WND_PROP_AUTOSIZE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif text == "Exercise":
            self.hide()
            self.ActivatePlank()

    def SitUps(self):
        # Setting up a combo list
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(200, 520, 350, 50)
        list = ["Demo", "Exercise"]
        self.combo_box.addItems(list)
        self.combo_box.setEditable(True)
        font = QFont('Arial', 11)
        self.combo_box.setFont(font)

        Sit_ups = QPushButton('Sit Ups', self)
        Sit_ups.setFont(QFont('Castellar', 17))
        #Sit_ups.setStyleSheet("border : 2px solid black; border - radius: 25px;")
        Sit_ups.setStyleSheet("QPushButton"
                             "{"
                             "background-color : black; color: white"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : darkgrey;"
                             "}")
        # Sit_ups.setStyleSheet("background-color : yellow")
        Sit_ups.clicked.connect(self.combo_box.showPopup)
        Sit_ups.resize(350, 50)
        Sit_ups.move(200, 520)

        self.combo_box.activated[str].connect(self.OnActivateSitUps)

    def OnActivateSitUps(self, text):
        if text == "Demo":
            cap = cv2.VideoCapture("Resources/situps1.mp4" )
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1250, 900))
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

    def displayCount(self, count, img, target):
        cv2.rectangle(img, (50, 60), (450, 80), (240, 240, 240), 70)
        cv2.putText(img, str("Count: "), (30, 100), cv2.FONT_HERSHEY_PLAIN, 6, (0, 0, 0), 5)
        cv2.putText(img, str(count), (370, 105), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 0), 5)
        cv2.rectangle(img, (1200, 60), (1700, 80), (240, 240, 240), 70)
        cv2.putText(img, str("Target: "), (1200, 100), cv2.FONT_HERSHEY_PLAIN, 6, (0, 0, 0), 5)
        cv2.putText(img, str(target), (1600, 105), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 0), 5)

    def draw_text(self,frame, text, x, y, color=(0, 0, 0), thickness=15, size=10):
        if x is not None and y is not None:
            cv2.putText(frame, text, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, size, color, thickness)

    def timer(self):
        cap = cv2.VideoCapture(0)
        init_time = time.time()
        test_timeout = init_time + 16
        final_timeout = init_time + 16
        counter_timeout_text = init_time + 1
        counter_timeout = init_time + 1
        counter = 15
        while (cap.isOpened()):
            ret, frame = cap.read()
            frame = cv2.resize(frame, (1900, 1100))
            if ret == True:
                center_x = int(frame.shape[0] / 0.8)
                center_y = int(frame.shape[0] / 3.6)
                if(time.time() > counter_timeout_text and time.time() < test_timeout):
                    self.draw_text(frame, str(counter), center_x, center_y)
                    counter_timeout_text += 0.03333
                if (time.time() > counter_timeout and time.time() < test_timeout):
                    counter -= 1
                    counter_timeout += 1
                cv2.imshow('Timer', frame)
                if (cv2.waitKey(1) & 0xFF == ord('q')) or (time.time() > final_timeout):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivateDumbbell(self):
        self.timer()
        #cap = cv2.VideoCapture("Dataset/curls.mp4")
        cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0

        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1800, 1000))

            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                # Right Arm
                angle_r = detector.findAngle(img, 12, 14, 16)

                # Left Arm
                angle_l = detector.findAngle(img, 11, 13, 15)
                per_l = np.interp(angle_l, (210, 310), (0, 100))
                per_r = np.interp(angle_r, (210, 310), (0, 100))

                # Check for the dumbbell curls
                if per_l == 100 and per_r == 100:
                    if dir == 0:
                        count += 0.5
                        dir = 1

                if per_l == 0 and per_r == 0:
                    if dir == 1:
                        count += 0.5
                        dir = 0

            target = 5

            if count == target:
                win = po.Window()
                cv2.waitKey(30000)

            self.displayCount(int(count), img, target)

            cv2.imshow("Dumbbell", img)
            cv2.waitKey(1)

            if cv2.getWindowProperty("Dumbbell", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivateSquat(self):
        #self.timer()
        cap = cv2.VideoCapture("Dataset/squat_main.mp4")
        #cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0

        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1800, 1000))

            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                # Left Leg
                angle_l = detector.findAngle(img, 23, 25, 27)
                # Right Leg
                #angle_r = detector.findAngle(img, 24, 26, 28)
                per_l = np.interp(angle_l, (165, 70), (0, 100))
                #per_r = np.interp(angle_r, (165, 70), (0, 80))
                print(angle_l, per_l)

                # Checking count for squat
                if round(angle_l) in range(150, 170):
                    if dir == 0:
                        count += 0.5
                        dir = 1

                if round(angle_l) in range(50, 80):
                    if dir == 1:
                        count += 0.5
                        dir = 0

            target = 3

            if count == target:
                win = po.Window()
                cv2.waitKey(30000)
            self.displayCount(int(count), img, str(target))

            cv2.imshow("Squats", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Squats", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivatePushUps(self):
        #self.timer()
        cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()

        dir = 0
        count = 0
        while True:
            success, img = cap.read()
            img = detector.findPose(img, False)

            img = cv2.resize(img, (1900, 1000))
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                angle_l = detector.findAngle(img, 11, 13, 15)
                #angle_r = detector.findAngle(img, 12, 14, 16)

                perc_l = np.interp(angle_l, (208, 290), (0, 100))
                #perc_r = np.interp(angle_r, (208, 290), (0, 100))

                if perc_l == 100 and perc_r == 100:
                    if dir == 0:
                        count += 0.5
                        dir = 1

                if perc_l == 0 and perc_r == 0:
                    if dir == 1:
                        count += 0.5
                        dir = 0

            target = 5

            if count == target:
                win = po.Window()
                cv2.waitKey(30000)

            self.displayCount(int(count), img, target)

            cv2.imshow("Push Ups", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Push Ups", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivateButtBridge(self):
        self.timer()
        #cap = cv2.VideoCapture("Dataset/glute_bridge.mp4")
        cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1800, 1000))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                angle = detector.findAngle(img, 12, 24, 26)
                #per = np.interp(angle, (190, 222), (0, 100))

                if round(angle) in range(170, 190):
                    if dir == 0:
                        count += 0.5
                        dir = 1

                if round(angle) in range(200, 230):
                    if dir == 1:
                        count += 0.5
                        dir = 0

            target = 5

            if count == target:
                win = po.Window()
                cv2.waitKey(30000)

            self.displayCount(int(count), img, target)

            cv2.imshow("Butt Bridge", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Butt Bridge", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivateFireHydrant(self):
        self.timer()
        #cap = cv2.VideoCapture("Dataset/fire_hydrant1.mp4")
        cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1900, 1000))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                leg_l = detector.findAngle(img, 23, 25, 27)
                leg_r = detector.findAngle(img, 24, 26, 28)
                per_r = np.interp(leg_r, (88, 295), (0, 100))

                # Checking count
                if round(leg_r) in range(280, 300):
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if round(leg_r) in range(70, 130):
                    color = (0, 0, 255)
                    if dir == 1:
                        count += 0.5
                        dir = 0

            target = 10

            if count == target:
                win = po.Window()
                cv2.waitKey(30000)

            self.displayCount(int(count), img, target)

            cv2.imshow("Fire Hydrant", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Fire Hydrant", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivatePlank(self):
        self.timer()
        cap = cv2.VideoCapture("Dataset/ud_plank1.mp4")
        #cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1900, 1000))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)
            if len(lmList) != 0:
                #hand1 = detector.findAngle(img, 11, 13, 15)
                hand = detector.findAngle(img, 12, 14, 16)
                per = np.interp(hand, (90, 180), (0, 100))
                #print(hand, per)

                if round(hand) in range(150, 190):
                    color = (0, 0, 255)
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if round(hand) in range(70, 90):
                    color = (0, 0, 255)
                    if dir == 1:
                        count += 0.5
                        dir = 0

            target = 5

            if count == target:
                win = po.Window()
                cv2.waitKey(30000)
            self.displayCount(int(count), img, target)

            cv2.imshow("Up/Down Plank", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("Up/Down Plank", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

    def ActivateSitUps(self):
        self.timer()
        #cap = cv2.VideoCapture("")
        cap = cv2.VideoCapture(0)

        detector = pm.poseDetector()
        count = 0
        dir = 0
        pTime = 0
        while True:
            success, img = cap.read()
            img = cv2.resize(img, (1900, 1000))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)

            if len(lmList) != 0:
                rightside = detector.findAngle(img, 12, 24, 26 )
                #leftside = detector.findAngle(img, 11, 23, 25)
                per = np.interp(rightside, (200, 300), (0, 100))
                #print(rightside, per)

                # Checking count
                color = (255, 0, 255)
                if round(rightside) in range(290, 310):
                    color = (0, 0, 255)
                    if dir == 0:
                        count += 0.5
                        dir = 1
                if round(rightside) in range(180,200):
                    color = (0, 0, 255)
                    if dir == 1:
                        count += 0.5
                        dir = 0

            target = 5

            if count == target:
                win = po.Window()
                cv2.waitKey(30000)

            self.displayCount(int(count), img, target)

            cv2.imshow("SitUps", img)
            cv2.waitKey(1)
            if cv2.getWindowProperty("SitUps", cv2.WND_PROP_AUTOSIZE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    App = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())