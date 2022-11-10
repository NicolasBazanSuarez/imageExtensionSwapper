import os

from model.FileData import FileData
from modules import output
from modules.converter import audioConverter, imageConverter, videoConverter


def start(data, mapValidator, outputFolder):
    for folder in data["path"]:
        # iterate over files in
        # that directory
        if (os.path.isdir(folder)):
            fileData = FileData(folder, outputFolder)
            output.checkFolderExist(fileData)
            for filename in os.listdir(folder):
                fileData.filename = filename
                fileData.outputFolder = outputFolder
                path = os.path.join(folder, filename)
                # checking if it is a file
                if os.path.isfile(path):
                    print(fileData.filename)
                    if fileData.filename.split(".")[-1] in mapValidator["validFormats"]:
                        imageConverter.convert(mapValidator["outputFormat"], fileData)
                    elif fileData.filename.split(".")[-1] in mapValidator["validFormats"]:
                        videoConverter.convert(mapValidator["outputFormat"], fileData)
                    elif fileData.filename.split(".")[-1] in mapValidator["validFormats"]:
                        audioConverter.convert(mapValidator["outputFormat"], fileData)
                    else:
                        print("Cannot convert {} format into a {}".format(fileData, mapValidator["outputFormat"]))
            output.endFolderConverter(fileData.folderName)
        else:
            print("Invalid output folder {}".format(folder))
        