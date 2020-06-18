# 1 Task. Stressful Subject
import re


def is_stressful(text: str):
    return (text.isupper() or text.endswith("!!!") or any(re.search('+[.!-]*'.join(c for c in word), text.lower())
                                                          for word in ['help', 'asap', 'urgent']))


if __name__ == '__main__':
    print("Result =", is_stressful('I neeed HELP!!!'))