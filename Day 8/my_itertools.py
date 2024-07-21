
# Itertools : product, permutations, combinations, accumulate, groupby, and infinite iterators

#Product -> Cartesian Product 

from itertools import product


a = [1,2]
b = [3]

prod = product(a,b, repeat=2)
print(list(prod))

# Permutations -> Possible Ordering of the position

from itertools import permutations

a = [1,2,3]

perm = permutations(a)
perm_1= permutations(a,2)

print(list(perm))
print(list(perm_1))

# Combinations -> Grouping of elements

from itertools import combinations, combinations_with_replacement

a = [1,2,3,4]

comb = combinations(a,2)

print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))