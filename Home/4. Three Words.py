# 4 Task. Three Words
def checkio(words: str) -> bool:
    i = 0
    for word in words.split():
        if word.isalpha():
            i += 1
        else:
            i = 0
        if i == 3:
            return True
    return False


if __name__ == '__main__':
    print("Result =", checkio("Hello World hello"))