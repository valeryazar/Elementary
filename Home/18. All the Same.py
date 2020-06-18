# 18 Task. All the Same
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if len(set(elements)) > 1: return False
    return True


if __name__ == '__main__':
    print("Result =", all_the_same([1, 1, 1]))
