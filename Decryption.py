#Decryption
import os

def Decrypt(y):
    n=len(list(y))
    i=0
    x=str()
    a=list()
    while i<(n):
        f = open("Answer Key.txt", "r")
        j = (f.readline())
        num = j[i]
        num = int(num)
        #num = int(input("Enter no."))
        a.append(num)
        ch= y[i]
        ch= bytes(ch,'utf-8')
        s=bytes([ch[0] - num])
        s=str(s)
        x=x+s[2]
        i=i+1
    print("Decrypted Message:", x)

f = open("Encrypted Message.txt", "r")
y = f.read()
f.close()
Decrypt(y) 

