import time


last_byte = 0b10000000
suffix_bits = 0b01111111

def num_to_vbc_bin(num):
    result = [(num & suffix_bits) + last_byte]
    num >>= 7
    while num != 0:
        result.append(num & suffix_bits)
        num >>= 7
    return result[::-1]


def flatten(a):
    result = []
    for el in a:
        if type(el) is list:
            for iner in el:
                result.append(iner)
        else:
            result.append(el)
    return result


def encode_index(in_file_name, out_file_name):
    with open(in_file_name, 'r', encoding='utf-8') as in_file, open(out_file_name, 'wb') as out_file:
        for line in in_file:
            # Turn lime into list of offsets
            indeces = [int(i) for i in line.split()[1:]]
            offsets = [indeces[0]]
            for i in range(1, len(indeces)):
                offsets.append(indeces[i] - indeces[i-1])

            offsets_in_bytes = flatten([num_to_vbc_bin(i) for i in offsets])

            out_file.write(bytes(offsets_in_bytes))

            out_file.write(b'\n')

def decode_index(in_file_name, out_file_name):
    with open(in_file_name, 'rb') as in_file, open(out_file_name, 'w', encoding='utf-8') as out_file:
        for line in in_file:
            out_line = []
            curr_num = 0
            for byte in line:
                to_add = byte & suffix_bits
                curr_num = (curr_num << 7) + to_add
                if byte & last_byte == 0b10000000:
                    out_line.append(curr_num)
                    curr_num = 0

            for i in range(1, len(out_line)):
                out_line[i] += out_line[i-1]

            out_file.write(f"{' '.join(str(i) for i in out_line)}\n")


def verify(original, decoded):
    with open(original, "r", encoding='utf-8') as original_file, open(decoded, "r", encoding='utf-8') as decoded_file:
        for line in original_file:
            indeces = line.split()[1:]
            decoded_indeces = decoded_file.readline().split()
            if indeces != decoded_indeces:
                return False
        return True

if __name__ == "__main__":
    start = time.perf_counter()
    encode_index("../../result.txt", "encoded.txt")
    inter = time.perf_counter()
    decode_index("encoded.txt", "out_decoded.txt")
    end = time.perf_counter()

    print(f"The encoding was right: {verify("../../result.txt", "out_decoded.txt")}")
    print(f"Time that it took to encode: {inter - start}")
    print(f"Time that it took to decode: {end - inter}")
    print(f"Overall time: {end - start}")
