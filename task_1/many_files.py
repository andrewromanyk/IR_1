import task_1.one_file as of
import sortedcontainers as sc
import pickle


##main function
def read_all_files(names):
    result = sc.SortedSet()
    for name in names:
        print(name)
        of.read_file(name, result)

    return result
##


def write_file(words):
    with open('simple_words.txt', 'w', encoding='UTF-8') as f:
        for word in words:
            f.write(word + '\n')


def write_ser(names: sc.SortedSet):
    with open('simple_words_ser.txt', 'wb') as f:
        pickle.dump(names, f)


def read_ser(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


def main(names):
    result = read_all_files(names)
    print(result)
    # write_file(result)
    # write_ser(result)
    # print(read_ser('simple_words_ser.txt'))


if __name__ == '__main__':
    names = [ "texts/" + i for i in
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
