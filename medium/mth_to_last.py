"""https://www.codeeval.com/open_challenges/10/"""

import sys
test_cases = open(sys.argv[1], 'r')

def mth_to_last(elems, m):
    if m > len(elems) + 1:
        return
    else:
        print(elems[len(elems) - m])

for test in test_cases:
    test = test.split()
    last_elem = test[len(test) - 1]
    test.remove(last_elem)
    mth_to_last(test, int(last_elem))
test_cases.close()
