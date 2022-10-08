from tkinter import *
import tkinter as tk
from PIL import  Image,ImageTk
from tkinter import messagebox
import mysql.connector
my=mysql.connector.connect(host='localhost',user='root',database='project',password='password')
cursor=my.cursor()
def transfer():
    global user1
    f=open('tempuser.txt','r')
    user1=f.read()
    print('username in convert page=',user1)
    f.close()

transfer()
def sec():
    global lval
    global cval
    global nval
    lang=name.get()
    if lang not in r:
        messagebox.showerror('Error','Language not found \n Please enter available lamguage name')
    else:
        root = Toplevel(main_screen)
        root.title('Update language')
        root.geometry('1500x1500')
        assign=StringVar()
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
        namec=lang+'c'
        namel=lang+'l'
        namen=lang+'n'
        cval=[]
        lval=[]
        nval=[]
        SQL='select code from {};'.format(namec)
        cursor.execute(SQL)
        while True:
            data=cursor.fetchone()
            if data==None:
                break
            else:
                key=data[0]
                cval.append(key)
        SQL='select code from {};'.format(namel)
        cursor.execute(SQL)
        while True:
            data=cursor.fetchone()
            if data==None:
                break
            else:
                key=data[0]
                lval.append(key)
        SQL='select code from {};'.format(namen)
        cursor.execute(SQL)
        while True:
            data=cursor.fetchone()
            if data==None:
                break
            else:
                key=data[0]
                nval.append(key)
        canvas.create_text(780, 20, text='Assign your new characters', font=('Times new roman',25,'bold','italic'),fill='navajowhite1')
        canvas.create_text(760, 60, text='Assign one character to each value and press done at the end', font=('david',15),fill='white')
        canvas.create_text(1160, 520, text='Assign a name for your language here.', font=('david',15),fill='white')
        v=name.get()
        txt=Entry(root, textvariable=assign, bd=7)
        assign.set(v)
        txt.place(x=1060, y=540)
        l=[]
        n=[]
        c=[]
        entries=[]
        names=[]
        #dicts
        c1={}
        lower={}
        num={}
        def printInput():
             global name
             global username
             global key
             name=txt.get()
             username=user1
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
                          c1[key]=value
                          sql='insert into {} Values("{}","{}","{}");'.format(langc,name,key,value) 
                          cursor.execute(sql)
                          my.commit() 
                          jj+=1
                     elif a>52 and a<=62:
                          key=chr(jjj)
                          num[key]=value
                          sql='insert into {} Values("{}","{}","{}");'.format(langn,name,key,value)
                          cursor.execute(sql)
                          my.commit()
                          jjj+=1
                  for i in range (26):
                      names.append(name)
                  messagebox.showinfo("success", "Language Updated")  
                  main_screen.destroy()
        def upload():
             global langl
             global langc
             global langn
             langc=name+'c'
             langl=name+'l'
             langn=name+'n'
           #command to delete to table
             sql='drop table {};'.format(langc);
             cursor.execute(sql)
             my.commit()
             sql='drop table {};'.format(langl);
             cursor.execute(sql)
             my.commit()
             sql='drop table {};'.format(langn);
             cursor.execute(sql)
             my.commit()
             
             sql='''create table {}
                    (langname char(30),
                     english char(30),
                     code char(30));'''.format(langc)
             cursor.execute(sql)
             my.commit()
             key=list(c1.keys())
             value=list(c1.values())
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
        a=0
        while j<=500:
          for i in range(97,115):
            texti=StringVar()
            txtfld=Entry(root, textvariable=texti, bd=5)
            txtfld.place(x=250, y=j)
            texti.set(lval[a])
            l.append(txtfld)
            lbl2 = Label(root, text = chr(i))
            lbl2.place( x=230, y=j)
            lbl2.config(font =("Courier", 13))
            j+=35
            a+=1
        #lower case after q
        j=90
        while j<=335:  
          for i in range(115,123):
            textj=StringVar()  
            txtfld=Entry(root, textvariable=textj, bd=5)
            txtfld.place(x=450, y=j)
            textj.set(lval[a])
            l.append(txtfld)
            lbl2 = Label(root, text = chr(i))
            lbl2.place( x=430, y=j)
            lbl2.config(font =("Courier", 13))
            j+=35
            a+=1
            
        ##capitals
        j=90
        b=0
        while j<=500:
          for i in range(65,83):
            textk=StringVar()
            txt1=Entry(root, textvariable=textk, bd=5)
            txt1.place(x=700, y=j)
            textk.set(cval[b])
            l.append(txt1)
            lbl3 = Label(root, text = chr(i))
            lbl3.place( x=680, y=j)
            lbl3.config(font =("Courier", 13))
            j+=35
            b+=1

        j=90    
        while j<=335:
          for i in range(83,91):
            textl=StringVar()
            txt1=Entry(root, textvariable=textl, bd=5)
            txt1.place(x=900, y=j)
            textl.set(cval[b])
            l.append(txt1)
            lbl3 = Label(root, text = chr(i))
            lbl3.place( x=880, y=j)
            lbl3.config(font =("Courier", 13))
            j+=35
            b+=1
        #numbers
        j=90
        c=0
        while j<=240:
          for i in range(48,58):
            textm=StringVar()
            txt2=Entry(root, textvariable=textm, bd=5)
            txt2.place(x=1200, y=j)
            textm.set(nval[c])
            l.append(txt2)
            lbl4 = Label(root, text = chr(i))
            lbl4.place( x=1180, y=j)
            lbl4.config(font =("Courier", 13))
            j+=35
            c+=1
        btn1 = Button(root,text=' Done ', command = printInput,fg='white',bg='navy blue')
        btn1.place(x=750, y=730)
        btn1.config(font =("Courier", 14),height="1", width="5")
        root.mainloop()


   


#___main screen___
def main():
    global name
    global canvas
    global main_screen
    global r
    main_screen = tk.Toplevel()
    main_screen.geometry("500x500")
    name=StringVar()

    # Read the Image
    image = Image.open("bg.png")

    # Reszie the image using resize() method
    resize_image = image.resize((500, 500))
    img = ImageTk.PhotoImage(resize_image)

    # Create Canvas
    canvas = Canvas(main_screen, width = 400,height = 400)

    canvas.pack(fill = "both", expand = True)

    # Display image
    canvas.create_image( 0, 0, image = img, anchor = "nw")
    # Add Text
    canvas.create_text(30,20, text = "Update your language",font=("times new roman", 20),fill='navajowhite1',anchor='nw')
    canvas.create_text(30,80, text = "Your exsisting languages are:",font=("times new roman", 16,'bold','italic'),fill='white',anchor='nw')
    sql='''select lang from langname
           where username="{}";'''.format(user1)
    r=[]
    cursor.execute(sql)
    while True:
        data=cursor.fetchone()
        if data==None:
            break
        else:
            r.append(data[0])
    jj=110
    for x in r:
        # Add Text
        canvas.create_text(30,jj, text = x,font=("times new roman", 16),fill='white',anchor='nw')
        jj+=40
    # Add Text
    canvas.create_text(70,320, text = "Please enter name of the language:",font=("david",15),fill='white',anchor='nw')
    #entry box
    langname_entry = tk.Entry(main_screen,textvariable=name)
    canvas.create_window(100,370,width=250,height=50,window=langname_entry,anchor='nw')
    #add buttons
    button1=Button(main_screen,text="Ok", height="1", width="3",command =sec,font=("Baskerville Old Face ",14),fg='white',bg='navy blue')
    button1_canvas = canvas.create_window(200,450, anchor = "nw",window = button1)
    main_screen.mainloop()
main()
my.close()
   
