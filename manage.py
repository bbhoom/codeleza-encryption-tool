from tkinter import *
import tkinter as tk
from PIL import  Image,ImageTk
import mysql.connector
import messagebox

# to get variable username from register csv file
def transfer():
    global user
    f=open('tempuser.txt','r')
    user=f.readline()
    print('username in manage page=',user)
    f.close()
my=mysql.connector.connect(host='localhost',user='root',database='project',password='password')
cursor=my.cursor()
if my.is_connected():
    print('Database connected')
    transfer()
def c():
    import Createlangintro
def convert():
    import convert


    

    
def langname_screen():
    root = Toplevel(main_screen)
    root.title('Manage')
    root.geometry('500x500')
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
    canvas1.create_text(50,50, text = "Your existing languages are:",font=("times new roman", 25),fill='navajowhite2',anchor='nw')
    r=[]
    sql='''select lang from langname
           where  username='{}';'''.format(user)
    cursor.execute(sql)

    while True:
        data=cursor.fetchone()
        if data==None:
            break
        else:
            print(data)
            r.append(data)
    print(r)
    
    jj=140
    for x in r:
        # Add Text
        canvas1.create_text(80,jj, text = x,font=("gill sans ultra bold", 25),fill='white',anchor='nw')
        jj+=50
    root.mainloop()


    
def langname_used():
    global langname_used_screen
    langname_used_screen = Toplevel(delete_screen)
    langname_used_screen.title("Error")
    langname_used_screen.geometry("150x100")
    Label(langname_used_screen, text="Language Not Found",fg="red").pack()
    Button(langname_used_screen, text="Try Another", command=delete_langname_used).pack()

def delete_langname_used():
    langname_used_screen.destroy()
    
def update_screen():
    import update
        
def delete_screen():
    global delete_screen
    global langname
    global canvas2
    delete_screen = Toplevel(main_screen)
    delete_screen.title("Delete")
    delete_screen.geometry("300x150")
    langname = StringVar()
    # Read the Image
    image = Image.open("bg.png")
      
    # Reszie the image using resize() method
    resize_image = image.resize((300, 150))
    img = ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas2= tk.Canvas(delete_screen, width = 400,height = 450)
      
    canvas2.pack(fill = "both", expand = True)
      
    # Display image
    canvas2.create_image( 0, 0, image = img, anchor = "nw")
    # Add Text
    canvas2.create_text(150,25, text = "Enter name of the language",font=("david",12),fill='white')
    #entry box
    langname_entry = tk.Entry(delete_screen,textvariable=langname)
    canvas2.create_window(70,60, window=langname_entry,anchor='nw')
    #add buttons
    button1=Button(delete_screen,text="Ok", height="1", width="3",command =delete,font=("Baskerville Old Face ",12),fg='white',bg='navy blue')
    button1_canvas = canvas2.create_window( 90,90, anchor = "nw",window = button1)

    delete_screen.mainloop()
def delete():
    sql='''select lang from langname
           where username="{}";'''.format(user)
    r=[]
    cursor.execute(sql)
    while True:
        data=cursor.fetchone()
        if data==None:
            break
        else:
            r.append(data[0])
    Langname=langname.get()
    print(Langname)
    langnamec=Langname+'c'
    print(langnamec)
    langnamel=Langname+'l'
    langnamen=Langname+'n'
    if Langname=='' or Langname not in r:
        messagebox.showerror("Error","Language not found")
    else:
        sql='''delete from langname
               where lang='{}';'''.format(Langname)
        cursor.execute(sql)
        my.commit()
        sql='''Drop table {};'''.format(langnamec)
        cursor.execute(sql)
        my.commit()
        sql='''Drop table {};'''.format(langnamel)
        cursor.execute(sql)
        my.commit()
        sql='''Drop table {};'''.format(langnamen)
        cursor.execute(sql)
        my.commit()
        messagebox.showinfo("Success","Language Deleted")
        delete_screen.destroy()

def log():
    global log_screen
    log_screen = Toplevel(main_screen)
    log_screen.title("Log out")
    log_screen.geometry("190x80")
    Label(log_screen, text="Are you sure you want to log out?",fg="red").pack()
    Button(log_screen, text="Yes", command=log_out).pack()
def log_out():
    main_screen.destroy()
    import registercsv


    
def manage_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("2000x1500")
    # Read the Image
    image = Image.open("bg.png")
      
    # Reszie the image using resize() method
    resize_image = image.resize((2100, 1600))
    img=ImageTk.PhotoImage(resize_image)   
    # Create Canvas
    canvas = Canvas(main_screen, width = 400,height = 400)
    canvas.pack(fill = "both", expand = True)
      
    # Display image
    canvas.create_image( 0, 0, image = img, anchor = "nw")


    # Add Text
    canvas.create_text(760,120, text = "Manage your languages",font=("times new roman", 35,'bold','italic'),fill='navajowhite1')
    #add buttons
    button1=Button(main_screen,text="Create a new language", height="3", width="21",command = c,font=("Times new roman",17,'bold'),fg='white',bg='navy blue')
    button2=Button(main_screen,text="See existing languages", height="3", width="21",command =langname_screen,font=("Times new roman",17,'bold'),fg='white',bg='navy blue')
    button3=Button(main_screen,text="Update an existing language", height="3", width="21",command =update_screen,font=("Times new roman",17,'bold'),fg='white',bg='navy blue')
    button4=Button(main_screen,text="Delete existing language", height="3", width="21",command = delete_screen,font=("Times new roman",17,'bold'),fg='white',bg='navy blue')
    button5=Button(main_screen,text="Convert text", height="3", width="21",command = convert,font=("Times new roman",17,'bold'),fg='white',bg='navy blue')
    button6=Button(main_screen,text="Log out", height="1", width="5",command =log,font=("Times new roman",13,'bold'),fg='white',bg='navy blue')


    # Display Buttons
    button1_canvas = canvas.create_window( 600,220, anchor = "nw",window = button1)
    button2_canvas = canvas.create_window( 600,420, anchor = "nw",window = button2)
    button3_canvas = canvas.create_window( 600,520, anchor = "nw",window = button3)
    button4_canvas = canvas.create_window( 600,620, anchor = "nw",window = button4)
    button5_canvas = canvas.create_window( 600,320, anchor = "nw",window = button5)
    button6_canvas = canvas.create_window( 1400,20, anchor = "nw",window = button6)
    main_screen.mainloop()
manage_screen()
my.close()


