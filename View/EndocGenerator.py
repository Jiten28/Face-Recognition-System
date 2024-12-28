import cv2
import face_recognition as fr
import os
import pickle

#Importing student images
folderPath = "Images"
pathList = os.listdir(folderPath)
# print(pathList) 

imgList = [ ]
studentIds = [ ]

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    # print(os.path.splitext(path)[0])
    studentIds.append(os.path.splitext(path)[0])
# print(len(studentIds))

def fileEncodings(imagesList):
    encoderList = [ ]
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encoderList.append(encode)
    return encoderList

print("Encoding Start...")
encoderListKnown = fileEncodings(imgList)
encodeListKnownWithIds = [encoderListKnown, studentIds]
print("Encoding Complete")

file = open('EncodeFile.p', 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved")
