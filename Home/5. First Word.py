# 5 Task. First Word
def first_word(text: str) -> str:
    return text.replace(".", " ").replace(",", " ").split()[0]


if __name__ == '__main__':
    print("Result =", first_word("Hello world"))