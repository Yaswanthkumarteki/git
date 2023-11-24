'''n = int(input(" Enter thr number of jars:- "))
k = int(input(" Enter thr number of times you fill the jars with candies:- "))'''
lst1 = [[2, 3, 603], [1, 1, 286], [4, 4, 882]]
n = 4


def fun(n, lst1):
    dummylist = [0 for i in range(n)]
    for i in range(len(lst1)):
        start = lst1[i][0] - 1
        end = lst1[i][1] - 1
        value = lst1[i][2]
        while start <= end:
            dummylist[start] = dummylist[start] + value
            start = start + 1
    return int(sum(dummylist)/len(dummylist))


'''output = 0
    for o in operations:
        output += o[2] * (o[1]-o[0]+1)
    return output//n'''

x = fun(n, lst1)
print(x)
