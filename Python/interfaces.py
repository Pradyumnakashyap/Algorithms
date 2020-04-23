#Implement a menthod to override a Interface to calculate the sum of all the divisors of a given number

import math

class AdvancedArithmetic(object):
    def divisorSum(self,n):
        raise NotImplementedError
      
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        self.divs = [1]
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                self.divs.extend([i,n/i])
        self.divs.extend([n])
        return int(sum(list(set(self.divs))))


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)