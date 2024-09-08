#Functional Programming -  Function composition

def add_one(x):   #first Simple function 
    return x + 1

def multiply_by_two(x):  #Second Simple function
    return x * 2

def compose(a,m): #Combining first and second function
    return lambda x: m(a(x))

add_then_multiply = compose(add_one, multiply_by_two)
print(add_then_multiply(7))


