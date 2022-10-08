from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import csv



#cursor instance
my=mysql.connector.connect(host='localhost',user='root',database='project',password='password')
cursor=my.cursor()



def insert(data):
    trv1.delete(*trv1.get_children())
    for i in data:
        trv1.insert('','end',values=i)

def get_user(event):
    item=trv1.item(trv1.focus())
    Username.set(item['values'][0])
    Password.set(item['values'][1])

    
    

def trv():
    #treeview showing all the reminders
    global trv1
    trv1=ttk.Treeview(user_frame,yscrollcommand=user_scroll.set,columns=(1,2,3),show="headings",height="5")
    trv1.pack()

    #assigning headings
    trv1.heading(1,text="Username")
    trv1.heading(2,text="Password")
    code="select * from userinfo order by username;"
    cursor.execute(code)
    data=cursor.fetchall()
    print(data)
    insert(data)
    trv1.bind('<Double 1>',get_user)

#Resets screen to original Interface
def clear():
    trv1.destroy()
    trv()



#Delete Rem
def del_user():
    L=[]
    usern=Username.get()
    query="delete from userinfo where Username='{}';".format(usern)
    cursor.execute(query)
    my.commit()
    del_rem_success()
    code="select * from userinfo order by username;"
    cursor.execute(code)
    data=cursor.fetchall()
    for i in data:
        L.append(list(i))
    f=open('username.csv','w',newline='')
    w=csv.writer(f)
    w.writerows(L)
    f.close()
    user_Options()
    clear()

#Deleted rem success
def del_rem_success():
    global del_rem_success_screen
    del_rem_success_screen = Toplevel(user_others)
    del_rem_success_screen.title("Success")
    del_rem_success_screen.geometry("250x150")
    lbl=Label(del_rem_success_screen,text="User Deleted Successfully!\nCLick Ok to go back")
    lbl.pack(side=tk.TOP,pady=10)
    btn=Button(del_rem_success_screen,text="Ok",command=delRem_success)
    btn.pack(side=tk.TOP,pady=10)

#Delete del_rem popup
def delRem_success():
    del_rem_success_screen.destroy()

def user_Options():
    global Username
    global Password
    global Email
    Email=StringVar()
    Username=StringVar()
    Password=StringVar()
    
    lbl1=Label(user_others,text="Username :")
    lbl1.grid(row=0,column=0,padx=5,pady=3)
    ent1=Entry(user_others,textvariable=Username)
    ent1.grid(row=0,column=1,padx=5,pady=3)

    lbl2=Label(user_others,text="Password :")
    lbl2.grid(row=1,column=0,padx=5,pady=3) 
    ent2=Entry(user_others,textvariable=Password)
    ent2.grid(row=1,column=1,padx=5,pady=3)


    
    option3=Button(user_others,text="Delete User",command=del_user)
    option3.grid(row=4,column=1,padx=5,pady=3)
    
    option2=Button(user_others,text="Close",command=back)
    option2.grid(row=4,column=0,padx=5,pady=3)

def back():
    import registercsv
    admin()
def admin():
    user_app.destroy()

def user_list():
    #base screen
    global user_scroll
    global user_frame
    global user_app
    global user_part
    global user_others
    user_app=Tk()
    user_app.title("Users")
    user_app.geometry("850x600")
    user_part = LabelFrame(user_app,text="Registered Users")
    user_part.pack(fill = "both", expand="yes",padx=20,pady=10)
    user_others = LabelFrame(user_app, text="User Options") 
    user_others.pack(fill="both", expand="yes",padx=20,pady=10)
    #Treeview scrollbar
    user_frame= Frame(user_part)
    user_frame.pack()
    user_scroll=Scrollbar(user_frame)
    user_scroll.pack(fill="y",side=RIGHT)
    trv()
    user_scroll.config(command=trv1.yview)


    user_Options()
    user_app.mainloop()

user_list()
my.close()
