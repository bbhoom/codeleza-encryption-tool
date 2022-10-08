from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import mysql.connector
def transfer():
    global user
    f=open('tempuser.txt','r')
    user=f.readline()
    print('username in manage page=',user)
    f.close()
transfer()
my=mysql.connector.connect(host='localhost',user='root',database='project',password='password')
cursor=my.cursor()
def delete_langcreated():
    langcreated_screen.destroy()
    root.destroy()

def langcreated():
     global langcreated_screen
     langcreated_screen = Toplevel(root)
     langcreated_screen.title("Success")
     langcreated_screen.geometry("150x100")
     Label(langcreated_screen, text="Language created!",fg='green',font=('david',12)).pack()
     Button(langcreated_screen, text="OK", command=delete_langcreated).pack()
root = tk.Toplevel()
root.title('your language')
root.geometry('1500x1500')
lbl1 = Label(root, text = "assign your values")
lbl1.place( x=100, y=10)
lbl1.config(font =("Times new roman",10))
# Read the Image
image = Image.open("bg.png")
  
# Reszie the image using resize() method
resize_image = image.resize((1500, 1500))
img = ImageTk.PhotoImage(resize_image)

# Create Canvas
canvas= tk.Canvas(root, width = 400,height = 400)
      
canvas.pack(fill = "both", expand = True)
  
# Display image
canvas.create_image( 0, 0, image = img, anchor = "nw")
canvas.create_text(780, 25, text='Assign your characters', font=('Times new roman',35,'bold','italic'),fill='navajowhite1')
canvas.create_text(760, 60, text='Assign one character to each value and press done at the end', font=('times new roman',18),fill='white')
canvas.create_text(1160, 520, text='Assign a name for your language here.', font=('times new roman',15),fill='white')
txt=Entry(root, text="", bd=7)
txt.place(x=1060, y=540)
##canvas.create_text(1160, 650, text='Mention your username.', font=('times new roman',15),fill='white')
##txt10=Entry(root, text="", bd=7)
##txt10.place(x=1060, y=680)
l=[]
n=[]
entries=[]
names=[]
#dicts
c={}
lower={}
num={}
def printInput():
     global name
     global username
     global key
     name=txt.get()
     username=user
     if name=='':
          name_error()
     else:
          upload()
          n.append(name)
          a=0
          j=97
          jj=65
          jjj=48
          global c
          for i in l:
             a+=1  
             value=i.get()
             entries.append(value)
             if a<=26:
                  key=chr(j)
                  SQL='''INSERT INTO {}
                         VALUES("{}","{}","{}");'''.format(langl,name,key,value)
                  cursor.execute(SQL)
                  my.commit()
                  lower[key]=value
                  j=j+1
             elif a<=52 and a>26:
                  key=chr(jj)
                  c[key]=value
                  sql='insert into {} Values("{}","{}","{}");'.format(langc,name,key,value) 
                  cursor.execute(sql)
                  my.commit() 
                  jj+=1
             elif a>51 and a<63:
                  key=chr(jjj)
                  num[key]=value
                  sql='insert into {} Values("{}","{}","{}");'.format(langn,name,key,value)
                  cursor.execute(sql)
                  my.commit()
                  jjj+=1
                  
                  
          print(lower)
          print(c)
          print(num)
          print(entries)
          for i in range (26):
              names.append(name)
          langcreated()
def upload():
     global langl
     global langc
     global langn
     SQL='INSERT INTO langname VALUES("{}","{}");'.format(username,name)
     cursor.execute(SQL)
     my.commit()
     
     langc=name+'c'
     langl=name+'l'
     langn=name+'n'
     sql='''create table {}
            (langname char(30),
             english char(30),
             code char(30));'''.format(langc)
     cursor.execute(sql)
     my.commit()
     key=list(c.keys())
     value=list(c.values())
     sql='''create table {}
            (langname char(30),
             english char(30),
             code char(30));'''.format(langl)
     cursor.execute(sql)
     my.commit()
     sql='''create table {}
            (langname char(30),
             english char(30),
             code char(30));'''.format(langn)
     cursor.execute(sql)
     my.commit()
def name_error():
    global name_error_screen
    name_error_screen = Toplevel()
    name_error_screen.title("Error")
    name_error_screen.geometry("150x100")
    Label(name_error_screen, text="Name Not Found",fg="red").pack()
    Button(name_error_screen, text="Insert a name", command=name_error_screen_delete).pack()

def name_error_screen_delete():
     name_error_screen.destroy()
     
     
#lower case till q
j=90
while j<=500:
  for i in range(97,115):
    txtfld=Entry(root, text="", bd=5)
    txtfld.place(x=250, y=j)
    l.append(txtfld)
    lbl2 = Label(root, text = chr(i))
    lbl2.place( x=230, y=j)
    lbl2.config(font =("Courier", 13))
    j+=35
#lower case after q
j=90
while j<=335:
  for i in range(115,123):
    txtfld=Entry(root, text="", bd=5)
    txtfld.place(x=450, y=j)
    l.append(txtfld)
    lbl2 = Label(root, text = chr(i))
    lbl2.place( x=430, y=j)
    lbl2.config(font =("Courier", 13))
    j+=35
##capitals
j=90    
while j<=500:
  for i in range(65,83):
    txt1=Entry(root, text="", bd=5)
    txt1.place(x=700, y=j)
    l.append(txt1)
    lbl3 = Label(root, text = chr(i))
    lbl3.place( x=680, y=j)
    lbl3.config(font =("Courier", 13))
    j+=35

j=90    
while j<=335:
  for i in range(83,91):
    txt1=Entry(root, text="", bd=5)
    txt1.place(x=900, y=j)
    l.append(txt1)
    lbl3 = Label(root, text = chr(i))
    lbl3.place( x=880, y=j)
    lbl3.config(font =("Courier", 13))
    j+=35
#numbers
j=90
while j<=240:
  for i in range(48,58):
    txt2=Entry(root, text="", bd=5)
    txt2.place(x=1200, y=j)
    l.append(txt2)
    lbl4 = Label(root, text = chr(i))
    lbl4.place( x=1180, y=j)
    lbl4.config(font =("Courier", 13))
    j+=35   
btn1 = Button(root,text=' Done ', command = printInput,fg='white',bg='navy blue')
btn1.place(x=750, y=730)
btn1.config(font =("Times new roman", 14),height="1", width="5")

               

