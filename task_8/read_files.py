import basic
import xml.etree.ElementTree as ET
import sortedcontainers as sc
import math

files_names = basic.read_ser("read_files.txt")
amount_of_files = len(files_names)

def read_index(file_name = "result.txt"):
    dictionary = sc.SortedDict()
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            values = line.split(" ")
            term = values[0]
            values = [int(i) for i in values[1:]]
            dictionary[term] = values
    return dictionary

index = read_index()
print(index)
amount_of_words = len(index)

def read_file(name: str, words=sc.SortedDict()) -> sc.SortedDict:
    fb2 = ET.iterparse(name, events=("start", "end"))
    try:
        parse_root_tag(fb2, words)
    except:
        print(f"Can't parse {name}")
    return words


def parse_root_tag(element, words):
    for event, elem in element:
        if elem.tag.endswith('binary'):
            elem.clear()
            continue
        text = None
        if event == "start":
            text = elem.text
        elif event == "end":
            text = elem.tail
        if text:
            # print(f"- Started reading text: {basic.current_memory()}")
            parse_text(text, words)
        elem.clear()
    return words



def parse_text(text: str, words: sc.SortedDict) -> None:
    word = ""
    for ch in text:
        if basic.is_token(ch):
            word += ch
        else:
            if word != "":
                process = basic.process_word(word)
                if process != "":
                    words.setdefault(process, 0)
                    words[process] += 1
                word = ""
    if word != "":
        process = basic.process_word(word)
        if process != "":
            words.setdefault(process, 0)
            words[process] += 1


def tfidf_all(file_num):
    try:
        print(files_names[file_num])
        all = read_file(files_names[file_num])
    except:
        print("_________________ААА______________")
        return sc.SortedDict()
    result = dict()
    for k, v in all.items():
        try:
            local_len = len(index[k])
        except:
            print(f"{k} OOPS")
            continue
        # print("v", v)
        # print("log", math.log(amount_of_files/local_len, 2))
        result[k] = v*math.log(amount_of_files/local_len, 10)
    return result

def vector(file_num):
    vector = []
    all = tfidf_all(file_num)
    for word in index.keys():
        vector.append(all.get(word, 0))
    return vector


def all_vectors():
    vectors = dict()
    for i in range(amount_of_files):
        print(f"file {i}")
        vectors[i] = vector(i)
    return vectors

if __name__ == '__main__':
    vectors = all_vectors()
    basic.write_ser(vectors, "vectors.txt")