from functools import reduce

import one_file_dict as of
import sortedcontainers as sc
import os
import basic
import time


def any_not_eof(lines):
    # print(lines)
    return reduce(lambda x, y: x or y, lines)


def count_files(directory):
    return len([name for name in os.listdir(directory)])

def all_file_names(directory="../texts/"):
    all_items = os.listdir(directory)
    files = [directory + item for item in all_items]
    return files

def read_all_files(names):
    os.makedirs("blocks", exist_ok=True)
    result = sc.SortedDict()
    for i in range(len(names)):
        print(names[i])
        of.read_file(names[i], i, result)
    return result

def find(diction: sc.SortedDict, author = "", title = "", body = ""):
    files = []

    if author:
        authors = author.split(" ")
        author_lists = [int(j.split('.')[0]) for j in basic.flatten([diction.get(i) for i in authors]) if j.split('.')[1] == "author"]
        files.extend(author_lists)

    if title:
        titles = title.split(" ")
        title_lists =  [int(j.split('.')[0]) for j in basic.flatten([diction.get(i) for i in titles]) if j.split('.')[1] == "title"]
        if files:
            files = basic.intersect_sorted_lists(files, title_lists)
        else:
            files = title_lists

    if body:
        bodys = body.split(" ")
        body_lists =  [int(j.split('.')[0]) for j in basic.flatten([diction.get(i) for i in bodys]) if j.split('.')[1] == "body"]
        if files:
            files = basic.intersect_sorted_lists(files, body_lists)
        else:
            files = body_lists

    return files



def main():
    files = all_file_names()[:11]
    files.append("../texts/pg1068.fb2")
    print(files)
    names = ["../texts/" + i for i in files]
    result = read_all_files(names)
    print(result)
    print(result.get("ulysses"))
    print(result.get("battle"))
    print(find(result, "ulysses", "", "battle"))



if __name__ == '__main__':
    main()
