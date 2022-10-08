from tkinter import *
import tkinter as tk
from PIL import  Image,ImageTk
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
def delete_lang_not_found_screen():
    lang_not_found_screen.destroy()
def error():
    global lang_not_found_screen
    lang_not_found_screen = Toplevel(main_screen)
    lang_not_found_screen.title("Error")
    lang_not_found_screen.geometry("150x100")
    Label(lang_not_found_screen, text="Lang Not Found",fg="red").pack()
    Button(lang_not_found_screen, text="Try Again", command=delete_lang_not_found_screen).pack()
def delete():
      canvas1.delete(label)
def delete1():
      canvas3.delete(label1)

def next():
    global canvas2
    lang=name.get()
    if lang=='' or lang not in r:
        error()
    else:
        root = Toplevel(main_screen)
        root.title('Convert')
        root.geometry('500x500')
        sen=StringVar()
        # Read the Image
        image = Image.open("bg.png")

        # Reszie the image using resize() method
        resize_image = image.resize((500, 500))
        img = ImageTk.PhotoImage(resize_image)

        # Create Canvas
        canvas2 = Canvas(root, width = 400,height = 400)

        canvas2.pack(fill = "both", expand = True)

        # Display image
        canvas2.create_image( 0, 0, image = img, anchor = "nw")

        # Add Text
        canvas2.create_text(125,20, text = "Choose your choice",font=("times new roman", 20,'bold'),fill='navajowhite1',anchor='nw')
        #add buttons
        button1=Button(root,text="English --> Code language", height="2", width="24",command =con,font=("Baskerville Old Face ",12),fg='white',bg='navy blue')
        button2=Button(root,text="Code language --> English", height="2", width="24",command =get,font=("Baskerville Old Face ",12),fg='white',bg='navy blue')
        button2_canvas = canvas2.create_window(100,150, anchor = "nw",window = button2)
        button1_canvas = canvas2.create_window(100,250, anchor = "nw",window = button1)

        root.mainloop()

#from code to english
def get():
    global canvas3
    global sentence
    root = Toplevel(main_screen)
    root.title('Code to English')
    root.geometry('500x500')
    sentence=StringVar()
    # Read the Image
    image = Image.open("bg.png")

    # Reszie the image using resize() method
    resize_image = image.resize((500, 500))
    img = ImageTk.PhotoImage(resize_image)

    # Create Canvas
    canvas3 = Canvas(root, width = 400,height = 400)

    canvas3.pack(fill = "both", expand = True)

    # Display image
    canvas3.create_image( 0, 0, image = img, anchor = "nw")



    # Add Text
    canvas3.create_text(155,20, text = "Enter you sentence",font=("times new roman", 20),fill='navajowhite1',anchor='nw')
    #entry box
    langname_entry = tk.Entry(root,textvariable=sentence)
    canvas3.create_window(7,70,width=482,height=50,window=langname_entry,anchor='nw')
    #add buttons
    button1=Button(root,text="Convert", height="2", width="9",command =d,font=("Baskerville Old Face ",12),fg='white',bg='navy blue')
    button1_canvas = canvas3.create_window(200,150, anchor = "nw",window = button1)
    button2=Button(root,text="Type again", height="2", width="9",command =delete1,font=("Baskerville Old Face ",12),fg='white',bg='navy blue')
    button2_canvas = canvas3.create_window(200,220, anchor = "nw",window = button2)
    root.mainloop()
    
def d():
    global label1
    y=sentence.get()
    lang=name.get()
    namec=lang+'c'
    namel=lang+'l'
    namen=lang+'n'
    c={}
    l={}
    n={}
    SQL='select code,english from {};'.format(namec)
    cursor.execute(SQL)
##    my.commit()
    while True:
        data=cursor.fetchone()
        if data==None:
            break
        else:
            key=data[0]
            value=data[1]
            c[key]=value
    SQL='select code,english from {};'.format(namel)
    cursor.execute(SQL)
##    my.commit()
    while True:
        data=cursor.fetchone()
        if data==None:
            break
        else:
            key=data[0]
            value=data[1]
            l[key]=value
    SQL='select code,english from {};'.format(namen)
    cursor.execute(SQL)
##    my.commit()
    while True:
        data=cursor.fetchone()
        if data==None:
            break
        else:
            key=data[0]
            value=data[1]
            n[key]=value

    ns=''
    for j in y:
          if ord(j)>=65 and ord(j)<=91:
            for k in c:
                if j==k:
                    ns+=str(c[k])
                else:
                    continue
          elif ord(j)>=97 and ord(j)<=123:
            for k in l:
                if j==k:
                    ns+=str(l[k])
                else:
                    continue
          elif ord(j)>=48 and ord(j)<=57:
            for k in n:
                if j==k:
                   ns+=str(n[k]) 
                else:
                  continue
          else:
             ns+=str(j)
    # Add Text
    label1=canvas3.create_text(150,280, text = ns ,font=("gill sans ultra bold",22),fill='white')

    
#from english to code
def c():
    global label
    global ns
    y=sen.get()
    lang=name.get()
    namec=lang+'c'
    namel=lang+'l'
    namen=lang+'n'
    c={}
    l={}
    n={}
    SQL='select english,code from {};'.format(namec)
    cursor.execute(SQL)
##    my.commit()
    while True:
        data=cursor.fetchone()
        if data==None:
            break
        else:
            key=data[0]
            value=data[1]
            c[key]=value
    SQL='select english,code from {};'.format(namel)
    cursor.execute(SQL)
    while True:
        data=cursor.fetchone()
        if data==None:
            break
        else:
            key=data[0]
            value=data[1]
            l[key]=value
    SQL='select english,code from {};'.format(namen)
    cursor.execute(SQL)
    while True:
        data=cursor.fetchone()
        if data==None:
            break
        else:
            key=data[0]
            value=data[1]
            n[key]=value

    ns=''
    for j in y:
          if ord(j)>=65 and ord(j)<=91:
            for k in c:
                if j==k:
                    ns+=str(c[k])
                else:
                    continue
          elif ord(j)>=97 and ord(j)<=123:
            for k in l:
                if j==k:
                    ns+=str(l[k])
                else:
                    continue
          elif ord(j)>=48 and ord(j)<=57:
            for k in n:
                if j==k:
                   ns+=str(n[k]) 
                else:
                  continue
          else:
             ns+=str(j)
    # Add Text
    label=canvas1.create_text(150,280, text = ns ,font=("gill sans ultra bold",22),fill='white')
def con():
    global canvas1
    global sen
    global root

    root = Toplevel(main_screen)
    root.title('English to code')
    root.geometry('500x500')
    sen=StringVar()
    # Read the Image
    image = Image.open("bg.png")

    # Reszie the image using resize() method
    resize_image = image.resize((500, 500))
    img = ImageTk.PhotoImage(resize_image)

    # Create Canvas
    canvas1 = Canvas(root, width = 400,height = 400)

    canvas1.pack(fill = "both", expand = True)

    # Display image
    canvas1.create_image( 0, 0, image = img, anchor = "nw")



    # Add Text
    canvas1.create_text(155,20, text = "Enter you sentence",font=("times new roman", 20),fill='navajowhite1',anchor='nw')
    #entry box
    langname_entry = tk.Entry(root,textvariable=sen)
    canvas1.create_window(7,70,width=482,height=50,window=langname_entry,anchor='nw')

    #add buttons
    button1=Button(root,text="Convert", height="2", width="9",command =c,font=("Baskerville Old Face ",12),fg='white',bg='navy blue')
    button1_canvas = canvas1.create_window(200,150, anchor = "nw",window = button1)
    button2=Button(root,text="Type again", height="2", width="9",command =delete,font=("Baskerville Old Face ",12),fg='white',bg='navy blue')
    button2_canvas = canvas1.create_window(200,210, anchor = "nw",window = button2)
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
    canvas.create_text(30,20, text = "Convert your text",font=("times new roman", 20),fill='navajowhite1',anchor='nw')
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
    canvas.create_text(70,340, text = "Please enter name of the language:",font=("david",15),fill='white',anchor='nw')
    #entry box
    langname_entry = tk.Entry(main_screen,textvariable=name)
    canvas.create_window(100,380,width=250,height=50,window=langname_entry,anchor='nw')
    #add buttons
    button1=Button(main_screen,text="Ok", height="1", width="3",command =next,font=("Baskerville Old Face ",14),fg='white',bg='navy blue')
    button1_canvas = canvas.create_window(200,450, anchor = "nw",window = button1)
    main_screen.mainloop()
main()
my.close()  
    
