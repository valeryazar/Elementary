# 11 Task. Non-unique Elements
def checkio(data: list) -> list:
    new_data = []
    for i in data:
        if data.count(i) > 1:
            new_data.append(i)
    return new_data


if __name__ == "__main__":
    print("Result =", checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]