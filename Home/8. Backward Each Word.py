# 8 Task. Backward Each Word
def backward_string_by_word(text: str) -> str:
    for i in text.split(' '):
        text = text.replace(i, i[::-1])
    return text


if __name__ == '__main__':
    print("Result =", backward_string_by_word('hello world'))