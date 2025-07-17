s = input().lower()
t = s
c = []
s = list(set(list(s)))
for i in s:
    c.append(t.count(i))
if c.count(max(c)) != 1:
    print("?")
else:
    print(s[c.index(max(c))].upper())