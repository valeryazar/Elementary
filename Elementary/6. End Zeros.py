# 6 Task. End Zeros
def end_zeros(num: int) -> int:
    return len(str(num)) - len(str(num).rstrip('0'))


if __name__ == '__main__':
    print("Result =", end_zeros(100))