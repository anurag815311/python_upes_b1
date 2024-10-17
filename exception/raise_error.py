def check_val(x):
    if x==0:
        raise ValueError("X cannot be zero")
    return x

try:
    check_val(0)
except ValueError as e:
    print(e)