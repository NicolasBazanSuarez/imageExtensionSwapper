from pydub import AudioSegment
from modules import output
from model.FileData import FileData

def convert(outputFormat, fileData: FileData):
    sound = AudioSegment.from_mp3(fileData.__path)
    fileNameConverted = output.getNewFileName(fileData.__filename, outputFormat)
    sound.export(output.getNewFilePath(fileData.__outputFolder, fileData.__folderName, fileNameConverted), format=outputFormat)
    output.endFileConversion(fileData.__filename, fileNameConverted)