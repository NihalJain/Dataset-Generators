#!/usr/bin/env python

import sys
import re

def getModifiedTransaction(line):
    digit = 0
    modifiedLine = ""

    numbers = result = re.findall(r'[0-9]+', line)
    for i in range(len(numbers)):
        if i >= 3:
            modifiedLine += str(int(numbers[i])) + " "
    return modifiedLine.strip(" ") + "\n"

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
        for line in ins:
            target.write(getModifiedTransaction(line))

print("DONE: IBM_to_ascii generation")
