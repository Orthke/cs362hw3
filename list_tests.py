from list_avg import *
import unittest


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(avg_list([]), None)

    def test2(self):
        self.assertEqual(avg_list([0,0,0,0,0]), 0)

    def test3(self):
        self.assertEqual(avg_list([-1,0,-1,0]), -0.5)

    def test4(self):
        self.assertEqual(avg_list([-1,0,-1,0]), 20)

if __name__ == "__main__":
    unittest.main()