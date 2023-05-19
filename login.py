from tkinter import *
from PIL import Image,ImageTk ##pip install pillow
from tkinter import filedialog
from tkinter import ttk
import shutil
from sql import Database
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title('Login')
        self.root.wm_iconbitmap('images/icons.ico')
        self.root.geometry("1250x675+0+0")
        self.root.maxsize(1250,675)
        self.root.minsize(1250,675)
        self.bg = ImageTk.PhotoImage(file='138728.jpg')
        bg = Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        self.left = ImageTk.PhotoImage(file='images/sideimage.png')
        left=Label(self.root,image=self.left).place(x = 80,y = 100,width=400,height=500)

        frame1=Frame(self.root,bg='white')
        frame1.place(x=480,y = 100,width=700,height=500)

        self.lblLoginHead = Label(frame1,text='LOGIN',font=('Verdana',25,'bold'),bg='white',fg='#0373fc').place(x=25,y=25)
        self.lblLoginEmail = Label(frame1,text='Email',font=('Verdana',15,'bold'),bg='white',fg='#0373fc').place(x=25,y=65)
        self.txtLoginEmail = Entry(frame1,font=('Verdana',15,'bold'))
        self.lblLoginPassword = Label(frame1,text='Password',font=('Verdana',15,'bold'),bg='white',fg='#0373fc').place(x=25,y=145)
        self.txtLoginPassword = Entry(frame1,font=('Verdana',15,'bold'))
        self.btnLogin = Button(frame1,text='Login',font=('Verdana',15,'bold'),bg='#0373fc',fg='white',command=self.login).place(x=25,y=240)
        self.txtLoginEmail.place(x=25,y=105)
        self.txtLoginPassword.place(x=25,y=185)
    
    def login(self):
        db = Database()
        print(self.txtLoginEmail.get())
        login_status,user_data = db.checkLogin(self.txtLoginEmail.get(),self.txtLoginPassword.get())
        print(login_status)
        if(login_status):
            self.root.destroy()
            from dashboard import Dashboard
            dashboardwindow=Tk()
            obj = Dashboard(dashboardwindow,user_data)
            root.mainloop()
        
        # try:
        #     if(db.checkLogin(self.txtLoginEmail.get(),self.txtLoginPassword.get())):
        #         self.root.destroy()
        #         from dashboard import dataTransfer
        #         dataTransfer(self.txtLoginEmail.get())
        # except:
        #     print('Something Occured')
        

    def clear(self):
        self.txtRemarks.delete(0,END)
        # self.root.destroy()
        # import register

root=Tk()

obj = Login(root)
root.mainloop()