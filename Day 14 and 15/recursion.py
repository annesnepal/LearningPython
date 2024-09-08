# Functional Programming


def factorial(n):
    if n < 0:
        return False

    elif n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial(n-1)


print(factorial(4))




