import one_file_perm as of
import sortedcontainers as sc
from functools import reduce


def read_all_files(names):
    result = sc.SortedDict()
    perm = sc.SortedDict()
    for i in range(len(names)):
        print(names[i])
        of.read_file(names[i], i, result, perm)
    return result, perm

def search_joker(phrase, dictionary, perm):
    left, right = phrase.split("*")
    to_search = right + '$' + left
    to_combine = [v for k, v in perm.items() if k.startswith(to_search)]
    # all_keys = [i for i in perm.keys() if i.startswith(to_search)]
    # print(f"keys = {all_keys} for phrase = {phrase}")
    # to_combine = [dictionary.get(key) for key in [i for i in dictionary.keys() if i.startswith(to_search)]]
    result_word_set = reduce(lambda x, y: x.union(y), to_combine)
    print(result_word_set)
    result = [dictionary.get(i) for i in result_word_set]
    return reduce(lambda x, y: x.union(y), result)

def main(names):
    result, perm = read_all_files(names)
    # print(result)
    print(search_joker("har*y", result, perm))
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
