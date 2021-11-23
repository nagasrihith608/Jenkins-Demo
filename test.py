#!/usr/bin/python3

import unittest

from build import *

class Test(unittest.TestCase):
    def test_addition(self):
        x = 1
        y = 2
        expected = 3
        self.assertEqual(addition(x, y), expected)

    def test_subtraction(self):
        x = 1
        y = 2
        expected = -1
        self.assertEqual(subtraction(x, y), expected)

if __name__ == '__main__':
    unittest.main()
