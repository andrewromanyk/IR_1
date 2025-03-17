import one_file_gram as of
import sortedcontainers as sc
from functools import reduce


def read_all_files(names):
    result = sc.SortedDict()
    kgram = sc.SortedDict()
    for i in range(len(names)):
        print(names[i])
        of.read_file(names[i], i, result, kgram)
    return result, kgram

def divide_into_grams(word, result):
    for i in range(len(word) - 2):
        result.append(word[i:i+3])

def search_joker(phrase, dictionary, kgram):
    if not phrase.startswith('*'):
        phrase = '$' + phrase
    if not phrase.endswith('*'):
        phrase = phrase + '$'
    left, right = phrase.split('*')
    # print(left, right)
    to_search = []
    divide_into_grams(left, to_search)
    divide_into_grams(right, to_search)
    # print(to_search)
    keys = kgram.keys()
    found_words = [kgram[i] for i in to_search if i in keys]
    # print(found_words)
    needed_words = reduce(lambda x, y: x.intersection(y), found_words)
    # print(needed_words)
    to_combine = [dictionary.get(key) for key in needed_words]
    result = reduce(lambda x, y: x.union(y), to_combine)
    return result

def main(names):
    result, kgram = read_all_files(names)
    # print(result)
    # print(kgram)
    print(search_joker("car*ot", result, kgram))
    # print(bool_search_dict("(harry AND potter AND (NOT azkaban)) OR (animal AND farm AND comrade)", result))
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
                 'harry_potter_phoenix.fb2',
                 'harry_potter_azkaban.fb2',
                 'harry_potter_cursed_child.fb2',
                 'harry_potter_goblet.fb2',
                 'harry_potter_prince.fb2',
                 'animal_farm.fb2'
             ]
             ]
    main(names)
