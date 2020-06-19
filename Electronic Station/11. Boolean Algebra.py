# 11 Task. Boolean Algebra
OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x: int, y: int, operation: str):
    if operation == "conjunction":
        return 1 if x == 1 and y == 1 else 0
    if operation == "disjunction":
        return 0 if x == 0 and y == 0 else 1
    if operation == "implication":
        return 0 if x == 1 and y == 0 else 1
    if operation == "exclusive":
        return 0 if (x == 1 and y == 1) or (x == 0 and y == 0) else 1
    if operation == "equivalence":
        return 1 if (x == 1 and y == 1) or (x == 0 and y == 0) else 0


if __name__ == '__main__':
    print("1 0 - конъюнкция =", boolean(1, 0, "conjunction"))
    print("1 0 - дизъюнкция =", boolean(1, 0, "disjunction"))
    print("1 1 - импликация =", boolean(1, 1, "implication"))
    print("0 1 - исключение =", boolean(0, 1, "exclusive"))
    print("0 1 - эквивалентность =", boolean(0, 1, "equivalence"))