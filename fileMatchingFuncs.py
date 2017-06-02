# Project 5
#
# Names: Russell Caletena and Dominic Gaiero
# Instructor: S. Einakian
# Section: 5

from given import *

def sortAccountNumber(fileName):
    fin = open(fileName)
    masterList = []
    unsortedAccountNumberList = []
    sortedAccountNunmberList = []
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
        unsortedAccountNumberList.append(unsortedAccountNumber)
        i += 1
    unsortedAccountNumberList.sort()
    print ()
    print (unsortedAccountNumberList)
    #print (sortedList)


sortAccountNumber('oldMaster.dat')
