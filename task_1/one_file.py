import xml.etree.ElementTree as ET
import sortedcontainers as sc
import basic

def read_file(name: str, words=sc.SortedSet()) -> sc.SortedSet:
    fb2 = ET.parse(name).getroot()
    return parse_root_tag(fb2, words)


def parse_root_tag(element: ET.Element, words) -> sc.SortedSet:
    for el in element.iter():
        if el.tag.endswith('binary'): 
            continue
        else:
            text = el.text
            if text != None:
                parse_text(text, words)
    return words


def parse_text(text: str, words: sc.SortedSet) -> None:
    word = ""
    for ch in text:
        if basic.is_token(ch):
            word += ch
        else:
            if word != "":
                words.add(basic.process_word(word))
                word = ""
    if word != "":
        words.add(basic.process_word(word))


if __name__ == '__main__':
    root = read_file('test.xml')
    print(root)
