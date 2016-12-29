#!/usr/bin/env python

import sys
import re

def countItems(line):
    digit = 0
    modifiedLine = ""

    numbers = result = re.findall(r'[0-9]+', line)
    for i in range(len(numbers)):
        digit += 1
        modifiedLine += str(int(numbers[i]) + 1) + " "
    return str(digit) + " " + modifiedLine.strip(" ") + "\n"


# Get the total number of args passed to the demo.py
total = len(sys.argv)
 
# Get the arguments list 
iFiles = sys.argv[1:]
print(iFiles)

for iFname in iFiles:
    #iFname = input()
    oFname = "ascii_"+iFname
    target = open(oFname, 'w')

    with open(iFname, "r") as ins:
        transNum = 1
        for line in ins:
            target.write(str(transNum)+" "+str(transNum)+" "+str(countItems(line)))#+"\t"+line)
            transNum += 1