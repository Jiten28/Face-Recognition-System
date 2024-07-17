import cv2

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

while True:
    success, img = cap.read()
    
    imgBackground[162:162 + 480, 55:55 + 640] = img
    
    # cv2.imshow("webcam", img)
    cv2.imshow("Face Detection", imgBackground)
    cv2.waitKey(1)