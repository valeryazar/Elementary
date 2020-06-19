# 15 Task. Mathematically Lucky Tickets
def checkio(data: str) -> bool:
    return 100 not in check_value(data)


def check_value(value: str) -> set:
    from operator import add, sub, mul, truediv as div
    number = int(value)
    result = {number}
    for position in range(1, len(value)):
        left = value[:position]
        right = value[position:]
        for left_operand in check_value(left):
            for operation in add, sub, mul, div:
                for right_operand in check_value(right):
                    try:
                        current_result = operation(left_operand, right_operand)
                    except ZeroDivisionError:
                        pass
                    else:
                        result.add(current_result)
    return result


if __name__ == '__main__':
    print("Result =", checkio('012395'))