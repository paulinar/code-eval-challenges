"""https://www.codeeval.com/open_challenges/37/"""

import sys
test_cases = open(sys.argv[1], 'r')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def pangrams(characters):
    missing_letters = ''
    for letter in alphabet:
        if letter not in characters:
            missing_letters += letter
    if missing_letters == '':
        print('NULL')
    else:
        print(missing_letters)
    return

for test in test_cases:
    pangrams(str(test))
test_cases.close()
