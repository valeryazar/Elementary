# 14 Task. Surjection Strings
def isometric_strings(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    temp = {}
    for index_1, index_2 in zip(str1, str2):
        if index_1 in temp and temp[index_1] != index_2:
            return False
        else:
            temp[index_1] = index_2
    return True


if __name__ == '__main__':
    print("Result =", isometric_strings('add', 'egg'))