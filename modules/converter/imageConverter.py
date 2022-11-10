from PIL import Image
from modules import output
from model.FileData import FileData

def convert(outputFormat, fileData: FileData):
    image = Image.open(fileData.__path).convert("RGB")
    fileNameConverted = output.getNewFileName(fileData.__filename, outputFormat)
    image.save(output.getNewFilePath(fileData.__outputFolder, fileData.__folderName, fileNameConverted), outputFormat)
    output.endFileConversion(fileData.__filename, fileNameConverted)