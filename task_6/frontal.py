import time


def common_prefix(words):
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix) and prefix:
            prefix = prefix[:-1]
    return prefix

def write_prefix(words, out_file):
    prefix = common_prefix(words)
    prefix_len = len(prefix)
    to_add = str(len(words[0])) + '*' + prefix + '*' + words[0][prefix_len:]
    for word in words[1:]:
        end = word[prefix_len:]
        to_add += str(len(end)) + '*' + end
    out_file.write(to_add)


def encode(in_file_name, out_file_name):
    with open(in_file_name, "r", encoding='utf-8') as in_file, open(out_file_name, "w", encoding='utf-8') as out_file:
        words = []
        for line in in_file:
            words.append(line.split()[0])
            if len(words) == 4:
                write_prefix(words, out_file)
                words = []
        if words:
            write_prefix(words, out_file)

def decode(in_file_name, out_file_name):
    with open(in_file_name, "r", encoding='utf-8') as in_file, open(out_file_name, "w", encoding='utf-8') as out_file:
        char = 'a'
        curr_word = ""
        while char:
            char = in_file.read(1)
            # Beginning of word. Read length of first word
            word_len = char
            char = in_file.read(1)
            while char.isdigit():
                word_len += char
                char = in_file.read(1)
            word_len = int(word_len)

            char = in_file.read(1)

            #Read prefix and first word
            prefix = ""
            while char != '*':
                prefix += char
                char = in_file.read(1)

            # Read first suffix
            prefix_len = len(prefix)
            suffix_len = word_len - prefix_len
            curr_word = prefix + in_file.read(suffix_len)

            out_file.write(curr_word + "\n")

            # Read subsequent suffixes
            i = 0
            while char and i != 3:
                char = in_file.read(1)
                if not char:
                    break
                suffix_len = ""
                while char.isdigit():
                    suffix_len += char
                    char = in_file.read(1)
                suffix_len = int(suffix_len)

                suffix = in_file.read(suffix_len)

                curr_word = prefix + suffix
                out_file.write(curr_word + "\n")

                i += 1


def verify(original, decoded):
    with open(original, "r", encoding='utf-8') as original_file, open(decoded, "r", encoding='utf-8') as decoded_file:
        for line in original_file:
            word = line.split()[0]
            decoded_word = decoded_file.readline()[:-1]
            if word != decoded_word:
                return False
        return True

if __name__ == "__main__":
    start = time.perf_counter()
    encode("../result.txt", "out_encoded.txt")
    inter = time.perf_counter()
    decode("out_encoded.txt", "out_decoded.txt")
    end = time.perf_counter()
    print(f"The files are the same = {verify('../result.txt', 'out_decoded.txt')}")

    print(f"Time that it took to encode: {inter - start}")
    print(f"Time that it took to decode: {end - inter}")
    print(f"Overall time: {end - start}")