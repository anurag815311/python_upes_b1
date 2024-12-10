class CustomError(Exception):
    def __init__(self, message):
        self.message = message

#Raising the custom exception
def check_value(x):
    if x < 0:
        raise CustomError("Value cannot be negative!")

try:
    check_value(-1)
except CustomError as e:
    print(e.message)  # Output: Value cannot be negative!



