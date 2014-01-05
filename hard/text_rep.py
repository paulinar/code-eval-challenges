"""https://www.codeeval.com/open_challenges/52/"""

import sys
test_cases = open(sys.argv[1], 'r')

ones = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    }

tens = {
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety'
    }

teens = {
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',    
    }

def text_rep(num):

    num = int(num)

    if (num > 99999999): # in the 100,000,000's        
        remainder = num % 100000000
        if (remainder == 0):
            return ones[num // 100000000] + "HundredMillion"
        else:
            return ones[num // 100000000] + "Hundred" + text_rep(remainder)

    if (99999999 >= num) & (num > 9999999): # in the 10,000,000's 
        first_digit = num // 10000000
        remainder = num % 10000000
        if (remainder == 0): 
            return tens[first_digit] + "Million"
        if (first_digit == 1): 
            return teens[num // 1000000] + "Million" + text_rep(num % 1000000)
        elif ((num // 1000000) % 10 == 0): # check if 2nd digit is a zero
            return tens[first_digit] + "Million" + text_rep(remainder)
        else:
            return tens[first_digit] + text_rep(remainder)

    if (9999999 >= num) & (num > 999999): # in the 1,000,000's 
        first_digit = num // 1000000
        remainder = num % 1000000
        if (remainder == 0): 
            return ones[first_digit] + "Million"
        return ones[first_digit] + "Million" + text_rep(remainder)

    if (999999 >= num) & (num > 99999): # in the 100,000's 
        first_digit = num // 100000
        remainder = num % 100000
        if (remainder == 0):
            return ones[first_digit] + "HundredThousand"
        else:
            return ones[first_digit] + "Hundred" + text_rep(num % 100000)

    if (99999 >= num) & (num > 9999): # is in the 10,000's  
        first_digit = num // 10000
        remainder = num % 10000
        if (first_digit == 1):
            return teens[num // 1000] + "Thousand" + text_rep(num % 1000)
        elif (remainder == 0): 
            return tens[first_digit] + "Thousand"
        elif ((num // 1000) % 10 == 0): # check if 2nd digit is zero
            return tens[first_digit] + "Thousand" + text_rep(remainder)
        else:
            return tens[first_digit] + text_rep(remainder) 

    if (9999 >= num) & (num > 999): # in the 1,000's
        first_digit = num // 1000
        remainder = num % 1000
        if (remainder == 0):
            return ones[first_digit] + "Thousand"
        else:
            return ones[first_digit] + "Thousand" + text_rep(remainder)

    if (999 >= num) & (num > 99): # in the 100s
        first_digit = num // 100
        remainder = num % 100
        if (remainder == 0): 
            return ones[first_digit] + "Hundred"
        else:
            return ones[first_digit] + "Hundred" + text_rep(remainder) 

    if (99 >= num) & (num > 9): # in the 10's    
        first_digit = num // 10
        remainder = num % 10
        if (first_digit == 1):
            return teens[num]
        elif (remainder == 0): # check if multiple of 10
            return tens[first_digit]
        else:
            return tens[first_digit] + text_rep(remainder)
        
    if (9 >= num): # in the 1's (BASE CASE)
        return ones[num]

    return print("Error: number must be less than 1 billion!")


def dollarize(num):
    print (text_rep(num) + "Dollars")
    return


for test in test_cases:
    dollarize(test)

test_cases.close()
