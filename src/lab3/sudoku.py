import pathlib
import typing as tp
import random

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [values[i:i+n] for i in range(0, len(values), n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    return [grid[i][pos[1]] for i in range(len(grid))]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    row_ind = pos[1]//3*3
    col_ind = pos[0]//3*3
    return [grid[i][j] for i in range(col_ind, col_ind+3) for j in range(row_ind, row_ind+3)]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return i, j
    return -1, -1

def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    union = set('123456789')
    values = set()

    values.update(get_row(grid, pos))
    values.update(get_col(grid, pos))
    values.update(get_block(grid, pos))

    return union.difference(values)


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    empty_pos = find_empty_positions(grid)

    if empty_pos == (-1,-1):
        return grid
    else:
        possible_vals = find_possible_values(grid, empty_pos)
        if len(possible_vals) == 0:
            return False

        y = empty_pos[0]
        x = empty_pos[1]

        for val in possible_vals:
            grid[y][x] = val
            t_grid = solve(grid)
            if not t_grid:
                grid[y][x] = '.'
            else:
                return t_grid
        return False

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False
    >>> bad_solution = [
    ...        ["6", "6", "1", "1", "1", "5", "8", "3", "7"],
    ...        ["3", "5", "7", "8", "2", "6", "1", "4", "9"],
    ...        ["1", "4", "8", "9", "3", "7", "5", "2", "6"],
    ...        ["6", "3", "9", "5", "1", "2", "4", "7", "8"],
    ...        ["5", "8", "1", "7", "6", "4", "3", "9", "2"],
    ...        ["4", "7", "2", "3", "9", "8", "6", "1", "5"],
    ...        ["9", "6", "4", "2", "8", "3", "7", "5", "1"],
    ...        ["8", "1", "5", "4", "7", "9", "2", "6", "3"],
    ...        ["7", "2", "3", "6", "5", "1", "9", "8", "4"],
    ...     ]
    >>> check_solution(bad_solution)
    False
    """

    for i in range(9):
        col = get_col(solution, (0, i))
        row = get_row(solution, (i, 0))
        block = get_block(solution, (i//3*3, i%3*3))
        if '.' in col or '.' in row or '.' in '.' in block:
            return False
        if not (len(set(col)) == 9 and len(set(row)) == 9 and len(set(block)) == 9):
            return False
    return True


def transpose(grid):
    """Транспонирование судоку"""
    t_grid = []
    for i in range(len(grid)):
        t = []
        for j in range(len(grid[0])):
            t.append(grid[j][i])
        t_grid.append(t)
    return t_grid

def swap_rows_small(grid):
    """Обмен двух строк в пределах одного района"""
    row1 = random.randint(0, 8)
    l = list(range(row1//3*3, row1//3*3+3))
    l.remove(row1)
    row2 = random.choice(l)
    grid[row1], grid[row2] = grid[row2], grid[row1]
    return grid

def swap_columns_small(grid):
    """Обмен двух столбцов в пределах одного района"""
    grid = transpose(grid)
    grid = swap_rows_small(grid)
    grid = transpose(grid)
    return grid

def swap_rows_area(grid):
    """Обмен двух районов по горизонтали"""
    row1 = random.randint(0, 2)
    l = list([0, 1, 2])
    l.remove(row1)
    row2 = random.choice(l)
    grid[row1*3:row1*3+3], grid[row2*3:row2*3+3] = grid[row2*3:row2*3+3], grid[row1*3:row1*3+3]
    return grid

def swap_columns_area(grid):
    """Обмен двух районов по вертикали"""
    grid = transpose(grid)
    grid = swap_rows_area(grid)
    grid = transpose(grid)
    return grid

def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """

    grid = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['4', '5', '6', '7', '8', '9', '1', '2', '3'],
        ['7', '8', '9', '1', '2', '3', '4', '5', '6'],
        ['2', '3', '4', '5', '6', '7', '8', '9', '1'],
        ['5', '6', '7', '8', '9', '1', '2', '3', '4'],
        ['8', '9', '1', '2', '3', '4', '5', '6', '7'],
        ['3', '4', '5', '6', '7', '8', '9', '1', '2'],
        ['6', '7', '8', '9', '1', '2', '3', '4', '5'],
        ['9', '1', '2', '3', '4', '5', '6', '7', '8']
    ]
    num_of_mixes = 10
    for i in range(num_of_mixes):
        k = random.randint(1,5)
        if k == 1:
            grid = transpose(grid)
        elif k == 2:
            grid = swap_rows_small(grid)
        elif k == 3:
            grid = swap_columns_small(grid)
        elif k == 4:
            grid = swap_rows_area(grid)
        elif k == 5:
            grid = swap_columns_area(grid)

    N = 81-N
    free_ind = [
        (0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
        (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),
        (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),
        (3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),
        (4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),
        (5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),
        (6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),
        (7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),
        (8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8)
    ]
    for i in range(N):
        to_remove = random.choice(free_ind)
        grid[to_remove[0]][to_remove[1]] = '.'
        free_ind.remove(to_remove)
    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)