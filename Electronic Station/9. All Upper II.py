# 9 Task. All Upper II
def is_all_upper(text: str) -> bool:
    return text.replace('', ' ').isupper()


if __name__ == '__main__':
    print("Result =", is_all_upper('ALL UPPER'))