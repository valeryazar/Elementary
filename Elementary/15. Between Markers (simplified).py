# 15 Task. Between Markers (simplified)
def between_markers(text: str, begin: str, end: str) -> str:
    return (text.split(begin)[1]).split(end)[0]


if __name__ == '__main__':
    print('Result =', between_markers('What is >apple<', '>', '<'))