# 11 Task. Max Digit
def max_digit(number: int) -> int:
    return int(max(str(number)))


if __name__ == '__main__':
    print("Result =", max_digit(123))
