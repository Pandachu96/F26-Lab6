# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 11/04/2026
# Purpose: Use Dictionary for Problem solving.
# Usage: ./lab5f.py

# TO DO 1: Create function histogram() as instructed in readme.md file. 
# TO DO 2: Create main() function and call histogram(). Call the main() function.
# TO DO 3: Run the script. Take screenshot of code showing the functions histogram() and main(). Also show output in the screenshot.
def histogram(input_string):
    '''
    Create a histogram (dictionary) that displays the count of the occurrences of each character in the input string in
    the form of asterisks.
    @param input_string: The string to analyze.
    @return: None. Prints the histogram to the console.
    '''
    hist = {}
    for char in input_string:
        if char != ' ':
            if char in hist:
                hist[char] += 1
            else:
                hist[char] = 1

    for char, count in hist.items():
        print(char, '*' * count)

def main():
    input_str = 'hello amma'
    histogram(input_str)

if __name__ == "__main__":
    main()