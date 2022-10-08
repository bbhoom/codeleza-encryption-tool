from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
def h():
    import create_final
root = tk.Toplevel()
root.title('Create your own Language')
root.geometry('520x400')
# Read the Image
image = Image.open("bg.png")
  
# Reszie the image using resize() method
resize_image = image.resize((550, 450))
img = ImageTk.PhotoImage(resize_image)

# Create Canvas
canvas2= tk.Canvas(root, width = 550,height = 500)
canvas2.pack(fill = "both", expand = True)
  
# Display image
canvas2.create_image( 0, 0, image = img, anchor = "nw")
fobj=open('intro.txt','r')
st=fobj.read()
fobj.close()
# Add Text
canvas2.create_text(250,40, text = "Creating a language!",font=("times new roman", 25,'bold','italic'),fill='navajowhite1')
canvas2.create_text(260,177, text=st,font=('gill sans ultra bold', 14),justify='left',fill='white')
#add buttons
button1=Button(root, text = 'Create my new language', command =h, height="1", width="20",font=("times new roman",17),fg='white',bg='navy blue')
# Display Buttons
button1_canvas = canvas2.create_window(120,270,anchor = "nw",window = button1)
root.mainloop()

