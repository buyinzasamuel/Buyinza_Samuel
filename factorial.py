def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate the factorial of 5
number = 5
factorial_of_5 = factorial(number)

print(f"The factorial of {number} is {factorial_of_5}.")
