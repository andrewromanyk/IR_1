from functools import reduce

import one_file as of
import sortedcontainers as sc
import basic

def read_all_files(names):
    result = sc.SortedDict()
    for i in range(len(names)):
        print(names[i])
        of.read_file(names[i], i, result)
    return result

def phrase_search(phrase, dictionary: sc.SortedDict, amount):
    phrase = phrase.lower()
    words = phrase.split()
    word_list_pairs = [(key, dictionary.get(key)) for key in words]
    if len(words) == 1:
        return list(word_list_pairs[0][1].keys())
    result = set()
    for file in range(amount):
        words_in_files = [(one[0], one[1].get(file)) for one in word_list_pairs]
        is_liable = True
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                # print(f"ij = {i};{j}" )
                left = words_in_files[i][1]
                right = words_in_files[j][1]
                if left is None or right is None:
                    is_liable = False
                    continue
                # print(left, right)
                right_mod = [el - (j-i) for el in right]
                if len(basic.intersect_sorted_lists(left, right_mod)) == 0:
                    is_liable = False
        if is_liable:
            result.add(file)
    # result = reduce(lambda x, y: x.intersection(y), results)
    # print(result)
    return result


def main(names):
    result = read_all_files(names)
    # print(result)
    print(phrase_search("animal farm", result, 10))
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
