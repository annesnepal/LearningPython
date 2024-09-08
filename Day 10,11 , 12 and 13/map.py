# Map applies a function to all items in an input list.

numbers = [1,2,3,4,5]

squared  = list(map(lambda x: x ** 2, numbers))

print(squared)

# Problem 2: Given a list of strings, use map to convert each string to uppercase.
# words = ["hello", "world", "python", "map"]

words = ["hello", "world", "python", "map", "anish"]

uppercase_list = list(map(lambda x: x.upper(), words))

print(uppercase_list)

# Problem 3: Given a list of words, use map to create a list of the first letters of each word.
# words = ["apple", "banana", "cherry", "date"]

words = ["apple", "banana", "cherry", "date", "elephant"]

first_letter_list = list(map(lambda x: x[0], words))

print(first_letter_list)