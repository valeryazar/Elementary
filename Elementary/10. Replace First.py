# 10 Task. Replace First
from typing import Iterable


def replace_first(items: list) -> Iterable:
    if items:
        items.append(items.pop(0))
    return items


if __name__ == '__main__':
    print("Result =", list(replace_first([1, 2, 3, 4])))
