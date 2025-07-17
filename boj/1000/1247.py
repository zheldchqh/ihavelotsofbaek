for _ in range(3):
    T = int(input())
    l = [int(input()) for _ in range(T)]
    k = sum(l)
    if k > 0:
        print("+")
    elif k < 0:
        print("-")
    else:
        print(0)