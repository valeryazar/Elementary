# 1 Task. Words Order
def words_order(text: str, words: list) -> bool:
    if set(words) - set(text.split(' ')):
        return False
    return sorted(set(words), key=text.index) == words


if __name__ == '__main__':
    print("Result =", words_order('hi world im here', ['world', 'here']))