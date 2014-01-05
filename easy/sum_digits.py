"""https://www.codeeval.com/open_challenges/21/"""

import sys
test_cases = open(sys.argv[1], 'r')

def sum_digits(n):
    n = int(n)
    sum = 0
    while (n/10 > 0):
        sum += n%10
        n = n//10
    print(sum)


for test in test_cases:
    sum_digits(test)
test_cases.close()
