# Functional Programming - Declarative Code 

#Imperative Style

numbers = [1,2,3,4,5]

squared_numbers = []

for i in numbers:
    squared_numbers.append(i * i)

# print(squared_numbers)


# Output: [1,4,9,16,25]

#Functional Style

sq_numbers = list(map(lambda x: x * x, numbers))
print(sq_numbers)