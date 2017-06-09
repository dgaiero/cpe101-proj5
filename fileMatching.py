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

#     #                    #######
##   ##   ##   # #    #    #       #    # #    #  ####  ##### #  ####  #    #
# # # #  #  #  # ##   #    #       #    # ##   # #    #   #   # #    # ##   #
#  #  # #    # # # #  #    #####   #    # # #  # #        #   # #    # # #  #
#     # ###### # #  # #    #       #    # #  # # #        #   # #    # #  # #
#     # #    # # #   ##    #       #    # #   ## #    #   #   # #    # #   ##
#     # #    # # #    #    #        ####  #    #  ####    #   #  ####  #    #

# ========================================================
# Import libraries
# ========================================================

from fileMatchingFuncs import *

# ========================================================
# Main Function
# ========================================================


def main():
    fileData = getTextFileInfo('oldMaster.dat')
    accountNumbers = sortAccountNumber(fileData)
    sortedData = sortTextFileInfo(fileData)
    createOldMaster(sortedData)
    transactionData = getTextFileInfo('transaction.dat')
    sortedData = matchTransaction(sortedData, transactionData, accountNumbers)
    createNewMaster(sortedData)

# ========================================================
# Calls main function
# ========================================================


if __name__ == "__main__":
    main()
