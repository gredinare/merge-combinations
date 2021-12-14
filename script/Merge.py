from PIL import Image
import itertools
import os

inputDirMain = os.getcwd() + "\input" + "\\"
inputFilesList = []

for i in range(len(os.listdir(inputDirMain))):
    strTemp = inputDirMain + os.listdir(inputDirMain)[i]

    listFilesTemp = []
    for j in range(len(os.listdir(strTemp))):
        fileDir = strTemp + "\\" + os.listdir(strTemp)[j]
        listFilesTemp.append(fileDir)
    
    inputFilesList.append(listFilesTemp)

outputNameFolder = "\output_{:02d}".format(len(os.listdir(os.getcwd() + "\output")))
outputDir = os.getcwd() + "\output" + outputNameFolder
os.mkdir(outputDir)


listOfCombinations = list(itertools.product(*inputFilesList))
count = 0

for i in range(len(listOfCombinations)):
    imgTemp = Image.open(listOfCombinations[i][0]).convert("RGBA")
    j = 1

    for j in range(len(listOfCombinations[i])):
        imgTemp2 = Image.open(listOfCombinations[i][j])
        imgTemp.paste(imgTemp2, (0,0), imgTemp2)
    
    imgTemp.save("{}\{:02d}.png".format(outputDir, count))
    count = count + 1

    