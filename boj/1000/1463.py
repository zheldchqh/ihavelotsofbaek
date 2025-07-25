import sys
from collections import *
input = sys.stdin.readline

n = int(input())
Q = deque([n])
t=[0] * (n + 1)
while Q:
    a=Q.popleft()
    if a < 2:
        break
    if t[a - 1] == 0:
        Q.append(a - 1)
        t[a - 1] = t[a] + 1
    if a % 3 == 0 and t[a // 3] == 0:
        Q.append(a // 3)
        t[a // 3] = t[a] + 1
    if a % 2 == 0 and t[a // 2] == 0:
        Q.append(a // 2)
        t[a // 2] = t[a] + 1
print(t[1])