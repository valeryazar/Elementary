# 4 Task. Acceptable Password II
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and any(map(str.isdigit, password))


if __name__ == '__main__':
    print("Result =", is_acceptable_password('short123'))