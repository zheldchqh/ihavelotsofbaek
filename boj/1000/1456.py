import sys
input = sys.stdin.readline

A, B = map(int, input().split())
l = [True] * (int(B ** 0.5) + 1)
l[1] = False
for i in range(2, int(B ** 0.5)+1):
    if l[i]:
        if i * i > int(B ** 0.5):
            break
        for j in range(i ** 2, int(B ** 0.5) + 1, i):
            l[j] = False
c = 0
for i in range(1, len(l)):
    if l[i]:
        t = i * i
        while True:
            if t < A:
                t *= i
                continue
            if t > B:
                break
            t *= i
            c += 1
print(c)