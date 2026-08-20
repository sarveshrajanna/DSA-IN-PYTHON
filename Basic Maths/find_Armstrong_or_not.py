class solution:
    def find_armstrong(self, n):
        dum_n = n
        s = 0
        while n > 0:
            r = n % 10
            n = n//10
            s = r**3 + s
        if dum_n == s:
            print("It is a Armstrong Number.")
        else :
            print("It is not a Armstrong.")


n = int(input ("enter the value or number: "))
sol = solution()
result = sol.find_armstrong(n)
