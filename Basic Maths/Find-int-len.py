# Given an integer N, return the number of digits in N.
import math
class solution:
    def find_len(self,n):
        if n == 0:
            return 1
        return ((math.log10(n)//1)+1)
sol = solution()
n = int(input("Enter Number : "))
result = int(sol.find_len(n))
print(result)