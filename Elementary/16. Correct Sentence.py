# 16 Task. Correct Sentence
def correct_sentence(text: str) -> str:
    if text[0].islower():
        text = text[0].upper() + text[1:]
    if text[-1] != '.':
        text += '.'
    return text


if __name__ == '__main__':
    print("Result =", correct_sentence("greetings, friends"))
