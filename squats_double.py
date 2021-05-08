import cv2
import numpy as np
import time
import pose_module as pm

#cap = cv2.VideoCapture("Dataset/squat_double.mp4")
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
        per1 = np.interp(angle1, (180, 290), (0, 100))
        # Right Leg
        angle2 = detector.findAngle(img, 24, 26, 28)
        per2 = np.interp(angle2, (186, 250), (0, 100))
        bar = np.interp(angle1, (180, 290), (650, 100))  # (min, max)
        print(angle2, per2)

        # Checking count for squat
        color = (255, 0, 255)
        if (round(per1) in range(0, 2)) and (round(per2) in range(0, 4)):
            color = (0, 0, 255)
            if dir == 0:
                count += 0.5
                dir = 1
        if (round(per1) in range(70, 101)) and round(per2) in range(70, 101):
            color = (0, 0, 255)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)

        # creating bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)

        cv2.putText(img, str("Squats Count: "), (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, color, 4)
        cv2.putText(img, f'{int(per1)}%', (1130, 75), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)
        cv2.putText(img, str(int(count)), (280, 65), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    #cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)