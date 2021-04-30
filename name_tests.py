from full_name import *
import unittest


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(gen_full("Dewey", "Finn"), "Dewey Finn")

    def test2(self):
        self.assertEqual(gen_full("", ""), " ")

    def test3(self):
        self.assertEqual(gen_full("Firstnameonly", ""), "Firstnameonly ")

    def test4(self):
        self.assertEqual(gen_full("Firstname", "Lastname"), "Lastname Firstname")

if __name__ == "__main__":
    unittest.main()