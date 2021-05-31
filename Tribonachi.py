def trib(n):
    old = 0
    cur = 1
    i = 1
    yield cur
    while (i < n):
        cur, old, i = cur+old, cur, i+1
        yield cur

for f in trib(35):
    print(f)