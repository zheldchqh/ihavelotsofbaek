import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N: return False
    if a[x][y] == 1:
        a[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    a = [[0]*N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        a[x][y] = 1
    t = 0
    for i in range(M):
        for j in range(N):
            if dfs(i, j): t += 1
    print(t)