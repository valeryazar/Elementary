# 10 Task. Ascending List
from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    return sorted(set(items)) == items


if __name__ == '__main__':
    print("Result =", is_ascending([-5, 10, 99, 123456]))