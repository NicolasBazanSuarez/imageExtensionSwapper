import moviepy.editor as moviepy
from modules import output
from model.FileData import FileData

def convert(outputFormat, fileData: FileData):
    clip = moviepy.VideoFileClip(fileData.__path)
    fileNameConverted = output.getNewFileName(fileData.__filename, outputFormat)
    clip.write_videofile(output.getNewFilePath(fileData.__outputFolder, fileData.__folderName, fileNameConverted))
    output.endFileConversion(fileData.__filename, fileNameConverted)