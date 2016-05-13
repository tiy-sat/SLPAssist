from passlib.hash import sha512_crypt

# auser = ['jimmy', '@admin',  'admin', 'nobody@swbell.net', 'password']

def hash_pswd(aList):
    pswd = aList[-1]
    hash_pswd = sha512_crypt.encrypt(pswd)
    aList.pop()
    aList.append(hash_pswd)
    return aList

def pswd_verify():
    pass

# print(auser)
# print(hash_pswd(auser))
