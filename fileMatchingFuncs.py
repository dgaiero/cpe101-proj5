# Project 5
#
# Names: Russell Caletena and Dominic Gaiero
# Instructor: S. Einakian
# Section: 5
# Github: https://github.com/dgaiero/cpe101-proj5
# For more inforamtion, see README.md

#######                    #     #
#       # #      ######    ##   ##   ##   #####  ####  #    # # #    #  ####
#       # #      #         # # # #  #  #    #   #    # #    # # ##   # #    #
#####   # #      #####     #  #  # #    #   #   #      ###### # # #  # #
#       # #      #         #     # ######   #   #      #    # # #  # # #  ###
#       # #      #         #     # #    #   #   #    # #    # # #   ## #    #
#       # ###### ######    #     # #    #   #    ####  #    # # #    #  ####

#######
#       #    # #    #  ####  ##### #  ####  #    #  ####
#       #    # ##   # #    #   #   # #    # ##   # #
#####   #    # # #  # #        #   # #    # # #  #  ####
#       #    # #  # # #        #   # #    # #  # #      #
#       #    # #   ## #    #   #   # #    # #   ## #    #
#        ####  #    #  ####    #   #  ####  #    #  ####

# ========================================================
# Function that opens the text file, and parses it to be
# used for other functions
# ========================================================


def getTextFileInfo(fileName):
    fin = open(fileName)
    textFileInfoList = []
    for line in fin:
        words = line.split()
        textFileInfoList.append(words)
    fin.close()
    return textFileInfoList

# ========================================================
# This function returns a list of just account numbers
# ========================================================


def sortAccountNumber(textFileInfoList):
    sortedAccountNumberList = []
    i = 0
    while i < len(textFileInfoList):
        unsortedAccountNumber = int(textFileInfoList[i][0])
        sortedAccountNumberList.append(unsortedAccountNumber)
        i += 1
    sortedAccountNumberList.sort()
    return sortedAccountNumberList

# ========================================================
# This function sorts all of the account data by
# account number
# ========================================================


def sortTextFileInfo(textFileInfoList):
    sortTextFileInfoList = textFileInfoList
    sortTextFileInfoList.sort(key=lambda a: a[0])
    return sortTextFileInfoList

# ========================================================
# This function creates the sorted old master file
# (style the data so that it matches the oldMaster file)
# ========================================================


def createOldMaster(sortTextFileInfoList):
    fout = open('sorted_oldMaster.dat', 'w')
    k = 0
    while k in range(len(sortTextFileInfoList)):
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

# ========================================================
# The function creates the new master file with the
# unmatched transactions
# ========================================================


def createNewMaster(sortTextFileInfoList):
    fout = open('newMaster.dat', 'w')
    k = 0
    while k in range(len(sortTextFileInfoList[1])):
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
        fout.write('Unmatched transaction record for account {}\n'.format(
            sortTextFileInfoList[0]))
    fout.close()

# ========================================================
# This function matches transactions to the master file
# ========================================================


def matchTransaction(old_sorted_list, transactionFile, accountNumbers):
    notFound = []
    for i in range(len(old_sorted_list)):
        for j in range(len(transactionFile)):
            if transactionFile[j][0] == old_sorted_list[i][0]:
                old_balance = float(old_sorted_list[i][3])
                add_balance = float(transactionFile[j][1])
                old_sorted_list[i][3] = "{:.2f}".format(
                    old_balance + add_balance)
            else:
                if int(transactionFile[j][0]) not in accountNumbers:
                    notFound.append(int(transactionFile[j][0]))
                    accountNumbers.append(int(transactionFile[j][0]))
    masterData = [notFound, old_sorted_list]
    return(masterData)
