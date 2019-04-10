import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("Town", 100.5, -123.4)
        self.assertEqual(repr(loc), "Location('Town', 100.5, -123.4)")
        loc = Location("Home", -50, 150.34)
        self.assertEqual(repr(loc), "Location('Home', -50, 150.34)")

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        other = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc, other)  # checks to ake sure identical objects point to same
        loc = Location("SLO", 35.3, -120.7)
        other = Location("SLOPE", 123, -456)
        self.assertNotEqual(loc, other)  # checks that they are NOT equal
        loc = Location("SLO", 35.3000000000001, -120.7000000000000001)
        other = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc, other)
        loc = Location("Hometown", 50.3, 100)
        other = Location("Hometown", 50.4, 100)
        self.assertNotEqual(loc, other)


if __name__ == "__main__":
        unittest.main()
