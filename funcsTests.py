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
from fileMatchingFuncs import *


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
            ['600', 'Nicol', 'Green', '-20.00', '8058875571', 'SLO']])

        self.assertEqual(getTextFileInfo('newIn2.dat'), [
            ['101', 'Ayssa', 'Sherman', '240.22', '8051298970', 'SLO'],
            ['127', 'Robbin', 'Perry', '-59.37', '8051234820', 'Arroyo_Grande'],
            ['210', 'Nolan', 'Woodbreak', '327.22', '8059855128', 'SLO'],
            ['245', 'Jeffry', 'Smith', '15.31', '8057901000', 'Santa_Maria'],
            ['715', 'Erick', 'Dowsy', '123.22', '8052006912', 'Atascadero'],
            ['788', 'Laris', 'Nolan', '697.86', '805125789', 'Paso_Robles']])

        self.assertEqual(getTextFileInfo('newIn3.dat'), [
            ['010', 'Jo', 'Lee', '-185.02', '8052348970', 'Santa_Maria'],
            ['103', 'Kent', 'Lee', '1698.48', '8123464820', 'SLO'],
            ['111', 'Shay', 'Jam', '143.02', '8051200891', 'Santa_Rose'],
            ['555', 'Renei', 'McCart', '100.59', '8057901237', 'Santa_Rose'],
            ['808', 'Sara', 'Grave', '-83.73', '8052586912', 'Morro_Bay']])

    def test_sortAccountNumber(self):
        self.assertEqual(sortAccountNumber(getTextFileInfo('oldMaster.dat')), [
            100, 120, 200, 300, 340, 500, 600, 700, 800])
        self.assertEqual(sortAccountNumber(getTextFileInfo('newIn2.dat')), [
            101, 127, 210, 245, 715, 788])
        self.assertEqual(sortAccountNumber(getTextFileInfo('newIn3.dat')), [10, 103, 111, 555, 808])

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
            ['800', 'Mike', 'Rosen', '-104.58', '8051200891', 'Pismo_Beach']])

        self.assertEqual(sortTextFileInfo(getTextFileInfo('newIn2.dat')), [
            ['101', 'Ayssa', 'Sherman', '240.22', '8051298970', 'SLO'],
            ['127', 'Robbin', 'Perry', '-59.37', '8051234820', 'Arroyo_Grande'],
            ['210', 'Nolan', 'Woodbreak', '327.22', '8059855128', 'SLO'],
            ['245', 'Jeffry', 'Smith', '15.31', '8057901000', 'Santa_Maria'],
            ['715', 'Erick', 'Dowsy', '123.22', '8052006912', 'Atascadero'],
            ['788', 'Laris', 'Nolan', '697.86', '805125789', 'Paso_Robles']])

        self.assertEqual(sortTextFileInfo(getTextFileInfo('newIn3.dat')), [
            ['010', 'Jo', 'Lee', '-185.02', '8052348970', 'Santa_Maria'],
            ['103', 'Kent', 'Lee', '1698.48', '8123464820', 'SLO'],
            ['111', 'Shay', 'Jam', '143.02', '8051200891', 'Santa_Rose'],
            ['555', 'Renei', 'McCart', '100.59', '8057901237', 'Santa_Rose'],
            ['808', 'Sara', 'Grave', '-83.73', '8052586912', 'Morro_Bay']])

    def test_matchTransaction(self):
        self.assertEqual(matchTransaction(sortTextFileInfo(getTextFileInfo('oldMaster.dat')),
            getTextFileInfo('transaction.dat'),
            sortAccountNumber(getTextFileInfo('oldMaster.dat'))),
            [[400, 900],
            [['100', 'Alan', 'Jones', '445.48', '8053564820', 'SLO'],
            ['120', 'Ford', 'Strong', '190.17', '8051155329', 'SLO'],
            ['200', 'Adam', 'Wise', '350.00', '8059867128', 'SLO'],
            ['300', 'Mary', 'Smith', '589.30', '8057901237', 'Santa_Maria'],
            ['340', 'Lena', 'Sharp', '70.00', '8058561859', 'SLO'],
            ['500', 'Sam', 'Sharp', '-55.25', '8052348970', 'SLO'],
            ['600', 'Nicol', 'Green', '-20.00', '8058875571', 'SLO'],
            ['700', 'Suzy', 'Green', '410.78', '8052586912', 'SLO'],
            ['800', 'Mike', 'Rosen', '-104.58', '8051200891', 'Pismo_Beach']]])

        self.assertEqual(matchTransaction(sortTextFileInfo(getTextFileInfo('newIn2.dat')),
            getTextFileInfo('trans2.dat'),
            sortAccountNumber(getTextFileInfo('newIn2.dat'))),
            [[201],
            [['101', 'Ayssa', 'Sherman', '240.22', '8051298970', 'SLO'],
            ['127', 'Robbin', 'Perry', '-40.37', '8051234820', 'Arroyo_Grande'],
            ['210', 'Nolan', 'Woodbreak', '534.36', '8059855128', 'SLO'],
            ['245', 'Jeffry', 'Smith', '15.31', '8057901000', 'Santa_Maria'],
            ['715', 'Erick', 'Dowsy', '123.22', '8052006912', 'Atascadero'],
            ['788', 'Laris', 'Nolan', '1409.97', '805125789', 'Paso_Robles']]])

        self.assertEqual(matchTransaction(sortTextFileInfo(getTextFileInfo('newIn3.dat')),
            getTextFileInfo('trans3.dat'),
            sortAccountNumber(getTextFileInfo('newIn3.dat'))),
            [[100],
            [['010', 'Jo', 'Lee', '-210.94', '8052348970', 'Santa_Maria'],
            ['103', 'Kent', 'Lee', '2847.98', '8123464820', 'SLO'],
            ['111', 'Shay', 'Jam', '266.46', '8051200891', 'Santa_Rose'],
            ['555', 'Renei', 'McCart', '100.59', '8057901237', 'Santa_Rose'],
            ['808', 'Sara', 'Grave', '-43.17', '8052586912', 'Morro_Bay']]])

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
