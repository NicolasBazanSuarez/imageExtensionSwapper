from pydub import AudioSegment
from modules import output
from model.FileData import FileData

def convert(outputFormat, fileData: FileData):
    sound = AudioSegment.from_mp3(fileData.path)
    fileNameConverted = output.getNewFileName(fileData.filename, outputFormat)
    sound.export(output.getNewFilePath(fileData.outputFolder, fileData.folderName, fileNameConverted), format=outputFormat)
    output.endFileConversion(fileData.filename, fileNameConverted)