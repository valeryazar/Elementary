# 2 Task. Easy Unpack
def easy_unpack(elements: tuple) -> tuple:
    return (elements[0], elements[2], elements[-2])


if __name__ == '__main__':
    print("Result =", easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))