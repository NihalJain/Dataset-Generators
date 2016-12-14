import re


def countItems(line):
    digit = 0
    modifiedLine = ""

    numbers = result = re.findall(r'[0-9]+', line)
    for i in range(len(numbers)):
        digit += 1
        modifiedLine += str(int(numbers[i]) + 1) + " "
    return str(digit) + " " + modifiedLine.strip(" ") + "\n"

iFiles = ["hor_10_10000.txt", "hor_12_10000.txt", "hor_14_10000.txt", "hor_16_10000.txt", "hor_18_10000.txt",
          "hor_20_10000.txt"]

for iFname in iFiles:
    #iFname = input()
    oFname = "for_"+iFname
    target = open(oFname, 'w')

    with open(iFname, "r") as ins:
        transNum = 1
        for line in ins:
            target.write(str(transNum)+" "+str(transNum)+" "+str(countItems(line)))#+"\t"+line)
            transNum += 1