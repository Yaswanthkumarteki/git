# arr = [3,2,3,3,1]
arr = [41, 22, 80, 80, 41, 41, 41, 80, 22, 80, 22, 41, 41, 41, 80, 80, 22, 22, 22, 22, 41, 80, 80, 41, 22,
       80, 80, 80, 80, 41, 22, 80, 22, 22, 22, 80, 22, 80, 80, 41, 22, 41, 41, 22, 22, 41, 22, 80, 22, 22, 80, 41]


def fun(arr):
    arr = sorted(arr)
    arr1 = list(set(arr))
    arr1.sort()
    print(arr1)
    lst = []
    for i in arr1:
        lst.append(arr.count(i))
    lst.remove(max(lst))
    return sum(lst)


x = fun(arr)
print(x)
