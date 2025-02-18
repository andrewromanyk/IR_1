import one_file as of
import sortedcontainers as sc


def read_all_files(names):
    result = sc.SortedSet()
    for name in names:
        print(name)
        of.read_file(name, result)

    return result


def main(names):
    result = read_all_files(names)

    print(repr(result))


if __name__ == '__main__':
    names = [ "texts/" + i for i in
                    ['alice_in_wonderland.fb2',
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
