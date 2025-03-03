import pickle
import sortedcontainers as sc

def is_token(ch: str) -> bool:
    return ch.isalnum() or ch in "'`@"


def process_word(word: str) -> str:
    word = word.lower()
    if word.startswith("'") and word.endswith("'"):
        word = word[1:-1]
    if word.startswith("'"):
        word = word[1:]
    if word.endswith("'s"):
        word = word[:-2]
    return word


def write_file(words, file_name):
    with open(file_name, 'w', encoding='UTF-8') as f:
        for word in words:
            f.write(word + '\n')


def write_ser(names, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(names, f)


def read_ser(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def intersect_sorted_lists(a, b):
    # print(f"a = {a}")
    # print(f"b = {b}")
    iter_a, iter_b = iter(a), iter(b)
    result = []
    value_a = next(iter_a, None)
    value_b = next(iter_b, None)
    while value_a is not None and value_b is not None:
        if value_a == value_b:
            result.append(value_a)
            value_a = next(iter_a, None)
            value_b = next(iter_b, None)
        elif value_a < value_b:
            value_a = next(iter_a, None)
        else:
            value_b = next(iter_b, None)
    # print(result)
    return sc.SortedList(result)