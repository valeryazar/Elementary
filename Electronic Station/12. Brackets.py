# 12 Task. Brackets
def checkio(expression: bool):
    array = []
    for i in expression:
        if i in set(["{", "[", "("]):
            array.append(i)
        if i == "}":
            if len(array) <= 0 or array[-1] != "{":
                return False
            array.pop()
        if i == "]":
            if len(array) <= 0 or array[-1] != "[":
                return False
            array.pop()
        if i == ")":
            if len(array) <= 0 or array[-1] != "(":
                return False
            array.pop()
    if len(array) > 0:
        return False
    return True


if __name__ == '__main__':
    print("Ressult =", checkio("(({[(((1)-2)+3)-3]/3}-3)"))



