#Encryption
import sqlite3
import random

def Encrypt(x):
    m=len(list(x))
    i=0
    y=str()
    mylist = []
    answerKey = []
    while i<m:
        ch=x[i]
        ch = bytes(ch, 'utf-8')
        r=random.randint(0,5)
        s=bytes([ch[0] + r])
        s=str(s)
        y=y+s[2]
        i=i+1
        answerKey.append(str(r))
    return y, answerKey

def encryptWithKey(x, answerKey):
    # m=len(list(x))
    i=0
    x = list(x)
    y=str()
    for a in answerKey:
        ch=x[i]
        ch = bytes(ch, 'utf-8')
        s=bytes([ch[0] + int(a)])
        s=str(s)
        y=y+s[2]
        i=i+1
    return y

#Decryption
def Decrypt(msg, answerKey):
    i=0
    x=str()
    a=list()
    for j in answerKey:
        num = j
        num = int(num)
        a.append(num)
        ch = msg[i]
        ch = bytes(ch,'utf-8')
        s = bytes([ch[0] - num])
        s = str(s)
        x = x+s[2]
        i = i+1
    return x

def decryptorFormatting(key):
    key = key.replace("[", "")
    key = key.replace("'", "")
    key = key.replace(",", "")
    key = key.replace(" ", "")
    key = key.replace("]", "")
    return list(key)
