import basic
import sortedcontainers as sc
import math
import random
import numpy as np

random.seed(500)

vectors = basic.read_ser("vectors.txt")
vector_amount = len(vectors)

def clusterize():
    amount = int(math.sqrt(vector_amount))
    leaders = random.sample(list(vectors.keys()), amount)
    result = {}
    for k in leaders:
        print(f"[{vectors[k][:10]} - {vectors[k][-10:]}]")
        result[k] = []
    for k, v in vectors.items():
        print(f"k = {k}")
        if k in leaders:
            continue
        curr = np.array(v, dtype=np.float64)
        distances = []
        for leader in leaders:
            lead = np.array(vectors[leader], dtype=np.float64)
            distance = np.dot(lead, curr)/(np.linalg.norm(curr)*np.linalg.norm(lead))
            distances.append([leader, distance])
        print(distances)
        minimum = max(distances, key=lambda x: x[1])[0]
        result[minimum].append(k)
    return result



if __name__ == '__main__':
    # vectors = basic.read_ser("vectors.txt")
    # for k, v in vectors.items():
    #     for i in v:
    #         print(i)
    #     break
    res = clusterize()
    print(res)
    for k, v in res.items():
        print(k, v)