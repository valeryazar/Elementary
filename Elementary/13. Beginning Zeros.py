# 13 Task. Beginning Zeros
def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))


if __name__ == '__main__':
    print("Result =", beginning_zeros('100'))