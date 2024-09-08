#Count
from itertools import count

for i in count(10):
    print(i)

    if i == 15:
        break

#Cycle
from itertools import cycle

a = [1,2,3,4]

for i in cycle(a):
    print(i)

#Repeat
from itertools import repeat

b = [1,2,3]

for i in repeat(b, 2):
    print(i)