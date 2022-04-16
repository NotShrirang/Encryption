import random

def encrypt(msg:str|list):
    '''
    Function for encrypting text.
    
    args :
        msg (str) : Text to be encrypted.
    Returns : 
        Tuple of encrypted message and answerkey for decryption. -> tuple[str, list]
    '''
    y=str()
    answerKey = []
    for ch in msg:
        ch = bytes(ch, 'utf-8')
        r=random.randint(0,5)
        s=bytes([ch[0] + r])
        s=str(s)
        y=y+s[2]
        answerKey.append(str(r))
    return y, answerKey
def encryptWithKey(msg : str, key : list):
    '''
    Function for encrypting text with user provided key.
    
    args :
        msg (str) : Text to be encrypted.
        key (list) : Key for encryption.
    Returns : 
        Encrypted message in string format.
    '''
    i=0
    msg = list(msg)
    y=str()
    for a in key:
        ch=msg[i]
        ch = bytes(ch, 'utf-8')
        s=bytes([ch[0] + int(a)])
        s=str(s)
        y=y+s[2]
        i=i+1
    return y
def decrypt(msg : str, key: list):
    '''
    Function for decrypting text.
    
    args :
        msg (str) : Encrypted text.
        key (list) : Key for decryption.
    Returns : 
        Decrypted message in string format.
    '''
    i=0
    x=str()
    a=list()
    for j in key:
        a.append(int(j))
        ch = msg[i]
        ch = bytes(ch,'utf-8')
        s = bytes([ch[0] - int(j)])
        s = str(s)
        x = x+s[2]
        i = i+1
    return x
def decryptorFormatting(key : str):
    '''
    Function for formatting given str(key) to list(key) in order to pass it to Decrypt().
    
    args :
        key (str) : key for decryption.
    Returns : 
        Converted key in list format.
    '''
    key = key.replace("[", "")
    key = key.replace("'", "")
    key = key.replace(",", "")
    key = key.replace(" ", "")
    key = key.replace("]", "")
    return list(key)
def hash(msg : str):
    '''
    Function for hashing the message passed.

    args :
        msg (str) : Text to be hashed.
    Returns : 
        hashed message.
    '''
    l = len(list(msg))
    s = ""
    y = str()
    for i in range(l):
        ch = msg[i]
        ch = bytes(ch, 'utf-8')
        ch = bytes([ch[0]+i])
        s = str(ch)
        y = y + str(s[2])
    return y