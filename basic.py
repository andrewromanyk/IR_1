import pickle


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