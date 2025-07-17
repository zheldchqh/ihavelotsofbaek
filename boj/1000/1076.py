l = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
s = ""
for _ in range(2): s += str(l[input()])
print(int(s) * 10 ** l[input()])