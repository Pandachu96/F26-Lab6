# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 11/04/2026
# Purpose: Practice Set Operations.
# Usage: ./lab6c.py

# TO DO 1: Copy the code from lab5b.py and paste here.
# TO DO 2: Create the function s3_and_s5_not_s7().
# TO DO 3: Run the script. Take screenshot of only s3_and_s5_not_s7() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.
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

def s3_and_s5_not_s7(s3, s5, s7):
    '''
    Create a set of numbers that are divisible by 3 and 5 but not by 7.
    @param s3: Set of numbers divisible by 3.
    @param s5: Set of numbers divisible by 5.
    @param s7: Set of numbers divisible by 7.
    @return: A set of numbers that are divisible by 3 and 5 but not by 7.
    '''
    return (s3 & s5) - s7


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

    # TO DO 2: Call the s3_and_s5_not_s7() function and print the result.
    s3ands5nots7 = s3_and_s5_not_s7(s3, s5, s7)
    print("s3 and s5 but not s7: ", s3ands5nots7)

main()