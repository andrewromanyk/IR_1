import xml.etree.ElementTree as ET
import sortedcontainers as sc


def read_file(name: str):
    fb2 = ET.parse(name).getroot()
    return parse_root_tag(fb2)


def parse_root_tag(element: ET.Element) -> [str]:
    words = sc.SortedSet()
    for text in element.itertext():
        words.update(parse_text(text))
    return words


def parse_text(text: str) -> [str]:
    result = []
    word = ""
    for ch in text:
        if is_token(ch):
            word += ch
        else:
            if word != "":
                result.append(word.lower())
                word = ""
    if word != "":
        result.append(word.lower())
    return result


def is_token(ch: str) -> bool:
    return ch.isalnum() or ch in "'`"


if __name__ == '__main__':
    root = read_file('test.xml')
    print(root)
