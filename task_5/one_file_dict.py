import xml.etree.ElementTree as ET
import sortedcontainers as sc
import basic

free_file = 1

def read_file(name: str, file_number, words=sc.SortedDict()) -> sc.SortedDict:
    fb2 = ET.iterparse(name, events=("start", "end"))
    print(f"-- Started iterpatse object: {basic.current_memory()}")
    to_return = parse_root_tag(fb2, file_number, words)
    print(f"-- After full parsing file: {basic.current_memory()}")
    return to_return


def parse_root_tag(element, file_number, words) -> sc.SortedDict:
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
            parse_text(text, file_number, words)
        elem.clear()
        # print(f"- Stopped reading text: {basic.current_memory()}")
        # print(basic.current_memory())
    return words


def insert_word(word, words, file_number):
    processed = basic.process_word(word)
    if processed == "":
        return
    words.setdefault(processed, sc.SortedSet()).add(file_number)

def parse_text(text: str, file_number, words: sc.SortedDict) -> None:
    word = ""
    for ch in text:
        if basic.is_token(ch):
            word += ch
        else:
            if word != "":
                insert_word(word, words, file_number)
                word = ""
                if basic.is_memory_full():
                    print("---- Memory full, writing")
                    write_dict_to_file(words)
    if word != "":
        insert_word(word, words, file_number)


def write_dict_to_file(dictionary: sc.SortedDict):
    global free_file
    if free_file > 12:
        raise "OOOPS. Too many files created"
    with open(f"blocks/{free_file}.txt", "w", encoding='utf-8') as f:
        for k, v in dictionary.items():
            line = str(k)
            for i in v:
                line += f" {i}"
            line += '\n'
            # print(line)
            f.write(line)
    free_file += 1
    print(f"--- Before clearing dict: {basic.current_memory()}")
    dictionary.clear()
    print(f"--- After clearing dict: {basic.current_memory()}")
    


if __name__ == '__main__':
    root = read_file('test.xml')
    print(root)
