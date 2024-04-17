from encrypt_decrypt import encrypt, decrypt

task_dict = {1:"Encryption", 2:"Decryption"}

try:
    try:
        task_to_be_done = int(input("Please enter the task to be done\n1 -> Encryption\n2 -> Decryption \n"))
    except Exception:
        raise Exception("Please enter Valid input")
    
    if task_to_be_done != 1 and task_to_be_done != 2:
        raise Exception("Please select valid task")
    else:
        if task_to_be_done == 1:
            FileName = input("Please enter file path you want to encrypt: \n")
            password = input("Please set the password: \n")
            encrypt(FileName=FileName, password=password)
        else:
            FileName = input("Please enter file path you want to decrypt: \n")
            password = input("Please enter the password: \n")
            decrypt(FileName=FileName, password=password)
except Exception as exc:
    print(exc)
