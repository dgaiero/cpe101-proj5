# Project 5
#
# Names: Russell Caletena and Dominic Gaiero
# Instructor: S. Einakian
# Section: 5

def sortAccountNumber(fileName):
    fin = open(fileName)
    masterList = []
    sortedAccountNumberList = []
    i = 0
    for line in fin:
        words = line.split()
        #print (words)
        masterList.append(words)
    #print ()
    print (masterList)

    while i < len(masterList):
        #print (masterList[i][0])
        unsortedAccountNumber = int(masterList[i][0])
        sortedAccountNumberList.append(unsortedAccountNumber)
        i += 1
    sortedAccountNumberList.sort()
    #print()
    #print (sortedAccountNumberList)

    '''
    # SORT FIRST WAY
    finalList = []
    for item in sortedAccountNumberList:
        print (item)
        for k in range(len(masterList)):

            if item == (int(masterList[k][0])):
                #print ('True')
                finalList.append(masterList[k])
    '''
    # SORT SECOND WAY
    finalList = masterList
    finalList.sort(key=lambda a: a[0])
    #print (finalList)

    #print (finalList)

    '''
    fout = open('sorted_oldMaster.dat', 'w+')
    k = 0
    while k in range(len(finalList)):
        #tempString = ''
        #tempString += '  '.join(finalList[k])
        #print (tempString)
        tempString = '{:4} {:6} {:11} {:10} {:15} {:12}'.format(finalList[k][0], finalList[k][1], finalList[k][2], finalList[k][3], finalList[k][4], finalList[k][5])
        fout.write('{}\n'.format(tempString))
        k += 1
    fout.close()
    '''
    return sortedAccountNumberList
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


    #print (floatTransactionList)



x = sortAccountNumber('oldMaster.dat')
#addTransaction('transaction.dat', x)
