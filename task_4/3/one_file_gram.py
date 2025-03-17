import xml.etree.ElementTree as ET
import sortedcontainers as sc
import basic

def read_file(name: str, file_number, words=sc.SortedDict(), kgram = sc.SortedDict()) -> sc.SortedDict:
    fb2 = ET.parse(name).getroot()
    return parse_root_tag(fb2, file_number, words, kgram)


def parse_root_tag(element: ET.Element, file_number, words, kgram) -> sc.SortedDict:
    for el in element.iter():
        if el.tag.endswith('binary'): 
            continue
        else:
            text = el.text
            if text != None:
                parse_text(text, file_number, words, kgram)
    return words

def set_word(word, words, file_number, kgram):
    processed = basic.process_word(word)
    if processed == "":
        return
    words.setdefault(processed, sc.SortedSet()).add(file_number)
    to_grams = '$' + processed + '$'
    for i in range(len(to_grams) - 2):
        kgram.setdefault(to_grams[i:i+3], sc.SortedSet()).add(processed)


def parse_text(text: str, file_number, words: sc.SortedDict, kgram) -> None:
    word = ""
    for ch in text:
        if basic.is_token(ch):
            word += ch
        else:
            if word != "":
                set_word(word, words, file_number, kgram)
                word = ""
    if word != "":
        set_word(word, words, file_number, kgram)


if __name__ == '__main__':
    root = read_file('test.xml')
    print(root)
