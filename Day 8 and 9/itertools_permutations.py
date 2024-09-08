# Permutations -> Possible Ordering of the position

from itertools import permutations

a = [1,2,3]

perm = permutations(a)
perm_1= permutations(a,2)

print(list(perm))
print(list(perm_1))