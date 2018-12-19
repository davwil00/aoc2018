import unittest
from part1 import Part1


class Part1Test(unittest.TestCase):
    def groupLetters(self):
        self.assertEqual(Part1.group_letters('aa'), {'a': 2})


if __name__ == '__main__':
    unittest.main()
