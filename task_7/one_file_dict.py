import xml.etree.ElementTree as ET
import sortedcontainers as sc
import basic

free_file = 1

def read_file(name: str, file_number, words=sc.SortedDict()) -> sc.SortedDict:
    fb2 = ET.iterparse(name, events=("start", "end"))
    print(f"-- Started iterpatse object: {basic.current_memory()}")
    parse_root_tag(fb2, file_number, words)
    print(f"-- After full parsing file: {basic.current_memory()}")
    return words


def parse_root_tag(element, file_number, words):
    for event, elem in element:
        if elem.tag.endswith('binary'):
            elem.clear()
            continue
        text = None
        # print(elem.tag, elem.text[:20] if elem.text else None)
        zone = "body"
        if event == "start":
            # print(elem.tag.split("}")[1])
            zone_t = elem.tag.split("}")[1]
            if zone_t in ["first-name", "last-name", "middle-name"]:
                zone = "author"
            elif zone_t == "book-title":
                zone = "title"
            text = elem.text
        elif event == "end":
            # print(elem.tag, elem.text[:20] if elem.text else None)
            text = elem.tail
        # if zone != "body":
        #     print("AHJFAHJFKHAKJFHAF")
        if text:
            # print(f"- Started reading text: {basic.current_memory()}")
            parse_text(text, file_number, words, zone)
        elem.clear()
        # print(f"- Stopped reading text: {basic.current_memory()}")
        # print(basic.current_memory())


def insert_word(word, words, file_number, zone):
    processed = basic.process_word(word)
    if processed == "":
        return
    words.setdefault(processed, sc.SortedSet()).add(f"{file_number}.{zone}")

def parse_text(text: str, file_number, words: sc.SortedDict, zone) -> None:
    word = ""
    for ch in text:
        if basic.is_token(ch):
            word += ch
        else:
            if word != "":
                insert_word(word, words, file_number, zone)
                word = ""
    if word != "":
        insert_word(word, words, file_number, zone)
    

if __name__ == '__main__':
    root = read_file('test.xml')
    print(root)
