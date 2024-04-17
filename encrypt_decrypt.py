def encrypt(FileName, password):
    passcode = len(password)+(len(password)%2)
    EncryptedPWD = ""
    EncryptedData = ""

    for i in password:
        EncryptedPWD += chr(ord(i) + passcode)

    with open(FileName,'r') as p:
        FileContent = p.read()
    with open(FileName,'w', encoding='utf-8') as p:
        for i in FileContent:
            EncryptedData += chr(ord(i) + passcode)
        p.write(EncryptedData)
    with open(FileName,'a', encoding='utf-8') as p:
        p.write(EncryptedPWD)


def decrypt(FileName,password):
    EncryptedPWD = ""
    content = ""
    passcode = len(password) + (len(password)%2)
    for i in password:
        EncryptedPWD += chr(ord(i) + passcode)
    with open(FileName, 'r', encoding = 'utf-8') as p:
        FileContent = p.read()

    if FileContent[-len(EncryptedPWD):] == EncryptedPWD:
        with open(FileName, 'w', encoding='utf-8') as p:
            EncryptedData = FileContent
            for i in EncryptedData:
                content += chr(ord(i) - passcode)
            content = content[: -(len(password))]
            p.write(content)

    else:
        with open(FileName, 'w', encoding = 'utf-8') as p:
            p.write(FileContent)
        raise Exception("Sorry you entered wrong password")
    
if __name__ == '__main__':
    print("In encrypt-decrypt file")
