import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources\\background.png')

#Importing the mode images into a list
folderModePath = "Resources\\Modes"
modePathList = os.listdir(folderModePath)
imgModeList = [ ]

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
# print(len(imgModeList))

#Load the encoding file
print("Loading the encoding file...")
file = 'EncodeFile.p'
f = open(file, 'rb')
encodeListKnownWithIds = pickle.load(f)
f.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encode file Loaded Successfully")

while True:
    success, img = cap.read()
    
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    
    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[0]
    
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print("Matches", matches)
        # print("Face Distance", faceDis)
        
        matchIndex = np.argmin(faceDis)
        # print("Match Index", matchIndex)
        
        if matches[matchIndex]:
            # print("Match Found(Known Face Detected)")
            # print(studentIds[matchIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, 20, rt=0)
            
            
    # cv2.imshow("webcam", img)
    cv2.imshow("Face Detection", imgBackground)
    cv2.waitKey(1)