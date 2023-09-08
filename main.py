# implement a regressive function to calculate the factorial of a given number
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Example usage
number = int(input("Enter a number: "))
factorial = calculate_factorial(number)

print("The factorial of", number, "is", factorial)