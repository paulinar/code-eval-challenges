"""https://www.codeeval.com/open_challenges/71/"""

import sys
import itertools
test_cases = open(sys.argv[1], 'r')

def reverse_groups(arr, k):
    chunked_arr = chunkify(arr, k)
    num_chunks = len(arr)//k
    i = 0
    while i < num_chunks:
        chunked_arr[i].reverse()
        i += 1
    reversed_arr = list(itertools.chain(*chunked_arr))
    print(str(reversed_arr).strip('[]').replace(", ", ",").replace("'", ""))

def chunkify(arr, k):
    return [arr[i:i+k] for i in range(0, len(arr), k)]

for test in test_cases:
    test = test.split(';') 
    test[0] = test[0].split(',')
    reverse_groups(test[0], int(test[1]))
test_cases.close()
