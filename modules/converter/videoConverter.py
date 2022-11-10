import moviepy.editor as moviepy
from modules import output

def convert(filename, folderName, path, outputFormat, outputFolder):
    clip = moviepy.VideoFileClip(path)
    fileNameConverted = output.getNewFileName(filename, outputFormat)
    clip.write_videofile(output.getNewFilePath(outputFolder, folderName, fileNameConverted))
    output.endFileConversion(filename, fileNameConverted)