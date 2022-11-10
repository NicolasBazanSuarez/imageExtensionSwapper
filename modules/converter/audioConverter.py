from pydub import AudioSegment
from modules import output

def convert(filename, folderName, path, outputFormat, outputFolder):
    sound = AudioSegment.from_mp3(path)
    fileNameConverted = output.getNewFileName(filename, outputFormat)
    sound.export(output.getNewFilePath(outputFolder, folderName, fileNameConverted), format=outputFormat)
    output.endFileConversion(filename, fileNameConverted)