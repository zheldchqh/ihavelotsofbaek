moeum = ["a", "e", "i", "o", "u"]
while True:
    k = 0
    s = input().lower()
    if s == "#":
        break
    for i in s:
        if i in moeum:
            k += 1
    print(k)