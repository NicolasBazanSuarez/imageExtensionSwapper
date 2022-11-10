import os

from paprika import *


@data
class FileData:
    __filename: str
    __folderName: str
    __path: str
    __outputFolder: str
    
    def __init__(self, filename, folder, outputFolder):
        self.__folderName = self.createFolderName(folder)
        self.__filename = filename
        self.__outputFolder = outputFolder
        self.__path = self.createPath(filename)
        
    def __init__(self, folder, outputFolder):
        self.__folderName = self.createFolderName(folder)
        self.__outputFolder = outputFolder
        
    def createPath(folder, filename):
        os.path.join(folder, filename)
    
    def createFolderName(folder):
        return os.path.basename(folder)
    