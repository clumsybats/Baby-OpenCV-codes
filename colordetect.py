import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#red    
    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask = red_mask)

#blue
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126,255,255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask = blue_mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)

    if cv2.waitKey(1) & 0xFF == ord('0'):
        break