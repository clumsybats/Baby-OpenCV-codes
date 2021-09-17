import cv2

cap = cv2.VideoCapture(0)
cap.set(3,720)          #width is 3
cap.set(4,1280)         #height is 4
cap.set(10,100)         #brigtness is 10

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break