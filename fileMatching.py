# Project 5
#
# Names: Russell Caletena
# Instructor: S. Einakian
# Section: 5

from testFileMatchingFuncs import *
def main():
    fileData = getTextFileInfo('oldMaster.dat')
    accountNumbers = sortAccountNumber(fileData)
    sortedData = sortTextFileInfo(fileData)
    createOldMaster(sortedData)
    transactionData = getTextFileInfo('transaction.dat')
    sortedData = matchTransaction(sortedData, transactionData, accountNumbers)
    createNewMaster(sortedData)

if __name__ == "__main__":
    main()
