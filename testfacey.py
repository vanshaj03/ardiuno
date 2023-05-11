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
        x,y,w,h = face['bbox']
        imgcrop = img[y-offset:y+h+offset , x-offset:x+w+offset+5]
        cv2.imshow("ImageCrop", imgcrop)
    cv2.imshow("Image", img) 
    cv2.waitKey(1)