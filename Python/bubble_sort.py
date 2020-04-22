#Bubble sort algorithm basic in python with swapping

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
count_swap = 0
for num in range(len(a)-1, 0, -1):
        for i in range(num):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                count_swap +=1



print ("Array is sorted in {} swaps.".format(count_swap))
print ("First Element: {}".format(a[0]))
print ("Last Element: {}".format(a[-1]))