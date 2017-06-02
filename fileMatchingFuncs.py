# Project 5
#
# Names: Russell Caletena and Dominic Gaiero
# Instructor: S. Einakian
# Section: 5

# I don't know how to access 'oldMaster.dat' in given directory so I have
# created a temporary 'oldMaster.dat' file in the repository
from given import *

def sortAccountNumber(fileName):
    fin = open(fileName)
    masterList = []
    sortedAccountNumberList = []
    i = 0

    for line in fin:
        words = line.split()
        print (words)
        masterList.append(words)
    print ()
    print (masterList)

    while i < len(masterList):
        #print (masterList[i][0])
        unsortedAccountNumber = int(masterList[i][0])
        sortedAccountNumberList.append(unsortedAccountNumber)
        i += 1
    sortedAccountNumberList.sort()
    print()
    print (sortedAccountNumberList)

    j = 0
    finalList = []
    for item in sortedAccountNumberList:
        print (item)

        #int(masterList[j][0])
        if item == (int(masterList[j][0])):
            print ('True')
            finalList.append(masterList[j])
        else:
            continue
        j += 1
    print (finalList)


    #print (sortedList)


sortAccountNumber('oldMaster.dat')
