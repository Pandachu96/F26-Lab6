# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 11/04/2026
# Purpose: Create Sets.
# Usage: ./lab6a.py

# TO DO 1: Complete the functions below.

def buildtheSet(divisor):
    '''
    Build a set of numbers from 0 to 100 that are divisible by the given divisor.
    @param divisor: The number to divide by.
    @return: A set of numbers in the range 0-100 that are divisible by the divisor.
    '''
    num_set = set()
    for num in range(101):
        if num % divisor == 0:
            num_set.add(num)

    return num_set

def main():

    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")

    s11 = buildtheSet(11)
    print("s11: ", s11)

main()