#Importing the mode images into a list
folderModePath = "Resources\\Modes"
modePathList = os.listdir(folderModePath)
imgModeList = [ ]

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
print(len(imgModeList))