
from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [0,1,2,3,4]

group_obj = groupby(a, key=smaller_than_3)

for key, value in group_obj:
    print(key, list(value))

#Another Example

persons = [
    {'name':'Anish', 'age':13}, 
    {'name':'Yash', 'age':13}, 
    {'name':'Dhaval', 'age':10},  
    {'name':'Atharva', 'age':10}
    ]

group_obj = groupby(persons, key= lambda x: x['age'])

for key, value in group_obj:
    print(key, list(value))