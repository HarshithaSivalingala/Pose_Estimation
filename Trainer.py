import cv2
import numpy as np
import time
import pose_module as pm

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
    lmList = detector.findPosition(img, True)

    if len(lmList) != 0:
        # Right Arm
        angle = detector.findAngle(img, 12, 14, 16)
        # Left Arm
        angle = detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))  # (min, max)
        print(angle, per)

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

        #Curls Count
        cv2.rectangle(img, (0, 570), (175, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (30, 700), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 20)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)