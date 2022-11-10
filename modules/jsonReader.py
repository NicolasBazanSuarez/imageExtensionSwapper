import json

def jsonReader(jsonPath):
    f = open(jsonPath, "r")
    data = json.loads(f.read())
    return data

def loadValidator(data):
    mapValidator = {}
    mapValidator.update({"outputFormat" : data["outputFormat"]})
    validFormats = jsonReader('validFormats.json')
    for format in validFormats:
        if mapValidator["outputFormat"] in validFormats[format]:
            mapValidator.update({"validFormats" : validFormats[format]})
    return mapValidator