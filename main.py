import mysql.connector
import sys
from tkinter import *

"""
Before starting this project, you should already have a database, username and password.
And there should be a table with columns :- Name, Password, and the tabe name is "pass"
"""

connection = mysql.connector.connect(host='sql6.freemysqlhosting.net',
                                         database='DATABASE',
                                         user='USERNAME',
                                         password='PASSWORD')

cursor = connection.cursor()

def ins():
    nn=input("Enter Name to be Added - ")
    mm=int(input("Enter password for "+nn+" - "))
    inserr = "INSERT INTO pass (Name, Password) VALUES ('"+nn+"', "+str(mm)+")"
    cursor.execute(inserr)
    print()
       
    
def sign():
    s=Tk()
    s.geometry("400x250")
    s.title("Sign in")
    
    nms=[]
    pas=[]
    
    select_pass_query = "SELECT Name, Password FROM pass"
    cursor.execute(select_pass_query)
    for row in cursor.fetchall():
       nms.append(row[0])
       pas.append(row[1])

    Label(s, text=' ').pack()
    Label(s, text="Enter username - ").pack()
    x1=Entry(s)
    x1.pack()
    Label(s, text=' ').pack()
    Label(s, text="Enter Password - ").pack()
    y1=Entry(s)
    y1.pack()

    def sub():
        x=x1.get()
        y=int(y1.get())

        bl=False
        i=0
        while i<len(nms):
            if nms[i]==x:
                if y==pas[i]:
                    wel=Tk()
                    Label(wel, text="WELCOME!").pack()
                    wel.mainloop()
                    break
                else:
                    ad=Tk()
                    Label(ad, text="Access Denied!").pack()
                    ad.mainloop()
                    break
            i+=1

    Label(s, text=' ').pack()
    Button(s, text='Submit', command=sub).pack()


from tkhtmlview import HTMLLabel
import tkinter.font as tkFont

root = Tk()
root.geometry("400x250")

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
Label(root, text=' ').pack()
Label(root, text='Login System', font=fontStyle).pack()
Label(root, text='______________').pack()
Label(root, text=' ').pack()
Button(root, text="Login", command=sign).pack()
Label(root, text=' ').pack()
Button(root, text="Register", command=ins).pack()

root.mainloop()

 
