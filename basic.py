import pickle
import sortedcontainers as sc
import psutil
import os

MAX_RAM = 128  #mb

list_of_files = [
    'alice_in_wonderland.fb2',
    '1984.fb2',
    'harry_potter_stone.fb2',
    'harry_potter_chamber.fb2',
    'harry_potter_phoenix.fb2',
    'harry_potter_azkaban.fb2',
    'harry_potter_cursed_child.fb2',
    'harry_potter_goblet.fb2',
    'harry_potter_prince.fb2',
    'animal_farm.fb2',
    'ancient_mariner.fb2',
    'greatest_show.fb2',
    'red_bandit.fb2',
    'dragon_prophecy.fb2'
]

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


def union_sorted_lists(a, b):
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
            result.append(value_a)
            value_a = next(iter_a, None)
        else:
            result.append(value_b)
            value_b = next(iter_b, None)
    while value_a:
        result.append(value_a)
        value_a = next(iter_a, None)
    while value_b:
        result.append(value_b)
        value_b = next(iter_b, None)
    return result



def current_memory():
    process = psutil.Process(os.getpid())
    memory_use = process.memory_info().rss / (1024 * 1024)
    return memory_use

def is_memory_full():
    return current_memory() >= MAX_RAM