import cv2, time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in face:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
        img[y:y + h, x:x + w] = cv2.medianBlur(img[y:y + h, x:x + w], 35)

    cv2.imshow('faceblur', frame)
    key = cv2.waitKey(1)

    if key == ord('0'):
        break

video.release()
cv2.destroyAllWindows