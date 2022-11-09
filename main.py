import platform, json, os
import moviepy.editor as moviepy
from PIL import Image

f = open('input.json', "r")
data = json.loads(f.read())

outputFormat = data["outputFormat"]
imageValidFormats = json.loads(open('validFormats.json', "r").read())["imageFormats"]
videoValidFormats = json.loads(open('validFormats.json', "r").read())["videoFormats"]

outputFolder = "output"

if not data["outputFolder"] == "":
    if (os.path.isdir(data["outputFolder"])):
        outputFolder = data["outputFolder"]

for folder in data["path"]:
    # iterate over files in
    # that directory
    if (os.path.isdir(folder)):
        folderName = os.path.basename(folder)
        if (not os.path.isdir(outputFolder+"/"+folderName)):
            os.mkdir(outputFolder+"/"+folderName)
        for filename in os.listdir(folder):
            path = os.path.join(folder, filename)
            # checking if it is a file
            if os.path.isfile(path):
                    if filename.split(".")[-1] in imageValidFormats:
                        print(filename.split(".")[-1])
                        image = Image.open(path).convert("RGB")
                        fileNameCoverted = filename.split(".")[0]+"."+outputFormat
                        image.save(outputFolder+"/{}/{}".format(folderName, fileNameCoverted), outputFormat)
                        print("Transformed {} into {}".format(filename, fileNameCoverted))
                    elif filename.split(".")[-1] in videoValidFormats:
                        clip = moviepy.VideoFileClip(path)
                        fileNameCoverted = filename.split(".")[0]+"."+outputFormat
                        clip.write_videofile(outputFolder+"/{}/{}".format(folderName, fileNameCoverted))
                        print("Transformed {} into {}".format(filename, fileNameCoverted))
                    else:
                        raise("{} invalid format".format(filename))
        print("Finish {}".format(folderName))
    else:
        print("Invalid output folder {}".format(folder))
    
                    