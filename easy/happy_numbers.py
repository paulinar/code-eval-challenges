"""https://www.codeeval.com/open_challenges/39/"""

import sys
test_cases = open(sys.argv[1], 'r')

def is_happy(num):
    seen = set()
    while True:
        sum_digits = sum(int(i)**2 for i in str(num))
        if sum_digits == 1:
            print(1)
            return
        if sum_digits in seen:
            print(0)
            return
        num = sum_digits
        seen.add(sum_digits)

for test in test_cases:
    is_happy(int(test))
test_cases.close()
