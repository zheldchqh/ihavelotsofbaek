l0 = [1, 0]
l1 = [0, 1]
i = 2
T = int(input())
for _ in range(T):
    N = int(input())
    if len(l0) <= N:
        while i <= N:
            l0.append(l0[i-1] + l0[i-2])
            l1.append(l1[i-1] + l1[i-2])
            i += 1
    print(l0[N], l1[N])