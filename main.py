import mysql.connector

from tkinter import *
master = Tk()
master.geometry("50x0")
master.title("User Login")

from sql import Database
# db = Database()
# firstname = 'Jayavighnesh'
# lastname = 'B K'
# email = 'bkjv2006@gmail.com'
# password = 'Jayavighnesh'
# phonenumber = '9344272929'
# doornum = '105'
# street = 'Pillayar Koil Street'
# area = 'Ammapet Main Road'
# city = 'Salem'
# photo = 'image'
# role = 'Owner'
# grade = 3
# dateofbirth = '01/01/2006'
# incomefromemp = 1000
# salary = 100000
# remarks = 'I am Owner da!!'

# db.createEmployee(firstname,lastname,email,password,phonenumber,doornum,street,area,city,photo,role,grade,dateofbirth,incomefromemp,salary,remarks)

def LoginScreen():
    parent = Toplevel(master)
    name = Label(parent,text = "Name").grid(row = 0, column = 0)  
    e1 = Entry(parent).grid(row = 0, column = 1)  
    password = Label(parent,text = "Password").grid(row = 1, column = 0)  
    e2 = Entry(parent).grid(row = 1, column = 1)  
    value1,value2 = e1.get(),e2.get()
    button = Tk.Button(master=frame, text='press', command= lambda: loginCheck(1,1)).grid(row = 4, column = 0)  
    
def loginCheck(a,b):
    print(a,b)

LoginScreen();
master.mainloop()
