"""https://www.codeeval.com/open_challenges/41/"""

import sys
test_cases = open(sys.argv[1], 'r')

def duplicate_finder(size, arr_elems):
    seen_so_far = []
    i = 0
    while (i < size):
        if (arr_elems[i] not in seen_so_far):
            seen_so_far.append(arr_elems[i])
            i += 1
        else:
            print(arr_elems[i])
            return

for test in test_cases:
    test = test.split(';')
    test[1] = test[1].split(',')  
    duplicate_finder(int(test[0]), test[1])
test_cases.close()
