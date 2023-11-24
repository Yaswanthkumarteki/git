s1 = 'absdjkvuahdakejfnfauhdsaavasdlkj'
s2 = 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'
s1len = len(s1)
s2len = len(s2)
s1 = [i for i in s1]
s2 = [i for i in s2]
flag = 0
for i in s1:
    if i in s2:
        s2.remove(i)
        flag = flag + 1

print((s1len - flag) + len(s2))
