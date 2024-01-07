# required libraries
import re
import os
from collections import Counter

# get list of names so that they can be put in Excel as original and later renamed
def ogList(imgsWinter):
    namesList = []
    namesTotal = os.listdir(imgsWinter)
    for image in namesTotal:
        namesList.append(image)
    return namesList

# renames the actual files fulfilling requirements - prefix, suffixes, underscores, 0s
def beginRename(imgsWinter):
    newNames = []
    updatedName = ""
    imgsFinal = os.listdir(imgsWinter)
    for image in imgsFinal:
        try:
            # takes apart the file name. removes prefix and separates numbers
            remIMG = re.search(r'\d+\.JPG', image)
            withoutPrefix = remIMG.group()
            justName = withoutPrefix.split('.')[0]
            # adds new prefixes, suffixes, and zeroes
            updatedName = "PWP2024" + "_" + "000" + justName + "A" + "_ALEXEY.JPG"
            newNames.append(updatedName)
        except:
            print("Error")
    print(newNames)
    return newNames

# checking and solving duplicates
def checkDuplicates(newNames):
    # shows how much each file name appears
    layout = Counter(newNames)
    print(layout)
    unDuped = []
    # for duplicates
    nameRemains = "lexey"
    for name in newNames:
        # if the file name appears twice
        if layout[name] > 1:
            dismantled = name.split('_')
            # adds bits of my name
            finalName = "PWP2024_" + dismantled[1] + nameRemains[0:layout[name]-1] + "_ALEXEY.JPG"
            unDuped.append(finalName)
            layout[name] -= 1
        else:
            unDuped.append(name)
    print(unDuped)
    print(len(unDuped))
    unDuped.sort()
    return unDuped
