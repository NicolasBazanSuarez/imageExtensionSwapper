from paprika import *
import os

@data
class FileData:
    filename: str
    folderName: str
    path: str
    outputFolder: str
    
    def __init__(self, filename, folder, outputFolder):
        self.folderName = self.createFolderName(folder)
        self.filename = filename
        self.outputFolder = outputFolder
        self.path = self.createPath(filename)
        
    def __init__(self, folder, outputFolder):
        self.folderName = self.createFolderName(folder)
        self.outputFolder = outputFolder
        
    def createPath(folder, filename):
        os.path.join(folder, filename)
    
    def createFolderName(folder):
        return os.path.basename(folder)
    