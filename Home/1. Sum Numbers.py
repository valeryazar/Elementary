# 1 Task. Sum Numbers
def sum_numbers(text: str) -> int:
    return sum([int(n) for n in text.split(" ") if n.isdigit()])


if __name__ == '__main__':
    print("Result =", sum_numbers('5 plus 6 is'))