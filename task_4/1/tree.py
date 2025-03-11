from operator import contains

import many_files as mf


class TreeNode:
    def __init__(self, char_range=None):
        self.char_range = char_range
        self.left_child = None
        self.right_child = None
        self.terms = []

    def __str__(self):
        return f"Node({self.char_range})"

    def print_left(self):
        if self.left_child:
            return str(self) + '\n' + self.left_child.print_left()
        return f"Node({self.terms})"

    def print_right(self):
        if self.right_child:
            return str(self) + '\n' + self.right_child.print_right()
        return f"Node({self.terms})"


    def all_terms(self) -> list:
        if len(self.terms) != 0:
            return self.terms
        left = self.left_child.all_terms() if self.left_child is not None else []
        right = self.right_child.all_terms() if self.right_child is not None else []
        left.extend(right)
        return left

    def all_terms_right(self) -> list:
        if len(self.terms) != 0:
            return self.terms
        # left = self.left_child.all_terms() if self.left_child is not None else []
        right = self.right_child.all_terms() if self.right_child is not None else []
        # left.extend(right)
        right.extend(self.terms)
        return right


    def get_left_right_range(self):
        return self.char_range.split('-')

    def in_range(self, chars):
        left_range, right_range = self.get_left_right_range()
        # print(f"check if '{chars}' is in '{left_range}' and '{right_range}'")
        for (i, j) in zip(left_range, chars):
            if ord(i) < ord(j):
                break
            elif ord(i) == ord(j):
                continue
            else:
                return False
        for (i, j) in zip(chars, right_range):
            if ord(i) < ord(j):
                break
            elif ord(i) == ord(j):
                continue
            else:
                return False
        # print("It is!")
        return True

    def find_joker(self, expr):
        left_range, right_range = self.get_left_right_range()
        # if self.terms and self.terms[0].startswith(expr):
        #     return self.terms
        result = []

        if len(self.right_child.get_left_right_range()) == 1:
            token = self.right_child.get_left_right_range()[0]
            if token.startswith(expr):
                result.append(token)
        else:
            right_range_1, right_range_2 = self.right_child.get_left_right_range()
            if right_range.startswith(expr) and right_range_2.startswith(expr):
                result.extend(self.right_child.all_terms())
            elif self.right_child.in_range(expr):
                result.extend(self.right_child.find_joker(expr))
        if len(self.left_child.get_left_right_range()) == 1:
            token = self.left_child.get_left_right_range()[0]
            if token.startswith(expr):
                result.append(token)
        else:
            left_range_1, left_range_2 = self.left_child.get_left_right_range()
            if left_range.startswith(expr) and left_range_1.startswith(expr):
                result.extend(self.left_child.all_terms())
            elif self.left_child.in_range(expr):
                result.extend(self.left_child.find_joker(expr))

        # if left_range.startswith(expr):
        #     result.extend(self.left_child.all_terms())
        # if right_range.startswith(expr):
        #     result.extend(self.right_child.all_terms())
        # if self.left_child.in_range(expr):
        #     result.extend(self.left_child.find_joker(expr))
        # elif self.right_child.in_range(expr):
        #     result.extend(self.right_child.find_joker(expr))
        return result



def build_dictionary_tree(terms):
    return build_tree(terms, 0, len(terms) - 1, "")


def build_tree(terms, start_idx, end_idx, orientation):
    # one term
    if start_idx == end_idx:
        node = TreeNode(terms[start_idx])
        node.terms.append(terms[start_idx])
        return node

    # two terms
    if end_idx - start_idx == 1:
        first_letter_start = terms[start_idx][0].lower()
        first_letter_end = terms[end_idx][0].lower()
        char_range = f"{first_letter_start}-{first_letter_end}"

        node = TreeNode(char_range)

        left_node = TreeNode(terms[start_idx])
        left_node.terms.append(terms[start_idx])

        right_node = TreeNode(terms[end_idx])
        right_node.terms.append(terms[end_idx])

        node.left_child = left_node
        node.right_child = right_node

        return node

    mid = (start_idx + end_idx) // 2

    if orientation == "right":
        first_letter_start = terms[start_idx][0].lower()
        previous_letter_start = terms[start_idx - 1][0].lower()
        i = 1
        while first_letter_start == previous_letter_start:
            i += 1
            first_letter_start = terms[start_idx][0:i].lower()
            previous_letter_start = terms[start_idx - 1][0:i].lower()
    else:
        first_letter_start = terms[start_idx][0].lower()

    if orientation == "left":
        first_letter_end = terms[end_idx][0].lower()
        next_letter_start = terms[end_idx+1][0].lower()
        i = 1
        while first_letter_end == next_letter_start:
            i += 1
            first_letter_end = terms[end_idx][0:i].lower()
            next_letter_start = terms[end_idx+1][0:i].lower()
    else:
        first_letter_end = terms[end_idx][0].lower()


    char_range = f"{first_letter_start}-{first_letter_end}"

    node = TreeNode(char_range)

    node.left_child = build_tree(terms, start_idx, mid, "left")
    node.right_child = build_tree(terms, mid + 1, end_idx, "right")

    return node


def main():
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
    terms = mf.read_all_files(names)
    tree = build_dictionary_tree(terms)
    # print(tree.all_terms())
    # print([x for x in tree.all_terms() if x.startswith("harry")])
    print(tree.find_joker('ouch'))

if __name__ == '__main__':
    main()
