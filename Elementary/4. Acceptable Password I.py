# 4 Task. Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


if __name__ == '__main__':
    print("Result =", is_acceptable_password('short'))