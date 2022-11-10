from PIL import Image
from modules import output
from model.FileData import FileData

def convert(outputFormat, fileData: FileData):
    image = Image.open(fileData.path).convert("RGB")
    fileNameConverted = output.getNewFileName(fileData.filename, outputFormat)
    image.save(output.getNewFilePath(fileData.outputFolder, fileData.folderName, fileNameConverted), outputFormat)
    output.endFileConversion(fileData.filename, fileNameConverted)