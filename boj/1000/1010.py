import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(math.comb(b, a))