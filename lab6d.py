# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 11/04/2026
# Purpose: Creating dictionary.
# Usage: ./lab6d.py

# TO DO 1: Create function times_ten as instructed in readme.md file. 

# TO DO 2: Run the script.
def times_ten(start_index: int, end_index: int):
    '''
    Create a dictionary with keys as numbers from start_index to end_index (inclusive) and
    values as those numbers multiplied by 10.
    @param start_index (int): The starting number for the dictionary keys.
    @param end_index (int): The ending number for the dictionary keys.
    @return: A dictionary with keys as numbers from start_index to end_index and values as those numbers multiplied by 10.
    '''
    numbers_dict = {}
    for num in range(start_index, end_index + 1):
        numbers_dict[num] = num * 10

    return numbers_dict

def main():
    start_index = 2
    end_index = 6
    my_dictionary = times_ten(start_index, end_index)
    print(my_dictionary)

main()