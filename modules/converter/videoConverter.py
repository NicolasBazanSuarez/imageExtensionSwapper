import moviepy.editor as moviepy
from modules import output
from model.FileData import FileData

def convert(outputFormat, fileData: FileData):
    clip = moviepy.VideoFileClip(fileData.path)
    fileNameConverted = output.getNewFileName(fileData.filename, outputFormat)
    clip.write_videofile(output.getNewFilePath(fileData.outputFolder, fileData.folderName, fileNameConverted))
    output.endFileConversion(fileData.filename, fileNameConverted)