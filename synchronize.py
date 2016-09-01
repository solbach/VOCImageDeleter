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

def printResults(pathAn, pathIm):
    anFiles = glob.glob(pathAn)
    imFiles = glob.glob(pathIm)

    print "\n##############"
    if not (len(imFiles) - len(anFiles)) == 0:
        print "Remaining Images: %i" % len(imFiles)
        print "Remaining Annotations: %i" % len(anFiles)
        print "---> Should be not different."
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

def init(inputParam):
    print "\n##############"
    print "Pascal VOC style data-set synchronizer"
    print " by Markus Solbach "
    print "    solbach@cse.yorku.ca"
    print "##############"

    if len(inputParam) < 2:
        print "\nNot enough arguments (%i)" % len(inputParam)
        print "Usage: synchronize.py <folder>"
        print "<folder> needs subfolders: Annotations with .xml and JPEGImages .JPEG"
        print "exit"
        sys.exit()
    return

################## Main

init(sys.argv)
# Path to folder containing subdir 'Annotations' and 'JPEGImages'
path = str(sys.argv[1])
pathAn = path + "Annotation/*.xml"
pathIm = path + "JPEGImages/*.JPEG"

# Check for Annotation and JPEGImages subfolders
checkPath(path + "Annotation/")
checkPath(path + "JPEGImages/")

anFiles = glob.glob(pathAn)
imFiles = glob.glob(pathIm)
count = 0

# Go over all Images and check if there is a corresponding annotation file
# Aligning JPEG with XML Folder
for ele in imFiles:
    start = ele.find('/n') + 1
    end = ele.find('JPEG', start)
    eleClean = ele[start:end]
    # print eleClean
    found = 0
    for anEl in anFiles:
        ex = anEl.find(eleClean + "xml")
        if ex >= 0:
            found = 1
            break
    if found == 0:
        print "Deleted: " + ele
        count = count + 1
        removeFile(ele)

# Aaaaaand the other way around
# Aligning XML with JPEG Folder
imFiles = glob.glob(pathIm)
for anEl in anFiles:
    start = anEl.find('/n') + 1
    end = anEl.find('xml', start)
    anElClean = anEl[start:end]
    found = 0
    for ele in imFiles:
        ex = ele.find(anElClean + "JPEG")
        if ex >= 0:
            found = 1
            break
    if found == 0:
        print "Deleted: " + anEl
        count = count + 1
        removeFile(anEl)

printResults(pathAn, pathIm)
# In a veeery early state
checkCNNsufficiency(anFiles)