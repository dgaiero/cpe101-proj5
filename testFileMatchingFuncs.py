# Project 5
#
# Names: Russell Caletena and Dominic Gaiero
# Instructor: S. Einakian
# Section: 5


def getTextFileInfo(fileName):
    fin = open(fileName)
    textFileInfoList = []
    for line in fin:
        words = line.split()
        textFileInfoList.append(words)
    print(textFileInfoList)  # Added just to see what list prints
    return textFileInfoList


def sortAccountNumber(textFileInfoList):
    sortedAccountNumberList = []
    i = 0
    while i < len(textFileInfoList):
        unsortedAccountNumber = int(textFileInfoList[i][0])
        sortedAccountNumberList.append(unsortedAccountNumber)
        i += 1
    sortedAccountNumberList.sort()
    print()
    print(sortedAccountNumberList)  # Added just to see what list prints
    return sortedAccountNumberList


def sortTextFileInfo(textFileInfoList):
    sortTextFileInfoList = textFileInfoList
    sortTextFileInfoList.sort(key=lambda a: a[0])
    print()
    print(sortTextFileInfoList)  # Added just to see what list prints
    return sortTextFileInfoList


def createSortedFile(sortTextFileInfoList):
    fout = open('sorted_oldMaster.dat', 'w')
    k = 0
    while k in range(len(sortTextFileInfoList)):
        #tempString = ''
        #tempString += '  '.join(finalList[k])
        #print (tempString)
        tempString = '{:4} {:6} {:11} {:10} {:15} {:12}'.format(
            sortTextFileInfoList[k][0],
            sortTextFileInfoList[k][1],
            sortTextFileInfoList[k][2],
            sortTextFileInfoList[k][3],
            sortTextFileInfoList[k][4],
            sortTextFileInfoList[k][5])
        fout.write('{}\n'.format(tempString))
        k += 1
    fout.close()

def matchTransaction(old_sorted_list, transactionFile):
    for i in range(len(transactionFile)):
        pass



    '''
def addTransaction(FileName, inputList):
    fin = open(FileName)
    transactionList = []
    for line in fin:
        words = line.split()
        transactionList.append(words)
    #print (transactionList)

    i = 0
    tempL = []
    j = 0

    transactionList.sort()
    print (transactionList)

    floatTransactionList = []
    for item in transactionList:
        floatTransactionList.append(float(item[1]))
    print (floatTransactionList)

    while j < len(floatTransactionList):
        if item == '27.14':
            print ('True')
        j += 1
    '''
    '''
        for item2 in item:
            item2 = float(item2)
            print (item2)
            tempL.append(item2)
    print (tempL)
    '''
    '''
    while i < len(transactionList):
        floatTransactionList = []
        for item in transactionList[i]:
            #item = float(item)
            floatTransactionList.append(float(item))
            #j += 1
        i += 1
    '''

    '''
    print (floatTransactionList)
    #print (type(floatTransactionList[0]))
    '''
    '''
        unsortedTransaction = (transactionList[i][0])
        #transactionList.append(unsortedTransaction)
        i += 1
    '''
#addTransaction('transaction.dat', x)
