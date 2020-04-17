import os


def build(dir):
    verbData = []
    listOfFiles = os.listdir(dir)
    for i in range(len(listOfFiles)):
        verbFile = open(dir+"/" +listOfFiles[i], "r")
        verbFileContent = verbFile.read()
        seperatedFileContent = verbFileContent.split("\n")
        splitPresent = seperatedFileContent[2].split(",")
        seperatedFileContent[2] = splitPresent
        verbData.append(seperatedFileContent)
        
    return (verbData)

def collectSpanishWords(dir):
    verbData = []
    EnglishWordList = []
    listOfFiles = os.listdir(dir)
    for i in range(len(listOfFiles)):
        verbFile = open(dir+"/" +listOfFiles[i], "r")
        verbFileContent = verbFile.read()
        seperatedFileContent = verbFileContent.split("\n")
        EnglishWordList.append(seperatedFileContent[0])
    
    return (EnglishWordList)
