from math import *

s, p = map(int, input().split())
P = log(p)
if s // e > 0:
    V = (s // e) * log(s / (s // e))
else:
    V = -10 ** 8
v = (s // e + 1) * log(s / (s // e + 1))
if P > max(V, v):
    print(-1)
    quit()
l = 1
if V < v:
    l = s // e + 1
else:
    l = s // e
a = []
while l <= L:
    m = (l + L) // 2
    t = m * log(s / m)
    if t < P:
        l = m + 1
    else:
        a.append(m)
        L = m - 1
m = int(min(a))
if m == 1 and s != p:
    print(2)
else:
    print(m)