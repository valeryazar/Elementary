# 5 Task. Acceptable Password III
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and any(map(str.isdigit, password)) and any(map(str.isalpha, password))


if __name__ == '__main__':
    print("Result =", is_acceptable_password('123456789'))