n, m, k = map(int, input().split())
if n + 1 < m + k or n > m * k:
    print(-1)
    quit()
l = [1] * m
if k == 1:
    print(*[i for i in range(1, m + 1)])
    quit()
d, r = (n - m) // (k - 1), (n - m) % (k - 1)
for i in range(d):
    l[i] = k
if r > 0:
    l[d] += r
a = []
temp = 0
for i in l:
    for j in range(temp + i, temp, -1):
        a.append(j)
    temp += i
print(*a)