# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 11/04/2026
# Purpose: Practice Set Operations.
# Usage: ./lab6b.py
# TO DO 1: Copy the code from lab6a.py and paste here.
# TO DO 2: Create the function s3ors5().
# TO DO 3: Run the script. Take screenshot of only s3ors5() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.
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

def s3_or_s5(s3, s5):
    '''
    Create a set of numbers that are divisible by 3 or 5.
    @param s3: Set of numbers divisible by 3.
    @param s5: Set of numbers divisible by 5.
    @return: A set of numbers that are divisible by 3 or 5.
    '''
    return s3 | s5


def main():

    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    # TO DO 2: Call the s3ors5() function and print the result.
    s3ors5 = s3_or_s5(s3, s5)
    print("s3 or s5: ", s3ors5)

main()