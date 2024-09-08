# Filter creates a list of elements for which a function returns true.

numbers = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)