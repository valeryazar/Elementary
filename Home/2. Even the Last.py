# 2 Task. Even the Last
def checkio(array):
    if len(array) >= 1:
        return (sum(array[0::2])) * array[-1]
    else:
        return 0


if __name__ == '__main__':
    print("Result =", checkio([0, 1, 2, 3, 4, 5]))