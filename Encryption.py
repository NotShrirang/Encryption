#Encryption
import random

def Encrypt(x):
    m=len(list(x))
    i=0
    y=str()
    mylist=[]
    while i<m:
        ch=x[i]
        ch = bytes(ch, 'utf-8')
        r=random.randint(0,5)
        s=bytes([ch[0] + r])
        s=str(s)
        y=y+s[2]
        i=i+1
        f = open("Answer Key.txt", "a")
        f.write(str(r))
##        print(r)
##    print("Encrypted Message :", y)
    f = open("Encrypted Message.txt", "w")
    f.write(y)
    f.close()

#x=input("Enter a string: ")
#Encrypt(x)
    

    
