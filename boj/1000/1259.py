while True:
    s = input().strip()
    if s == "0":
        break
    else:
        if s == s[::-1]:
            print("yes")
        else:
            print("no")