import os
currentDate=os.system("date")

#os.mkdir("/Applications/Harkirat white hat jr/Python/class 99/tempFolder")
workingDirectory=os.getcwd()
print(workingDirectory)

path="/Applications/Harkirat white hat jr/Python/class 99/"
isExistOrNot=os.path.exists(path)
print(isExistOrNot)
filePath="backupFiles.py"
rootExt=os.path.splitext(filePath)
print(rootExt[0])
print(rootExt[1])
print(os.listdir())