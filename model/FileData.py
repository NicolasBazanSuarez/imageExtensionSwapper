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
    
    @property
    def folderName(self):
        return self.__folderName
    @property
    def filename(self):
        return self.__filename
    @property
    def path(self):
        return self.__path
    @property
    def outputFolder(self):
        return self.__outputFolder
    
    @folderName.setter
    def folderName(self, folderName):
        self.__folderName = folderName
        
    @filename.setter
    def filename(self, filename):
        self.__filename = filename
    
    @path.setter
    def path(self, path):
        self.__path = path
    
    @outputFolder.setter
    def outputFolder(self, outputFolder):
        self.__outputFolder = outputFolder
    