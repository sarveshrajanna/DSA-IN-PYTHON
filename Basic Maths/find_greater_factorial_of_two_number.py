class solution:
    def findGcd(self,a, b):
        while b != 0:
            a, b = b, a % b
        return a
a = int(input("Enter first number: "))
b = int(input("Enter the second number: "))
sol = solution()
big_factor = sol.findGcd(a,b)
print(f"{big_factor} is the big factor ")