# 14 Task. Nearest Value
def nearest_value(values: set, one: int) -> int:
    return min((abs(n - one), n) for n in values)[1]


if __name__ == '__main__':
    print("Result =", nearest_value({4, 7, 10, 11, 12, 17}, 9))