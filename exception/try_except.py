try:
    x=10/0
    y=int("hello")
except (ValueError,ArithmeticError) as e:
    print(f"Error: {e}")

"""except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Invalid input")"""

def check_age(x):
    if x < 18:
        raise ValueError("Age is less than 18")
    else:
        return x

try:
    check_age(16)
except ValueError as e:
    print(e)