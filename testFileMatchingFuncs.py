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


def createOldMaster(sortTextFileInfoList):
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


def createNewMaster(sortTextFileInfoList):
    fout = open('newMaster.dat', 'w')
    k = 0
    while k in range(len(sortTextFileInfoList[1])):
        #tempString = ''
        #tempString += '  '.join(finalList[k])
        #print (tempString)
        tempString = '{:4} {:6} {:11} {:10} {:15} {:12}'.format(
            sortTextFileInfoList[1][k][0],
            sortTextFileInfoList[1][k][1],
            sortTextFileInfoList[1][k][2],
            sortTextFileInfoList[1][k][3],
            sortTextFileInfoList[1][k][4],
            sortTextFileInfoList[1][k][5])
        fout.write('{}\n'.format(tempString))
        k += 1
    for i in range(len(sortTextFileInfoList[0])):
        fout.write('Unmatched transaction record for account {}'.format(
            sortTextFileInfoList[0]))
    fout.close()


def matchTransaction(old_sorted_list, transactionFile, accountNumbers):
    notFound = []
    for i in range(len(old_sorted_list)):
        for j in range(len(transactionFile)):
            if transactionFile[j][0] == old_sorted_list[i][0]:
                old_balance = float(old_sorted_list[i][3])
                add_balance = float(transactionFile[j][1])
                old_sorted_list[i][3] = "{:.2f}".format(
                    old_balance + add_balance)
                # print (old_sorted_list[i])
            else:
                if int(transactionFile[j][0]) not in accountNumbers:
                    notFound.append(int(transactionFile[j][0]))
                    accountNumbers.append(int(transactionFile[j][0]))
                    # print("Not found - {}".format(transactionFile[j][0]))
        # print("\n")
    # print("\n\n\n\n")
    # print(old_sorted_list)
    # print("\n\n\n\n")
    masterData = [notFound, old_sorted_list]
    return(masterData)

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
