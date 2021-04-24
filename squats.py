import cv2
import numpy as np
import time
import pose_module as pm

#cap = cv2.VideoCapture("Dataset/squat1.mp4")
cap = cv2.VideoCapture(0)

detector = pm.poseDetector()
count = 0
dir = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (900, 800))

    img = detector.findPose(img, True)
    lmList = detector.findPosition(img, True)

    if len(lmList) != 0:
        # Left Leg
        angle1 = detector.findAngle(img, 23, 25, 27)
        # Right Leg
        angle2 = detector.findAngle(img, 24, 26, 28)
        per1 = np.interp(angle1, (180, 260), (0, 100))
        per2 = np.interp(angle2, (180, 260), (0, 100))
        cv2.putText(img, str(int(angle1)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        #bar = np.interp(angle, (220, 310), (650, 100))  # (min, max)

        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per1 == 100 and per2 == 100:
            color = (0, 0, 255)
            if dir == 0:
                count += 0.5
                dir = 1
        if per1 == 0 and per2:
            color = (0, 0, 255)
            if dir == 1:
                count += 0.5
                dir = 0

        # Drawing the box --> Bar
        #cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        #cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        #cv2.putText(img, f'{int(per)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

        #Curls Count
        #cv2.rectangle(img, (0, 570), (175, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (30, 700), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 20)

    cv2.imshow("Image", img)
    cv2.waitKey(1)