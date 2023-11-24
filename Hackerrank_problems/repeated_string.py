s = 'gfcaaaecbg'
n = 547602


def fun(s, n):
    rem = n % len(s)
    a_count = s.count('a')
    if rem == 0:
        return (a_count*int(n/len(s)))
    else:
        x = int((n - rem)/len(s)) * a_count
        y = s[:(rem-1)]
        print(y)
        return x+y.count('a')


z = fun(s, n)
print(z)
