from tkinter import *
from PIL import Image,ImageTk ##pip install pillow
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title('Add a new Employee')
        self.root.wm_iconbitmap('images/icons.ico')
        self.root.geometry("1250x675+0+0")
        self.root.maxsize(1250, 675)
        self.root.minsize(1250,675)
        self.bg = ImageTk.PhotoImage(file='138728.jpg')
        bg = Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        self.left = ImageTk.PhotoImage(file='images/sideimage.png')
        left=Label(self.root,image=self.left).place(x = 80,y = 100,width=400,height=500)

        frame1=Frame(self.root,bg='white')
        frame1.place(x=480,y = 100,width=700,height=500)

        title = Label(frame1,text='Add New Employee',font=("Verdana",20,"bold"),bg="white",fg='green').place(x=50,y=30)
        lblFirstName = Label(frame1,text='First Name :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=80)
        lblLastName = Label(frame1,text='Last Name :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=110)
        txtFirstName = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtLastName = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtFirstName.place(x=150,y=80) 
        txtLastName.place(x=150,y=110) 
    
root=Tk()

obj = Register(root)
root.mainloop()