import os
from model.FileData import FileData

def assignOutputFolder(data):
    outputFolder = "output"

    if not data["outputFolder"] == "":
        if (os.path.isdir(data["outputFolder"])):
            outputFolder = data["outputFolder"]
    return outputFolder

def endFileConversion(filename, fileNameConverted):
    print("Transformed {} into {}".format(filename, fileNameConverted))
    
def endFolderConverter(folderName):
    print("Finish {}".format(folderName))
    
def getNewFileName(filename, outputFormat):
    return filename.split(".")[0]+"."+outputFormat

def getNewFilePath(outputFolder, folderName, fileNameConverted):
    return outputFolder+"/{}/{}".format(folderName, fileNameConverted)

def checkFolderExist(fileData: FileData):
    if (not os.path.isdir(fileData.outputFolder+"/"+fileData.folderName)):
        os.mkdir(fileData.outputFolder+"/"+fileData.folderName)