"""https://www.codeeval.com/open_challenges/12/"""

import sys
test_cases = open(sys.argv[1], 'r')

def first_non_repeating(string):
    
    characters = []
    for char in string:
        characters.append(char)
    
    i = 0
    while i < len(characters):
        if characters.count(characters[i]) == 1:
            print(characters[i])
            return
        else:
            i += 1
    return

for test in test_cases:
    first_non_repeating(str(test))
test_cases.close()
