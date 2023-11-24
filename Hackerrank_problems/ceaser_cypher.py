word = 'Abcdefghijklmno- pqrstuvwXyz'
shift = 3
shift = shift % 26
let = ''
for i in word:
    if i.isalpha():
        if i.islower():
            if ord(i) + shift > 122:
                z = ord(i)-26
                z = z + shift
                let = let + (chr(z))
            else:
                let = let + (chr(ord(i)+shift))
        elif i.isupper():
            if ord(i) + shift > 90:
                z = ord(i)-26
                z = z + shift
                let = let + (chr(z))
            else:
                let = let + (chr(ord(i)+shift))
    else:
        let = let + i

print(let)
