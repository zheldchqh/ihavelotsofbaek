min_val, max_val = map(int, input().split())
sieve = [True] * (max_val - min_val + 1)
for i in range(2, int(max_val**0.5) + 1):
    square = i ** 2
    start = max(square, (min_val + square - 1) // square * square)
    for j in range(start, max_val + 1, square):
        sieve[j - min_val] = False
print(sum(sieve))