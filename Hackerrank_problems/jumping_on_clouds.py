lst = [0, 0]


def game(lst):
    noi = len(lst)
    flag = 0
    count = 0
    noic = noi-1
    while flag < noic:
        if noic-flag == 1:
            count = count + 1
            flag = flag + 1
        else:
            if lst[flag + 2] == 1:
                count = count + 1
                flag = flag + 1
            else:
                count = count + 1
                flag = flag + 2

    return count


x = game(lst)
print(x)
