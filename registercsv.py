from tkinter import *
import tkinter as tk
from tkinter import ttk
import csv
import os
import messagebox
from PIL import Image,ImageTk

def username_transfer():
    user=username1
    f=open('tempuser.txt','w')
    f.write(user)
    f.close()
import mysql.connector
my=mysql.connector.connect(host='localhost',user='root',database='project',password='password')
cursor=my.cursor()
if my.is_connected():
    print('Database connected')
def bn():
    os.system('python reg bg.py')
    

###___csvheading___
##f=open('username.csv','w',newline='')
##w=csv.writer(f)
##l=['username','password']
##w.writerow(l)
##f.close()


# Deleting popups
def delete_username_used():
    username_used_screen.destroy()
 
def delete_login_success():
    login_success_screen.destroy()

def delete_login():
    login_screen.destroy()

def delete_register():
    register_screen.destroy()
    
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def delete_main():
    main_screen.destroy()

#login sucess ok button command
def f():
   delete_login()
   delete_login_success()
   delete_main()
   import manage
   
    

# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    global canvas2
    username = StringVar()
    password = StringVar()
    # Read the Image
    image = Image.open("bg.png")
      
    # Reszie the image using resize() method
    resize_image = image.resize((300, 250))
    img = ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas2= tk.Canvas(register_screen, width = 400,height = 400)
      
    canvas2.pack(fill = "both", expand = True)
      
    # Display image
    canvas2.create_image( 0, 0, image = img, anchor = "nw")
    
    # Add Text
    canvas2.create_text(150,25, text = "Please enter details below",font=("david",12),fill='white')
    canvas2.create_text(120,58, text="Username * ",font=("david", 12),fill='white')
    canvas2.create_text(120,112, text="Password * ",font=("david", 12),fill='white')
    #entry box
    username_entry = tk.Entry(register_screen,textvariable=username)
    canvas2.create_window(140,80, window=username_entry)
    password_entry = tk.Entry(register_screen,textvariable=password, show='*')
    canvas2.create_window(140,130, window=password_entry)
    #add buttons
    button1=Button(register_screen,text="Register", height="1", width="10",command = register_user,font=("david", 10),bg='navy blue',fg='white')
    button2=Button(register_screen,text="Done", height="1", width="10",command=delete_register and login,font=("david", 10),bg='navy blue',fg='white')
    # Display Buttons
    button1_canvas = canvas2.create_window( 96, 160,anchor = "nw",window = button1)
    button2_canvas = canvas2.create_window( 96, 210,anchor = "nw",window = button2)
    register_screen.mainloop()

# Designing window for login 
 
def login():
    global canvas3
    global login_screen
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")


    # Read the Image
    image = Image.open("bg.png")
      
    # Reszie the image using resize() method
    resize_image = image.resize((300, 250))
    img = ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas3= tk.Canvas(login_screen, width = 400,height = 400)
      
    canvas3.pack(fill = "both", expand = True)
      
    # Display image
    canvas3.create_image( 0, 0, image = img, anchor = "nw")
    
    # Add Text
    canvas3.create_text(150,25, text = "Please enter details below to login",font=("david",12),fill='white')
    canvas3.create_text(120,58, text="Username * ",font=("david", 12),fill='white')
    canvas3.create_text(120,112, text="Password * ",font=("david", 12),fill='white')
    #entry box
    username_login_entry = tk.Entry(login_screen,textvariable=username_verify)
    canvas3.create_window(140,80, window=username_login_entry)
    password_login_entry= tk.Entry(login_screen,textvariable=password_verify, show='*')
    canvas3.create_window(140,130, window=password_login_entry)
    #add buttons
    button1=Button(login_screen,text="Login", height="1", width="10",command = login_verify,font=("david", 10),bg='navy blue',fg='white')
    # Display Buttons
    button1_canvas = canvas3.create_window(96, 170,anchor = "nw",window = button1)
    login_screen.mainloop()

 
# Implementing event on register button

def register_user():
    d=[]
    username_info = username.get()
    password_info = password.get()
    file = open('username.csv', "r+",newline='')
    w=csv.writer(file)
    r=csv.reader(file)
    #defining verification's conditions 
    for i in r:
       try:
           if i[0]==username_info:
                username_used()
                break
       except IndexError:
           continue
    else:
         d.append(username_info)
         d.append(password_info)
         w.writerow(d)
         print(d)
         SQL='INSERT INTO userinfo VALUES("{}","{}");'.format(username_info,password_info)
         cursor.execute(SQL)
         my.commit()
         canvas2.create_text(150,198, text = "Registration Success!Now click on done.",font=("calibri", 12),fill='white')
    file.close()

    
def username_used():
    global username_used_screen
    username_used_screen = Toplevel(register_screen)
    username_used_screen.title("Error")
    username_used_screen.geometry("150x100")
    Label(username_used_screen, text="Username unavailable",fg="red").pack()
    Button(username_used_screen, text="Try another", command=delete_username_used  ).pack()
# Implementing event on login button

def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    file1 = open('username.csv', "r",newline='')
    r=csv.reader(file1)
##    for i in r:
    try:
        if username1=='admin':
            if password1=='admin':
                admin_popup()
        else:
            for i in r:
              if i[0]==username1:
                   if i[1]==password1:
                      login_sucess()
                      break
                   else :
                      password_not_recognised()
                      break
            else:
              user_not_found()

  
    except IndexError:
           x=1
    file1.close()
    username_transfer()

# Designing popup for login success
def login_sucess():
    global f
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success",fg='green',font=('david',13)).pack()
    Button(login_success_screen, text="OK", command=f).pack()


 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password",fg="red").pack()
    Button(password_not_recog_screen, text="Try Again", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    messagebox.showerror("Error","User not found \n Try again")
#Admin options
    
def admin_popup():
    global admin_screen
    admin_screen = Toplevel(main_screen)
    admin_screen.title("Admin Options")
    admin_screen.geometry("300x330")
    # Read the Image
    image = Image.open("bg.png")
      
    # Reszie the image using resize() method
    resize_image = image.resize((300, 330))
    img = ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas2= tk.Canvas(admin_screen, width = 300,height = 330)
    canvas2.pack(fill = "both", expand = True)
      
    # Display image
    canvas2.create_image( 0, 0, image = img, anchor = "nw")
    
    # Add Text
    canvas2.create_text(150,25, text = "Welcome back, Admin!",font=("arial",20),fill='navajowhite')

    #add buttons
    button1=Button(admin_screen,text="Users", height="3", width="20",command = user,font=("david", 12),fg='white',bg='navy blue')
    button2=Button(admin_screen,text="Languages", height="3", width="20",command= reminder_list ,font=("david", 12),fg='white',bg='navy blue')
    button3=Button(admin_screen,text="Close", height="3",width="20",command= del_adminscreen ,font=("david", 12),fg='white',bg='navy blue')
    # Display Buttons
    button1_canvas = canvas2.create_window( 46, 80,anchor = "nw",window = button1)
    button2_canvas = canvas2.create_window( 46, 160,anchor = "nw",window = button2)
    button3_canvas = canvas2.create_window( 46, 240,anchor = "nw",window = button3)
    admin_screen.mainloop()

def del_adminscreen():
    admin_screen.destroy()

def user():
##    del_adminscreen()
##    main_screen.destroy()
    import admin

def reminder_list():
    #base screen
    lang_screen =Toplevel(admin_screen)
    lang_screen.title("Admin Options")
    lang_screen.geometry("600x630")
    # Read the Image
    image = Image.open("bg.png")
      
    # Reszie the image using resize() method
    resize_image = image.resize((600,630))
    img = ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas2= tk.Canvas(lang_screen, width = 600,height =630)
    canvas2.pack(fill = "both", expand = True)
      
    # Display image
    canvas2.create_image( 0, 0, image = img, anchor = "nw")
    L=[]
    canvas2.create_text(300,50, text ="The existing languages in the database are",font=("david",20),fill='navajowhite')
    canvas2.create_text(100,100, text ="Username",font=("david",18),fill='white')
    canvas2.create_text(400,100, text ="Language",font=("david",18),fill='white')
    sql='''SELECT * from langname;'''
    cursor.execute(sql)
    data=cursor.fetchall()
    for i in data:
        L.append(list(i))
    jj=150
    j=100
    k=400
    for i in L:
        canvas2.create_text(j,jj, text = i[0],font=("david",16),fill='white')
        canvas2.create_text(k,jj, text = i[1],font=("david",16),fill='white')
        jj+=50
    lang_screen.mainloop()
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("2000x1500")
    # Read the Image
    image = Image.open("bg.png")
      
    # Reszie the image using resize() method
    resize_image = image.resize((2100, 1600))
    img = ImageTk.PhotoImage(resize_image)
    
    # Create Canvas
    canvas1 = Canvas(main_screen, width = 400,height = 400)
      
    canvas1.pack(fill = "both", expand = True)
      
    # Display image
    canvas1.create_image( 0, 0, image = img, anchor = "nw")
    
    # Add Text
    canvas1.create_text(740,150, text = "Welcome to Codeleza",font=("times new roman", 45,'bold','italic'),fill='navajowhite1')
    canvas1.create_text(750,365, text = "New here? Register now!",font=("david", 20),fill='white')

    #add buttons
    button1=Button(main_screen,text="Login", height="3", width="30",command = login,font=("david", 20),fg='white',bg='navy blue')
    button2=Button(main_screen,text="Register", height="3", width="30",command=register,font=("david", 20),fg='white',bg='navy blue')
    # Display Buttons
    button1_canvas = canvas1.create_window( 500, 200, anchor = "nw",window = button1)
    button2_canvas = canvas1.create_window( 500, 400,anchor = "nw",window = button2)
    main_screen.mainloop()
main_account_screen()
my.close()

 

