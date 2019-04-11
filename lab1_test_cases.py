import unittest
from lab1 import *


class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)  # used to check for exception
        tlist = [0]
        self.assertEqual(max_list_iter(tlist), 0)  # list of one value should return that value
        tlist = [1, 2, 10, 50, 3]
        self.assertEqual(max_list_iter(tlist), 50)  # test right side location of max
        tlist = [1, 50, 10, 2, 3]
        self.assertEqual(max_list_iter(tlist), 50)  # test left side location of max
        tlist = [50, 50, 10, 2, 50]
        self.assertEqual(max_list_iter(tlist), 50)  # test when list includes multiple max
        tlist = [-5, -4, -3, -2, -1]
        self.assertEqual(max_list_iter(tlist), -1)  # tests negative values
        tlist = [4.78, 4.77, 4.79, 4, 0]
        self.assertEqual(max_list_iter(tlist), 4.79)  # testing floats
        tlist = [-4.78, -4.77, -4.79, -4, 0]
        self.assertEqual(max_list_iter(tlist), 0)  # test that 0 is greatest from negative values

    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([]), [])  # used to check for empty list exception
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])  # basic run through
        self.assertEqual(reverse_rec([4, 6, 4, 3, 2]), [2, 3, 4, 6, 4])  # longer list
        self.assertEqual(reverse_rec([-1, -2, -3, 4.35]), [4.35, -3, -2, -1])  # floats and negative int values
        self.assertEqual(reverse_rec([1, '', 3, 'hello']), ['hello', 3, '', 1]) # test with string and int values
        self.assertEqual(reverse_rec([5]), [5])  # list of one entry should return itself

    def test_bin_search(self):
        tlist = []  # testing empty string exception
        low = 0
        high = 0
        self.assertEqual(bin_search(7, low, high, tlist), None)
        tlist = [1, 2, 3, 4, 5]  # testing low > high exception
        low = 10
        high = len(tlist) - 1
        self.assertEqual(bin_search(5, low, high, tlist), None)
        tlist = [0, 1, 2, 3, 4, 7, 8, 9, 10]  # test if target is found right away
        low = 0
        high = len(tlist)-1
        self.assertEqual(bin_search(4, low, high, tlist), 4)
        tlist = [0, 1, 2, 3, 4, 7, 8, 9, 10]  # test for target on right half
        low = 0
        high = len(tlist) - 1
        self.assertEqual(bin_search(9, low, high, tlist), 7)
        tlist = [0, 1.0542, 2, 3, 4, 7, 8, 9, 10]  # test for target on left half and float
        low = 0
        high = len(tlist) - 1
        self.assertEqual(bin_search(1.0542, low, high, tlist), 1)
        tlist = [-5, -4, -3, -2, -1]  # test with negative entries
        low = 1
        high = 3
        self.assertEqual(bin_search(-3, low, high, tlist), 2)
        tlist = [5]  # test for list with one entry should always return 0 index
        low = 0
        high = len(tlist) - 1
        self.assertEqual(bin_search(5, low, high, tlist), 0)
        tlist = [0, 1, 2, 3, 4, 7, 8, 9, 10]  # if not found should return None
        low = 0
        high = len(tlist) - 1
        self.assertEqual(bin_search(11, low, high, tlist), None)
        tlist = None
        low = 0
        high = 1
        with self.assertRaises(ValueError):  # test for None int_list exception
            bin_search(14, low, high, tlist)


if __name__ == "__main__":
        unittest.main()
