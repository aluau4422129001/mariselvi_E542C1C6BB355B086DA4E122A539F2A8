def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input from the user
num = int(input("Enter a number: "))

# Check if the input is negative
if num < 0:rs;
print("Factorial is not defined for negative number.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}") 