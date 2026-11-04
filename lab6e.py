# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 11/04/2026
# Purpose: Traverse dictionary.
# Usage: ./lab6e.py

my_dict = {"switzerland" : "Alps", "United States" : "Alska Range", "Armenia" : "Caucasus", "Argentina" : "Andes", "Karakoram" : "Pakistan"}
# TO DO 1: Create a for in loop as instructed in readme.md file. 
# TO DO 2: Run the script, and take the screenshot of code and output.
for country, mountain_range in my_dict.items():
    print(f"{country} : {mountain_range}")