from cube_volume import *
import unittest


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(calc_volume_cube(3), 27)

    def test2(self):
        self.assertEqual(calc_volume_cube(0), 0)

    def test3(self):
        self.assertEqual(calc_volume_cube(-1), None)

if __name__ == "__main__":
    unittest.main()