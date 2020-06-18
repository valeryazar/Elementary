# 2 Task. Sort by Extension
from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    return sorted(files, key=lambda x: x.split('.')[-1] if x.split('.')[-2] != '' else x.split('.')[0])


if __name__ == '__main__':
    print("Result =", sort_by_ext(['1.cad', '1.bat', '1.aa']))