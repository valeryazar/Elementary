# 8 Task. Remove All Before
from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    return list(items[items.index(border):] if border in items else items)


if __name__ == '__main__':
    print("Result =", list(remove_all_before([1, 2, 3, 4, 5], 3)))
