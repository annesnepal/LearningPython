from itertools import accumulate

a = [1,2,3,4]
acc = accumulate(a)

print(list(acc))

#Multiplication 

import operator

a = [1,2,3,4,5]
acc = accumulate(a, func=operator.mul)

print(list(acc))

#Maximum

a = [1,2,6,3,4,5,7]
acc = accumulate(a, func=max)

print(list(acc))