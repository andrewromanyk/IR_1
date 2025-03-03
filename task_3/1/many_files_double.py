from functools import reduce

import one_file_double as of
import sortedcontainers as sc


def read_all_files(names):
    result = sc.SortedDict()
    for i in range(len(names)):
        print(names[i])
        of.read_file(names[i], i, result)
    return result

def phrase_search(phrase, dictionary: sc.SortedDict):
    phrase = phrase.lower()
    words = phrase.split()
    pairs = [words[i] + " " + words[i+1] for i in range(len(words)-1)]
    results = [dictionary.get(key) for key in pairs]
    result = reduce(lambda x, y: x.intersection(y), results)
    print(result)
    return result


def main(names):
    result = read_all_files(names)
    print(result)
    print(phrase_search("you are a wizard harry", result))
    # write_file(result)
    # write_ser(result)
    # print(read_ser('simple_words_ser.txt'))


if __name__ == '__main__':
    names = ["../../texts/" + i for i in
             [
                 'alice_in_wonderland.fb2',
                 '1984.fb2',
                 'harry_potter_stone.fb2',
                 'harry_potter_chamber.fb2',
                 'harry_potter_stone.fb2',
                 'harry_potter_azkaban.fb2',
                 'harry_potter_cursed_child.fb2',
                 'harry_potter_goblet.fb2',
                 'harry_potter_prince.fb2',
                 'animal_farm.fb2'
             ]
             ]
    main(names)
