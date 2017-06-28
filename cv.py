#!/usr/bin/env python

'''
Python program to convert decimal number into binary, octal, and hexadecimal number system

Usage:
    Valid inputs are positive integer values:

        $ python cv.py 20
'''
import sys

__author__ = "M. Jastad"
__copyright__ = "Copyright(c) 2015"
__license__ = "USE-AS-IS"
__version__ = "1.0.2"
__maintainer__ = "M. Jastad"
__email__ = "majastad@icloud.com"

ERROR_MSG = "error: input must be a postive integer..."

def error():
    print ERROR_MSG
    exit(0)

def main():

    try:
        userInput = sys.argv[1]
        userInput = int(userInput)
    except:
        error()

    if userInput < 0 : 
        error()

    print "converted values of", userInput, '\n'

    data = [[bin(userInput), ": binary"], [oct(userInput), ": octal"], [hex(userInput), ": hexadecimal"]]
    col_width = max(len(word) for row in data for word in row) + 2
    for row in data:
        print "".join(word.ljust(col_width) for word in row)

if __name__ == "__main__":
    main()
