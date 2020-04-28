#Determine if the number is prime or not, time complexity is less than O(n) or O(root(N))
#Input number of inputs

import math

def isprime(num):
    if num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"

T = int(input())
for i in range(T):
    number = int(input())
    print(isprime(number))

    