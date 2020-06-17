# 7 Task. Count Digits
def count_digits(text: str) -> int:
    return len([i for i in text if i.isdigit()])


if __name__ == '__main__':
    print("Result =", count_digits('5 plus 6 is'))