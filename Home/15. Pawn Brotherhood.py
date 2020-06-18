# 15 Task. Pawn Brotherhood
def safe_pawns(pawns: set) -> int:
    pawns_index = set()
    for n in pawns:
        row = int(n[1]) - 1
        column = ord(n[0]) - 97
        pawns_index.add((row, column))
        count = 0
    for row, column in pawns_index:
        is_safe = ((row - 1, column - 1) in pawns_index) or ((row - 1, column + 1) in pawns_index)
        if is_safe:
            count += 1
    return count


if __name__ == '__main__':
    print("Result =", str(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})))