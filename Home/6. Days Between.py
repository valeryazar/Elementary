# 6 Task. Days Between
from datetime import date


def days_diff(a, b):
    return abs((date(*b) - date(*a)).days)


if __name__ == '__main__':
    print("Result =", days_diff((2020, 6, 15), (2020, 6, 26)))
