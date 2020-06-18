# 3 Task. Digits Multiplication
def checkio(number: int) -> int:
    result = 1
    for i in str(number):
        if i != '0': result *= int(i)
    return result


if __name__ == '__main__':
    print("Result =", checkio(123405))
