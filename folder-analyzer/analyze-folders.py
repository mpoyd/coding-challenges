import os
import sys


#We first need to get the the directory from the command line arguments
#If there is no argument we exit the program
if(len(sys.argv) <2):
    sys.exit("Missing input directory")

#Getting the directory
directory = sys.argv[1]
#Getting the view hidden files parameter, by default we don't count hidden files
hiddenFilesParameter = "dontCountHiddenFiles";
if(len(sys.argv) >2):
    hiddenFilesParameter = sys.argv[2]


#Initializing Categories based on file associations
imageCategory = ["jpeg", "jpg", "png", "gif", "svg"]
documentCategory = ["doc", "docx", "pdf", "html", "odt", "ppt", "pptx", "txt"]
audioCategory = ["mp3", "wav", "aac", "wma"]
videoCategory = ["mp4", "mpg", "avi", "wmv"]

#Initializing counters
folderCounter = 1
fileCounter = 0
imageCounter = 0
documentCounter = 0
audioCounter = 0
videoCounter = 0
otherCounter = 0

#We will use os.walk() in order to list all files and directories in a directory tree
#   os.walk() returns three values on each iteration of the loop:
#     The name of the current folder
#     A list of folders in the current folder
#     A list of files in the current folder

for dirpath, dirnames, files in os.walk(directory):
    #We exclude hidden folders and files if the hidden files parameter is not set to countHidden
    if(hiddenFilesParameter!="countHidden"):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        files[:] = [f for f in files if not f.startswith('.')]
    #Counting sub directories
    for dir in dirnames:
        folderCounter+= 1
    #We iterate over the files in a folder
    for fileName in files:
        fileCounter += 1
        #Getting the file extention from the file name, we take the sub string that starts after '.'
        fileExtention = fileName[fileName.rfind('.')+1::]
        #Adding to a Category counter based on the file extension
        if (fileExtention in imageCategory): imageCounter += 1
        elif (fileExtention in documentCategory): documentCounter += 1
        elif (fileExtention in audioCategory): audioCounter += 1
        elif (fileExtention in videoCategory): videoCounter += 1
        else : otherCounter += 1

#if we dont find any files we exit the program
if(fileCounter == 0):
    sys.exit("No files found")

#Calculating statistics
percentageImage = imageCounter/fileCounter * 100
percentageDocument = documentCounter/fileCounter * 100
percentageAudio = audioCounter/fileCounter * 100
percentageVideo = videoCounter/fileCounter * 100
percentageOther = otherCounter/fileCounter * 100

#Printing Output
output ="found {fileCounter} files in {directory} within {folderCounter} folders with \n {percentageImage}% images ({imageCounter} files)\n {percentageDocument}% documents ( {documentCounter} files)\n {percentageAudio}%  audio ({audioCounter} files)\n {percentageVideo}% video ( {videoCounter} files)\n {percentageOther}%  other ({otherCounter} files)\n".format(fileCounter=fileCounter,directory=directory,folderCounter=folderCounter,percentageImage=percentageImage,imageCounter=imageCounter,percentageDocument=percentageDocument,documentCounter=documentCounter,percentageAudio=percentageAudio,audioCounter=audioCounter,percentageVideo=percentageVideo,videoCounter=videoCounter,percentageOther=percentageOther,otherCounter=otherCounter)
print(output)





    