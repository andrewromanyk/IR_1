from functools import reduce

import one_file_dict as of
import sortedcontainers as sc
import os
import basic
import time
import pickle

def any_not_eof(lines):
    # print(lines)
    return reduce(lambda x, y: x or y, lines)


def count_files(directory):
    return len([name for name in os.listdir(directory)])


def combine_all_blocks():
    freefile = count_files("blocks/")
    files = [open("blocks/" + str(i) + ".txt", 'r', encoding='utf-8') for i in range(1, freefile+1)]
    print(files)
    with open("../task_8/result.txt", "w", encoding='utf-8') as f:
        lines = [f.readline() for f in files]
        print("started writing")
        while any_not_eof(lines):
            pairs = [
                (line.split(' ')[0], [int(i) for i in line.split(' ')[1:]]) for line in lines
            ]
            smallest_word = pairs[0][0]
            smallest_files_indices = [0]
            for (i, (x, _)) in enumerate(pairs[1:]):
                if x == '':
                    continue
                if x < smallest_word:
                    smallest_word = x
                    smallest_files_indices = [i+1]
                elif x == smallest_word:
                    smallest_files_indices.append(i+1)
            lists_of_files = [pairs[i][1] for i in smallest_files_indices]
            merged_list = reduce(lambda a, b: basic.union_sorted_lists(a, b), lists_of_files)
            line = smallest_word
            for i in merged_list:
                line += " " + str(i)
            f.write(line + "\n")
            # print(smallest_files_indices)
            # print(lines)
            for i in smallest_files_indices:
                lines[i] = files[i].readline()



def all_file_names(directory="../texts/"):
    all_items = os.listdir(directory)
    print(all_items)
    files = [directory + item for item in all_items]
    return files



def read_all_files(names = all_file_names()):
    os.makedirs("blocks", exist_ok=True)
    result = sc.SortedDict()
    for i in range(len(names)):
        print(names[i])
        of.read_file(names[i], i, result)
    if len(result) != 0:
        of.write_dict_to_file(result)
    combine_all_blocks()
    return result


def main():
    start = time.perf_counter()
    result = read_all_files()
    end = time.perf_counter()
    print(f"- Finished in {end - start} seconds")
    for i in range(1, count_files("blocks/")+1):
        print(f"-- Size of file {i}.txt is {(os.stat(f'blocks/{i}.txt').st_size / 1024):.2f} kb")
    print(f"- Size of result.txt is {(os.stat('../task_8/result.txt').st_size / 1024):.2f}kb")



if __name__ == '__main__':
    # names = ["../texts/" + i for i in basic.list_of_files]
    # print(all_file_names())
    # basic.write_ser(all_file_names(), "../task_8/read_files.txt")
    main()
