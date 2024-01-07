# required libraries
from sheetChange import *
from renaming import *

# path to the original folder full of files
imgsWinter = "C:/Users/alexe/Downloads/PWP2022/PWP2022"

# original list with originally named files
theOGList = ogList(imgsWinter)

# revamped list without duplication check
revampedList = beginRename(imgsWinter)

# revamped list with duplication check
dupedFinal = checkDuplicates(revampedList)

# inserts the original list into the spreadsheet
insertion("PWPWinter", 0, 1, theOGList)

# inserts the revised list into the spreadsheet
insertion("PWPWinter", 0, 2, dupedFinal)
