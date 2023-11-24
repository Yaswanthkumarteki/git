s = 'SOSOOSOSOSOSOSSOSOSOSOSOSOS'


def sos(s):
    l = len(s)/3
    flag = 0
    i = 0
    while l > 0:
        if s[i] == 'S' and s[i+1] == 'O' and s[i+2] == 'S':
            flag = flag + 0
        elif (s[i] == 'S' and s[i+1] == 'O') or (s[i+1] == 'O' and s[i+2] == 'S') or (s[i] == 'S' and s[i+2] == 'S'):
            flag = flag + 1
        elif (s[i] == 'S') or (s[i+1] == 'O') or (s[i+2] == 'S'):
            flag = flag+2
        else:
            flag = flag+3
        i = i+3
        l = l-1
    return flag


x = sos(s)
print(x)
