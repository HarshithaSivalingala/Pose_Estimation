import cv2
import numpy as np
import time
import pose_module as pm

cap = cv2.VideoCapture("Dataset/Fire_hydrant.mp4")
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

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
    cv.destroyAllWindows()