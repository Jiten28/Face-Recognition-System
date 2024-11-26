import cv2
# import face_recognition as fr
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
print(len(studentIds))