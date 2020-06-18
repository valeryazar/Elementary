# 13 Task. Sort Array by Element Frequency
def frequency_sort(items):
    return sorted(sorted(items, key=items.index), key=items.count, reverse=True)


if __name__ == '__main__':
    print("Result =", frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))