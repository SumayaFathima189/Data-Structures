number = int(input("Enter a number to find the factorial - "))

def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number*factorial(number-1)
print(f"Factorial of {number} is {factorial(number)}")    