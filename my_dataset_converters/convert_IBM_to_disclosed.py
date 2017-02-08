#!/usr/bin/env python

import sys
import re

global itemList
itemList = {}

def addToHashTable(line, lineNum):
    #global itemList
    numbers = result = re.findall(r'[0-9]+', line)
    for i in range(len(numbers)):
        if i >= 3:
            item = int(numbers[i])
            if item in itemList:
                itemList[item] += str(lineNum)+"\t"
            else:
                itemList[item] = str(lineNum)+"\t"

# Get the total number of args passed to the demo.py
total = len(sys.argv)
 
# Get the arguments list 
iFiles = sys.argv[1:]
print(iFiles)

for iFname in iFiles:
    #iFname = input()
    oFname = "disclosed_"+iFname
    target = open(oFname, 'w')
    lineNum = 0
    #global itemList
    itemlist = {}
    with open(iFname, "r") as ins:
        for line in ins:
            lineNum += 1
            addToHashTable(line, lineNum)
        totalItems = max(itemList.keys())
        #print(itemList)
        target.write(str(lineNum) + "\t" + str(totalItems + 1) + "\t\n")
        for i in range(0, totalItems + 1):
            if i in itemList:
                target.write(itemList[i].rstrip()+"\t\n")
            else:
                target.write("\n")

print("DONE: IBM_to_disclosed generation")