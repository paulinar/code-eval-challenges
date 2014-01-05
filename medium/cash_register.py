"""https://www.codeeval.com/open_challenges/54/"""

import sys
test_cases = open(sys.argv[1], 'r')

register = {
    0.01: 'PENNY',
    0.05: 'NICKEL',
    0.10: 'DIME',
    0.25: 'QUARTER',
    0.50: 'HALF DOLLAR',
    1.00: 'ONE',
    2.00: 'TWO',
    5.00: 'FIVE',
    10.00: 'TEN',
    20.00: 'TWENTY',
    50.00: 'FIFTY',
    100.00: 'ONE HUNDRED',
    }

def change_maker(PP, cash):
    if cash < PP:
        print('ERROR')
    if cash == PP:
        print('ZERO')
    else:
        global output_so_far
        output_so_far = []
        change = (cash - PP)
        for key in register:
            if change in register:
                print(str(register[change].replace("'", "")))
                return
        calculate(change)
        print(str(output_so_far).strip('[]').replace(", ", ",").replace("'", ""))          

def calculate(change):
    if (100.00 < change):
        change -= 100.00
        output_so_far.append(register[100.00])
        calculate(change)
    elif (50.00 < change < 100):
        change -= 50.00
        output_so_far.append(register[50.00])
        calculate(change)
    elif (20.00 < change < 50.00):
        change -= 20.00
        output_so_far.append(register[20.00])
        calculate(change)
    elif (10.00 < change < 20.00):
        change -= 10.00
        output_so_far.append(register[10.00])
        calculate(change)
    elif (5.00 < change < 10.00):
        change -= 5.00
        output_so_far.append(register[5.00])
        calculate(change)
    elif (2.00 < change < 5.00):
        change -= 2.00
        output_so_far.append(register[2.00])
        calculate(change)
    elif (1.00 < change < 2.00):
        change -= 1.00
        output_so_far.append(register[1.00])
        calculate(change)
    elif (0.50 < change < 1.00):
        change -= 0.50
        output_so_far.append(register[0.50])
        calculate(change)
    elif (0.25 < change < 0.50):
        change -= 0.25
        output_so_far.append(register[0.25])
        calculate(change)
    elif (0.10 < change < 0.25):
        change -= 0.10
        output_so_far.append(register[0.10])
        calculate(change)
    elif (0.05 < change < 0.10):
        change -= 0.05
        output_so_far.append(register[0.05])
        calculate(change)
    elif (0.01 < change < 0.05):
        change -= 0.01
        output_so_far.append(register[0.01])
        calculate(change)
    else:
        if change in register:
            output_so_far.append(register[change])

for test in test_cases:
    test = test.split(';')
    change_maker(float(test[0]), float(test[1]))
test_cases.close()
