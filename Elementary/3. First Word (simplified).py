# 3 Task. First Word (simplified)
def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ').strip()
    text = text.split()
    return text[0]


if __name__ == '__main__':
    print("Result =", first_word("Hello world"))