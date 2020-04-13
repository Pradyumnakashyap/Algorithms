#Given a base-10 integer,n, convert it to binary (base-2). Then find and 
# print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.



import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    nbin = str("{0:b}".format(n)).split('0') 
    print(max([len(n1) for n1 in nbin]))
            