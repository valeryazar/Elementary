# 3 Task. Right to Left
def left_join(string_array: tuple) -> str:
    return (",".join(string_array)).replace("right", "left")


if __name__ == '__main__':
    print("Result =", left_join(("left", "right", "left", "stop")))