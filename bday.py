#!/usr/bin/env python

'''
Python program to sumulte the birthday problem or birthday paradox having concerns
the probability that, in a set of n randomly chosen people, some pair of them will
have the same birthday.

Usage:
    Valid inputs are positive integer values:

        $ python bday.py 23
'''
import random
import sys

__author__ = "M. Jastad"
__copyright__ = "Copyright(c) 2015"
__license__ = "USE-AS-IS"
__version__ = "1.1.5"
__maintainer__ = "M. Jastad"
__email__ = "majastad@icloud.com"

ERROR_MSG = "error: input must be a postive integer..."

def error():
    print ERROR_MSG
    exit(0)

def has_duplicates(listToCheck):
    number_set = set(listToCheck)

    if len(number_set) is not len(listToCheck) : return True
    else : return False

def main():

    duplicateNumber = 0

    try:
        userInput = sys.argv[1]
        userInput = int(userInput)
    except:
        error()

    if userInput <= 0:
        error()

    for i in range(0,1000):
        birthdayList = []

        for j in range(0,userInput):
            birthday=random.randint(1,365)
            birthdayList.append(birthday)

        x = has_duplicates(birthdayList)

        if x : duplicateNumber += 1

    print "results: post 1000 simulations with " + str(userInput) + " student(s) there were: ", duplicateNumber,\
                    "simulations with at least one match. approximate probability is: ", \
                    round(((duplicateNumber/1000.0)*100),3),"%"


if __name__ == "__main__":
    main()
