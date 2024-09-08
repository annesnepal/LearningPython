# Currying is a method that transforms a function taking multiple arguments into a chain of function that each take a single argument.
def add(a):
    def add_b(b):
        return a+b
    return add_b

result = add(3)(7)
print(result)




