import unittest
from src.lab3.sudoku import group

class SudokuTestCase(unittest.TestCase):

    def test_group(self):
        self.assertEqual(group([1,2,3,4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group([1,2,3,4,5,6,7,8,9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(group([1,2,3,4,5,6], 6), [[1,2,3,4,5,6]])
        self.assertEqual(group([1,2,3], 1), [[1],[2],[3]])

