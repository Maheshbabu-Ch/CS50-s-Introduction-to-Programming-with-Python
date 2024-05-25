d = {}
while True:
    try:
        x = input().strip().upper()
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    except EOFError:
        p = sorted(d.keys())
        for i in p:
            print(f"{d[i]} {i}")
        break
    else:
        continue
