import math

n, m = map(int, input().split())
print(m - math.gcd(n, m))