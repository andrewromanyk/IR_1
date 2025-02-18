import xml.etree.ElementTree as ET
import sortedcontainers as sc


def read_file(name: str, words=sc.SortedSet()) -> sc.SortedSet:
    fb2 = ET.parse(name).getroot()
    return parse_root_tag(fb2, words)


def parse_root_tag(element: ET.Element, words) -> sc.SortedSet:
    for text in element.itertext():
        parse_text(text, words)
    return words


def parse_text(text: str, words: sc.SortedSet) -> None:
    word = ""
    for ch in text:
        if is_token(ch):
            word += ch
        else:
            if word != "":
                words.add(word.lower())
                word = ""
    if word != "":
        words.add(word.lower())


def is_token(ch: str) -> bool:
    return ch.isalnum() or ch in "'`"


if __name__ == '__main__':
    root = read_file('test.xml')
    print(root)
