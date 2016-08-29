import glob
import os

totalDel = 0

def removeFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
        global totalDel
        totalDel = totalDel + 1
    else:
        print ">> " + filename + " <<" + " does not exist. Skip!"
    return

def printResults():
    print "\n##############"
    print "Total deleted files: %i" % totalDel
    print "##############"
    return

print "Pascal VOC style data-set synchronizer \n"

# Path to folder containing subdir 'Annotations' and 'JPEGImages'
path = "Test"
pathAn = path + "/Annotation/*.xml"
pathIm = path + "/JPEGImages/*.JPEG"

anFiles = glob.glob(pathAn)
imFiles = glob.glob(pathIm)

imFilesName = []
anFilesName = []

for ele in imFiles:
    start = ele.find('/n') + 1
    end = ele.find('.JPEG', start)
    eleClean = ele[start:end]
    imFilesName.append(eleClean)
    found = 0
    # check if annotation file exist
    for anEl in anFiles:
        ex = anEl.find(eleClean)
        if ex != -1:
            found = 1
    if found != 1:
        print "Deleted >>" + ele
        removeFile(ele)

printResults()