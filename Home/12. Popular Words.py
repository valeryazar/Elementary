# 12 Task. Popular Words
def popular_words(text: str, words: list) -> dict:
    new_text = text.lower().split()
    result = {}
    for word in words:
        result[word] = new_text.count(word)
    return result


if __name__ == '__main__':
    print("Result =", popular_words('''
    When I was One
    I had just begun
    When I was Two
    I was nearly new
    ''', ['i', 'was', 'three', 'near']))