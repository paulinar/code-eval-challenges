"""https://www.codeeval.com/open_challenges/20/"""

import sys
test_cases = open(sys.argv[1], 'r')

def convert_lowercase(s):
    print(s.lower())

for test in test_cases:
    convert_lowercase(test)

test_cases.close()
