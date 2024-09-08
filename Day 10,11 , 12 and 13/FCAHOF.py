#Functional programming - First Class and Higher Order Functions

def greet(name): #Value as an argument
    return f"Hello {name}!"

def calling_greet(new_func,value): #Function as an argument
    return new_func(value) #Function call of First class Function

print(calling_greet(greet, 'Anish'))