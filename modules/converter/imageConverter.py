from PIL import Image
from modules import output

def convert(filename, folderName, path, outputFormat, outputFolder):
    image = Image.open(path).convert("RGB")
    fileNameConverted = output.getNewFileName(filename, outputFormat)
    image.save(output.getNewFilePath(outputFolder, folderName, fileNameConverted), outputFormat)
    output.endFileConversion(filename, fileNameConverted)