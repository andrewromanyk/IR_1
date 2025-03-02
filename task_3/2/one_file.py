import xml.etree.ElementTree as ET
import sortedcontainers as sc
import basic

def read_file(name: str, file_number, words=sc.SortedDict()) -> sc.SortedDict:
    fb2 = ET.parse(name).getroot()
    return parse_root_tag(fb2, file_number, words)


def parse_root_tag(element: ET.Element, file_number, words) -> sc.SortedDict:
    index = 1
    for el in element.iter():
        if el.tag.endswith('binary'): 
            continue
        else:
            text = el.text
            if text != None:
                index = parse_text(text, file_number, index, words)
    return words


def parse_text(text: str, file_number, index, words: sc.SortedDict) -> int:
    word = ""
    for ch in text:
        if basic.is_token(ch):
            word += ch
        else:
            index += 1
            if word != "":
                words.setdefault(basic.process_word(word), sc.SortedDict()).setdefault(file_number, sc.SortedList()).add(index)
                word = ""
    if word != "":
        words.setdefault(basic.process_word(word), sc.SortedDict()).setdefault(file_number, sc.SortedList()).add(index)

    return index


if __name__ == '__main__':
    root = read_file('test.xml')
    print(root)
