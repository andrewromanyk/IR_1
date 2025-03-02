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


def parse_text(text: str, file_number, words: sc.SortedDict) -> None:
    word_pair = [None, None]
    word = ""
    for ch in text:
        if basic.is_token(ch):
            word += ch
        else:
            if word != "":
                word_pair[0] = word_pair[1]
                word_pair[1] = word
                if word_pair[0] is not None:
                    words.setdefault(basic.process_word(word_pair[0]) + " " + basic.process_word(word_pair[1]), sc.SortedSet()).add(file_number)
                word = ""
    if word != "":
        word_pair[0] = word_pair[1]
        word_pair[1] = word
        if word_pair[0] is not None:
            words.setdefault(basic.process_word(word_pair[0]) + " " + basic.process_word(word_pair[1]),
                             sc.SortedSet()).add(file_number)


if __name__ == '__main__':
    root = read_file('test.xml')
    print(root)
