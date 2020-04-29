#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    l1 = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = str(firstNameEmailID[0])

        emailID = firstNameEmailID[1]
        if re.match(r"^[a-z0-9]+[\.'\-]*[a-z0-9]+@(gmail)\.com$",emailID):
            l1.append(firstName)
print(*sorted(l1, key=str), sep='\n')
