import platform, json, os
from PIL import Image

f = open('input.json', "r")
data = json.loads(f.read())

validFormats = json.loads(open('validFormats.json', "r").read())["formats"]

outputFormat = data["outputFormat"]

outputFolder = "output"

print(data["outputFolder"])

if not data["outputFolder"] == "":
    if (os.path.isdir(data["outputFolder"])):
        outputFolder = data["outputFolder"]

for folder in data["path"]:
    # iterate over files in
    # that directory
    folderName = os.path.basename(folder)
    if (not os.path.isdir(outputFolder+"/"+folderName)):
        os.mkdir(outputFolder+"/"+folderName)
    for filename in os.listdir(folder):
        imageName = os.path.join(folder, filename)
        # checking if it is a file
        if os.path.isfile(imageName) and filename.split(".")[-1] in validFormats:
            image = Image.open(imageName).convert("RGB")
            image.save(outputFolder+"/{}/{}".format(folderName, filename.split(".")[0])+"."+outputFormat, outputFormat)