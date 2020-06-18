# 13 Task. Second Index
def second_index(text: str, symbol: str) -> [int, None]:
    if 2 > text.count(symbol):
        return None
    else:
        return text.find(symbol, text.find(symbol) + 1);


if __name__ == '__main__':
    print("Result =", second_index("My name is Valera.", "e"))