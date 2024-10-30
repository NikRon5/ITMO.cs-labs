import unittest
from src.lab3.sudoku import group, get_col, get_row, get_block, read_sudoku

class SudokuTestCase(unittest.TestCase):

    def test_group(self):
        self.assertEqual(group([1,2,3,4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group([1,2,3,4,5,6,7,8,9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(group([1,2,3,4,5,6], 6), [[1,2,3,4,5,6]])
        self.assertEqual(group([1,2,3], 1), [[1],[2],[3]])

    def test_get_row(self):
        self.assertEqual(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '2', '.'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0)), ['4', '.', '6'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0)), ['.', '8', '9'])
        self.assertEqual(get_row([['1', '2'], ['3', '4'], ['5', '6'], ['7', '8']], (2, 0)), ['5', '6'])

    def test_get_col(self):
        self.assertEqual(get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '4', '7'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1)), ['2', '.', '8'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2)), ['3', '6', '9'])
        self.assertEqual(get_col([['1', '2', '3', '4', '5'], ['6', '7', '8', '9']], (0, 2)), ['3', '8'])

    def test_get_block(self):
        grid = read_sudoku('../../src/lab3/puzzle1.txt')

        self.assertEqual(get_block(grid, (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEqual(get_block(grid, (4, 7)), ['.', '.', '3', '.', '.', '1', '.', '.', '6'])
        self.assertEqual(get_block(grid, (8, 8)), ['2', '8', '.', '.', '.', '5', '.', '7', '9'])
        self.assertEqual(get_block(grid, (7, 1)), ['.', '6', '.', '.', '.', '.', '.', '.', '.'])


