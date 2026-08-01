# Reverse the number 
class solution:
    # Reverse the number 
    def reverse(self,n):
        new_number = 0
        while n > 0:
            dig = n%10
            new_number = new_number*10 + dig
            n = n // 10
        print(new_number)

    # find number is palindrome or not
    def palindrome(self,n):
        new_number = 0
        duplicate = n
        while n > 0:
            dig = n%10
            new_number = new_number*10 + dig
            n = n // 10
        if new_number == duplicate:
            print("The number is a palindrome.")
        else:
            print("The number is not a palindrome.")


    
sol = solution()
n = int(input("Enter the number: "))
# To Reverse the number 
#Reversed_number = sol.reverse(n)

# To find the Palindrome of the number
find_palindrome = sol.palindrome(n)


