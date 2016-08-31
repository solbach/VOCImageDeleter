import os
import sys
import glob

totalDel = 0
totalNotDel = 0

def removeFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
        global totalDel
        totalDel = totalDel + 1
    else:
        print ">> " + filename + " <<" + " does not exist. Skip!"
        global totalNotDel
        totalNotDel = totalNotDel + 1
    return

def checkPath(path):
    if not os.path.isdir(path):
        print ">> " + path + " <<" + " does not exist."
        print "exit"
        sys.exit()
    return

def printResults():
    print "\n##############"
    print "Total deleted files: %i" % totalDel
    if totalNotDel > 0:
        print "Files not deleted: %i" % totalDel
    print "##############"
    return

def checkCNNsufficiency(anFiles):
    if len(anFiles) < 200:
        print "\nYou have less than 200 images in the data-set. (%i)" % len(anFiles)
        print "Are you sure you wanna keep it?"
    else:
        print "Data-set has enough training-images. (%i)" % len(anFiles)
    return

print "\n##############"
print "Pascal VOC style data-set synchronizer"
print "##############"

if len(sys.argv) < 2:
    print "\nNot enough arguments (%i)" %len(sys.argv)
    print "Usage: synchronize.py <folder>"
    print "<folder> needs subfolders: Annotations with .xml and JPEGImages .JPEG"
    print "exit"
    sys.exit()

# Path to folder containing subdir 'Annotations' and 'JPEGImages'
path = str(sys.argv[1])
pathAn = path + "Annotation/*.xml"
pathIm = path + "JPEGImages/*.JPEG"

# Check for Annotation and JPEGImages subfolders
checkPath(path + "Annotation/")
checkPath(path + "JPEGImages/")

anFiles = glob.glob(pathAn)
imFiles = glob.glob(pathIm)

for ele in imFiles:
    start = ele.find('/n') + 1
    end = ele.find('.JPEG', start)
    eleClean = ele[start:end]
    found = 0
    for anEl in anFiles:
        ex = anEl.find(eleClean + ".xml")
        if ex != -1:
            found = 1
    if found != 1:
        print "Deleted: " + ele
        removeFile(ele)

printResults()
# In a veeery early state
checkCNNsufficiency(anFiles)