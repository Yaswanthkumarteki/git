lst = [34, 95, 34, 64, 45, 95, 16, 80, 80,
       75, 3, 25, 75, 25, 31, 3, 64, 16, 31]


def fun(lst):
    lst.sort()
    unqlst = list(set(lst))
    unqlst.sort()
    cntlst = []
    for i in unqlst:
        x = lst.count(i)
        cntlst.append(x)
    mini = 1
    for i in range(len(cntlst)):
        if cntlst[i] <= mini:
            x = i

    ans = unqlst[x]
    return ans


x = fun(lst)
print(x)
