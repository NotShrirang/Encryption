#password asker

from tkinter import *
from Encryption import Encrypt
from Decryption import Decrypt
root = Tk()
root.title("Password Asker")

def sign_in():
    password=entry.get()
    n=len(list(password))
    i=0
    a=list()
    while i<n:
        ch=password[i]
        ch = bytes(ch, 'utf-8')
##        f = open("Answer Key.txt", "r")
##        j = (f.readline())
        num = j[i]
        num = int(num)
        a.append(num)
        ch= y[i]
        ch= bytes(ch,'utf-8')
        s=bytes([ch[0] + num])
        s=str(s)
        x=x+s[2]
        i=i+1

def Change():
    Changed_Password=entry.get()
    Encrypt(Changed_Password)
    

entry = Entry(root, text = "")
entry.grid(row=0, column=0, columnspan = 3)

Display = Label(root, text="")
Display.grid(row=3, column=1, columnspan=3)

NewPasswordButton = Button(root, text="New Password", command=Change)
NewPasswordButton.grid(row=2,column=2)

Login_button = Button(root, text="Sign In", command=sign_in)
Login_button.grid(row=2,column=1)

