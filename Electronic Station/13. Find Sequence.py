# 13 Task. Find Sequence
from typing import List


def checkio(matrix: List[List[int]]) -> bool:
    temp = list(map(list, zip(*reversed(matrix))))
    for grid in (matrix, temp):
        height , width = len(grid) - 3, len(grid[0]) - 3
        for i, row in enumerate(grid):
            for j in range(width):
                if set(row[j:j + 4]) == {row[j]}:
                    return True
                if i < height:
                    if set(grid[i + k][j + k] for k in range(4)) == {row[j]}:
                        return True
    return False


if __name__ == '__main__':
    print("Result =", checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]))