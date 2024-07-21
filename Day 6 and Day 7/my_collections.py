from collections import deque


d = deque()

d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.extendleft([5,6,7,8])
d.extend([9,10,11])
print(d)
d.rotate(-2)

print(d)


