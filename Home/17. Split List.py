# 17 Task. Split List
import math


def split_list(items: list) -> list:
    array = math.ceil(len(items) / 2)
    return [items[:array], items[array:]]


if __name__ == '__main__':
    print("Result =", split_list([1, 2, 3, 4, 5, 6]))