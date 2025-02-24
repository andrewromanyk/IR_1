import random

import task_1.many_files as mf
import many_files_dict as mfd
import scipy.sparse as sparse
import time


def sorteddict_to_matrix(sorteddict, file_number):
    scr_matrix = sparse.lil_array((len(sorteddict.keys()), file_number), dtype=int)
    for index, (key, value) in enumerate(sorteddict.items()):
        for file in value:
            scr_matrix[index, value] = 1

    return scr_matrix.tocsr()


def test_access_time_dict(dictionary):
    start_time = time.perf_counter()
    for key in dictionary.keys():
        value = dictionary[key]
    end_time = time.perf_counter()
    print("Time for overall access: ", end_time - start_time)
    print("Time for overall access for each: ", (end_time - start_time)/len(dictionary))



def test_access_time_matrix(matrix, set_of_names):
    keys, _ = matrix.shape
    overall = 0
    for i in range(1000):
        index = random.randint(0, keys-1)
        word = set_of_names[index]
        start_time = time.perf_counter()
        index = set_of_names.index(word)
        value = matrix[index]
        end_time = time.perf_counter()
        overall += end_time - start_time
    print("Time for overall access: ", overall)
    print("Time for overall access for each: ", overall / keys)


def main(names):
    start = time.perf_counter()
    dictionary = mfd.read_all_files(names)
    breakpoint_1 = time.perf_counter()
    matrix = sorteddict_to_matrix(dictionary, 10)
    end = time.perf_counter()
    print("How much time took to create dictionary in seconds: ", breakpoint_1 - start)
    print("How much time took to create matrix in seconds: ", end - start)
    print("How much time took to create matrix from fict in seconds: ", end - breakpoint_1)

    words_set = mf.read_all_files(names)

    print("access time for dictionary")
    test_access_time_dict(dictionary)
    print("access time for matrix")
    test_access_time_matrix(matrix, words_set)
    print("access time for matrix array")
    test_access_time_matrix(matrix.toarray(), words_set)
    print(matrix.toarray()[1])
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
                 'harry_potter_stone.fb2',
                 'harry_potter_azkaban.fb2',
                 'harry_potter_cursed_child.fb2',
                 'harry_potter_goblet.fb2',
                 'harry_potter_prince.fb2',
                 'animal_farm.fb2'
             ]
             ]
    main(names)

