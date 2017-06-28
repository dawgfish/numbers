#!/usr/bin/env python

'''
Python program to display the Fibonacci sequence up to n-th term using recursive functions

Usage:
    Valid inputs are positive integer values:

        $ python fib.py 10
'''

import sys

__author__ = "M. Jastad"
__copyright__ = "Copyright(c) 2015"
__license__ = "USE-AS-IS"
__version__ = "2.0.4"
__maintainer__ = "M. Jastad"
__email__ = "majastad@icloud.com"

ERROR_MSG = "error: input must be a postive integer..."

def error():
    print ERROR_MSG
    exit(0)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

def main():

    try:
        userInput = sys.argv[1]
        userInput = int(userInput)
    except:
	error()

    if userInput <= 0:
        error()
 
    print("Fibonacci sequence:")
    for i in range(userInput):
        print(fibonacci(i))

if __name__ == "__main__":
    main()
