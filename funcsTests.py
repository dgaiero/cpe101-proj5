# Project 5
#
# Names: Russell Caletena
# Instructor: S. Einakian
# Section: 5

 #######                    #     #
 #       # #      ######    ##   ##   ##   #####  ####  #    # # #    #  ####
 #       # #      #         # # # #  #  #    #   #    # #    # # ##   # #    #
 #####   # #      #####     #  #  # #    #   #   #      ###### # # #  # #
 #       # #      #         #     # ######   #   #      #    # # #  # # #  ###
 #       # #      #         #     # #    #   #   #    # #    # # #   ## #    #
 #       # ###### ######    #     # #    #   #    ####  #    # # #    #  ####

 #######
    #    ######  ####  ##### # #    #  ####
    #    #      #        #   # ##   # #    #
    #    #####   ####    #   # # #  # #
    #    #           #   #   # #  # # #  ###
    #    #      #    #   #   # #   ## #    #
    #    ######  ####    #   # #    #  ####

# ======================================
# Import libraries
# ======================================
import unittest
from testFileMatchingFuncs import *

class TestCases (unittest.TestCase):
    # Add test functions here
    def test_getTextFileInfo(self):
        self.assertEqual(getTextFileInfo('oldMaster.dat'), [
        ['100', 'Alan', 'Jones', '348.17', '8053564820', 'SLO'],
        ['700', 'Suzy', 'Green', '-14.22', '8052586912', 'SLO'],
        ['300', 'Mary', 'Smith', '27.19', '8057901237', 'Santa_Maria'],
        ['800', 'Mike', 'Rosen', '-104.58', '8051200891', 'Pismo_Beach'],
        ['500', 'Sam', 'Sharp', '0.00', '8052348970', 'SLO'],
        ['200', 'Adam', 'Wise', '100.00', '8059867128', 'SLO'],
        ['120', 'Ford', 'Strong', '90.00', '8051155329', 'SLO'],
        ['340', 'Lena', 'Sharp', '70.00', '8058561859', 'SLO'],
        ['600', 'Nicol', 'Green', '-20.00', '8058875571', 'SLO']
        ] )

    def test_sortAccountNumber(self):
        self.assertEqual(sortAccountNumber(getTextFileInfo('oldMaster.dat')), [
        100, 120, 200, 300, 340, 500, 600, 700, 800])
    def test_sortTextFileInfo(self):
        self.assertEqual(sortTextFileInfo(getTextFileInfo('oldMaster.dat')), [
        ['100', 'Alan', 'Jones', '348.17', '8053564820', 'SLO'],
        ['120', 'Ford', 'Strong', '90.00', '8051155329', 'SLO'],
        ['200', 'Adam', 'Wise', '100.00', '8059867128', 'SLO'],
        ['300', 'Mary', 'Smith', '27.19', '8057901237', 'Santa_Maria'],
        ['340', 'Lena', 'Sharp', '70.00', '8058561859', 'SLO'],
        ['500', 'Sam', 'Sharp', '0.00', '8052348970', 'SLO'],
        ['600', 'Nicol', 'Green', '-20.00', '8058875571', 'SLO'],
        ['700', 'Suzy', 'Green', '-14.22', '8052586912', 'SLO'],
        ['800', 'Mike', 'Rosen', '-104.58', '8051200891', 'Pismo_Beach'],
        ] )

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
