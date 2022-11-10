from modules import jsonReader, output, startConversion

data = jsonReader.jsonReader("input.json")

mapValidator = jsonReader.loadValidator(data)

outputFolder = output.assignOutputFolder(data)

startConversion.start(data, mapValidator, outputFolder)
