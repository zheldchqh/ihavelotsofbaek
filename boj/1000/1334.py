s = input()
l = len(s)
if l < 2:
    s = int(s) + 1
    if s == 10:
        s += 1
elif l % 2 == 1:
    L = s[:l // 2]
    t = s[l // 2 + 1:]
    m = s[l // 2]
    if int(L[::-1]) <= int(t):
        if s[l // 2] != '9':
            s = L + str(int(m) + 1) + L[::-1]
        else:
            if len(str(int(L) + 1)) == len(L):
                s = str(int(L) + 1) + '0' + str(int(L) + 1)[::-1]
            else:
                s = str(int(L) + 1) + str(int(L) + 1)[::-1]
    else:
        s = L + m + L[::-1]
else:
    L = s[:l // 2]
    t = s[l // 2:]
    if int(L[::-1]) <= int(t):
        if len(L) == len(str(int(L) + 1)):
            s = str(int(L) + 1) + str(int(L) + 1)[::-1]
        else:
            s = str(int(L) + 1) + str(int(L) + 1)[::-1][1:]
    else:
        s = L + L[::-1]
print(s)