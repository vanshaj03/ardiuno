import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector()
offset = 20
while True:
    succ, img = cap.read()
    faces, img = detector.findFaces(img)
    if faces.any():
        face = faces[0]
        x,y,w,h = face[0], face[1], face[2], face[3]
        x_start, y_start = x-offset, y-offset
        x_end, y_end = x+w+offset, y+h+offset
        imgcrop = img[y_start:y_end, x_start:x_end]
        cv2.imshow("ImageCrop", imgcrop)
    cv2.imshow("Image", img) 
    cv2.waitKey(1)