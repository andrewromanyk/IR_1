import xml.etree.ElementTree as ET
import sortedcontainers as sc
import basic

def read_file(name: str, file_number, words=sc.SortedDict()) -> sc.SortedDict:
    fb2 = ET.parse(name).getroot()
    return parse_root_tag(fb2, file_number, words)


def parse_root_tag(element: ET.Element, file_number, words) -> sc.SortedDict:
    for el in element.iter():
        if el.tag.endswith('binary'): 
            continue
        else:
            text = el.text
            if text != None:
                parse_text(text, file_number, words)
    return words

def set_word(word, words, file_number):
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
                set_word(word, words, file_number)
                word = ""
    if word != "":
        set_word(word, words, file_number)


if __name__ == '__main__':
    root = read_file('test.xml')
    print(root)
