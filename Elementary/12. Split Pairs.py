# 12 Task. Split Pairs
def split_pairs(a):
    if len(a) % 2 == 1:
        a += "_"
    return [a[i:i+2] for i in range(0, len(a), 2)]


if __name__ == '__main__':
    print("Result =", list(split_pairs('abc')))