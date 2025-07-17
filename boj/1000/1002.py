import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().rstrip().split())
    r = ((x1 - x2)**2 + (y1 - y2)**2) ** .5
    r1, r2 = max(r1, r2), min(r1, r2)
    if (x1, y1) == (x2, y2):
        if r1 == r2: print(-1)
        else: print(0)
    else:
        if r1 - r2 < r and r < r1 + r2: print(2)
        elif r1 + r2 == r or r1 - r2 == r: print(1)
        else: print(0)