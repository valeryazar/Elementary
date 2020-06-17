# 9 Task. Bigger Price
def bigger_price(limit: int, data: list) -> list:
    last_index = len(data) - 1
    for i in range(0, last_index):
        for j in range(0, last_index - i):
            if data[j]["price"] < data[j + 1]["price"]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data[:limit]


if __name__ == '__main__':
    print('Result =', bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))