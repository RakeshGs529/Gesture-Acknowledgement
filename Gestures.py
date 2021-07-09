import cv2
import numpy as np
import pyautogui as pyautogui

import Hand_module as htm
import time

wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7
#########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        #print(y1,y2)

        fingers = detector.fingersUp()
        print(fingers)

        if fingers == [0,0,0,0,0]:
            print("closed")
            cv2.putText(img, f'Closed', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
        elif fingers == [1,1,1,1,1]:
            print("opened")
            cv2.putText(img, f'Open', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
        elif fingers == [0,1,0,0,1]:
            print("Spider Man")
            cv2.putText(img, f'Spider Man', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
        elif fingers == [0,1,1,0,0]:
            print("Peace")
            cv2.putText(img, f'Peace', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
        elif fingers == [1, 1, 0, 0, 0]:
            print("Two")
            cv2.putText(img, f'Two', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
        elif fingers == [0, 1, 0, 0, 0]:
            print("One")
            cv2.putText(img, f'One', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

        #cv2.putText(img, f'Eg:', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)





    cv2.imshow("Image", img)
    cv2.waitKey(1)