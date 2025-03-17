import one_file_dict as of
import sortedcontainers as sc
import boolean_expr as be


def read_all_files(names):
    result = sc.SortedDict()
    for i in range(len(names)):
        print(names[i])
        of.read_file(names[i], i, result)
    return result


def bool_search_dict(expression, dictionary):
    return be.bool_search(expression, dictionary.get)


def main(names):
    result = read_all_files(names)
    print(result)
    print(bool_search_dict("(harry AND potter AND (NOT azkaban)) OR (comrade)", result))
    # write_file(result)
    # write_ser(result)
    # print(read_ser('simple_words_ser.txt'))


if __name__ == '__main__':
    names = ["../texts/" + i for i in
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
