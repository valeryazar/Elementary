# 10 Task. Between Markers
def between_markers(text: str, begin: str, end: str) -> str:
    # Первая версия (Оно нестабильно работает).
    """
    first = text.find(begin)
    last = text.find(end)
    if first != -1:
        first += len(begin)
    else:
        b = 0
    if last == -1:
        e = len(text)
    return text[first:last]
    """
    # Вторая версия.
    if begin in text:
        first = text.find(begin) + len(begin)
    else:
        first = 0
    if end in text:
        last = text.find(end)
    else:
        last = len(text)
    return text[first:last]


if __name__ == '__main__':
    print("Result =", between_markers('No[/b] hi', '[b]', '[/b]'))