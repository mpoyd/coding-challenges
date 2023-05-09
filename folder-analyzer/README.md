# How to test the program
If you want to count hidden directories run the following command:
```
python .\analyze-folders.py [Directory] countHidden
```
Otherwise remove the countHidden argument:
```
python .\analyze-folders.py [Directory]
```
# Folder Analyzer

Goal of this program is to analyze a *folder structure* (folder and it's subfolder hierarchy) on your computer's filesystem in order to retrieve various statistics about the files contained. The main purpose of the program is to categorize the files which are scanned into these categories:
- images
- documents
- music
- videos
- other files

The classification of a file should be done based on it's file extension. The tables below specify each of the categories and the connected file extensions. The output of the program shall be something like

found 7347 files in c:\root within 34 folders with  
43% images (728 files)  
30% documents (2203 files)  
2% audio (147 files)  
15% videos (1101 files)  
10% other (734 files)  

## File Categories

| Category | File Associations                         |
| ---------|:-----------------------------------------:|
| image    | jpeg, jpg, png, gif, svg                  |
| document | doc, docx, pdf, html, odt, ppt, pptx, txt |
| audio    | mp3, wav, aac, wma                        |
| video    | mp4, mpg, avi, wmv                        |

Note that there are much more file extensions for each category. As this requirement just serves educational purposes, it is not complete. 

For further information look here:\
https://en.wikipedia.org/wiki/Video_file_format  
https://en.wikipedia.org/wiki/Audio_file_format  
https://en.wikipedia.org/wiki/Audio_file_format    
https://blog.filestack.com/thoughts-and-knowledge/document-file-extensions-list/  

## Program usage

The idea is to use the program on the commandline like this:

```
analyze-folders <directory>
```
  
Then the specified output shall be generated.

## Deliverables

Fork this repository and put your code inside this root folder.

Write a program in the language of your choice which fulfills this requirement. Make sure, that you create small units of execution in order for later reusage. Also try to comment as much as possible your code, if something is not obvious.

Feel free to deliver more functionality, if you like. Some ideas here:
- statistics based on file types (distribution of image file extensions among the image files)
- implement switch to also consider hidden files
- also count the file size and build an alternative statistic based on file size and not amount of files

Update the description here with information on howto test the program.



