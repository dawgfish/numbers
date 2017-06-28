#!/usr/bin/env python

'''
Python program to display the Fibonacci sequence up to n-th term using recursive functions
'''

__author__ = "M. Jastad"
__copyright__ = "Copyright(c) 2015"
__license__ = "USE-AS-IS"
__version__ = "2.0.4"
__maintainer__ = "M. Jastad"
__email__ = "majastad@icloud.com"


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

def main():

    while True:

        userInput = raw_input("\nenter numeric value (q to quit): ")
        if userInput == 'q': break

        try:
            userInput = int(userInput)
        except:
            print "error: ", userInput, "is non-numeric."
            continue

        if userInput <= 0:
            print("error: enter a positive integer")
            continue
        else:
            print("Fibonacci sequence:")
            for i in range(userInput):
                print(fibonacci(i))

if __name__ == "__main__":
    main()