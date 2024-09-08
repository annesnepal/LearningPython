#Reduce applies a rolling computation to sequential pairs of values in a list

from functools import reduce

numbers = [1,2,3,4,5]

product = reduce(lambda x,y : x * y, numbers)

print(product)

sum = reduce(lambda x,y : x + y, numbers)
print(sum)
