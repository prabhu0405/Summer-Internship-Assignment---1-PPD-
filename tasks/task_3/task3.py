
def safe_divide(a, b):
    try:
        result = float(a) / float(b)
        return result

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    except ValueError:
        return "Error: Invalid input. Please enter numeric values."


#input from user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

#function call
output = safe_divide(num1, num2)

#printing result
print("\nResult:")
print(output)