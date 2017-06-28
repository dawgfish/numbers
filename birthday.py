#!/usr/bin/env python

'''
Python program to sumulte the birthday problem or birthday paradox having concerns
the probability that, in a set of n randomly chosen people, some pair of them will
have the same birthday.
'''

import random

__author__ = "M. Jastad"
__copyright__ = "Copyright(c) 2015"
__license__ = "USE-AS-IS"
__version__ = "1.1.5"
__maintainer__ = "M. Jastad"
__email__ = "majastad@icloud.com"


def has_duplicates(listToCheck):
    number_set = set(listToCheck)

    if len(number_set) is not len(listToCheck) : return True
    else : return False

def main():

    duplicateNumber = 0

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

        for i in range(0,1000):
            birthdayList = []

            for j in range(0,userInput):
                birthday=random.randint(1,365)
                birthdayList.append(birthday)

            x = has_duplicates(birthdayList)

            if x : duplicateNumber += 1

        print "results: after 1000 simulations with " + str(userInput) + " student(s) there were", duplicateNumber,\
                    "simulations with at least one match. The approximate probability is", \
                    round(((duplicateNumber/1000.0)*100),3),"%"


if __name__ == "__main__":
    main()