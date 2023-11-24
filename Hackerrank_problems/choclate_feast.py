def fun(n,c,m):
    noc = int(n/c)
    now = int(n/c)
    rw = 0
    while now>=m:
        wcc = int((now/m))
        rw = (now%m)
        noc = noc + wcc
        now = wcc + rw
    return noc


x = fun(15,3,2)
print(x)
