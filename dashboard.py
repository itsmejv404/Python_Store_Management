from tkinter import *
from PIL import Image,ImageTk ##pip install pillow
from tkinter import filedialog
from tkinter import ttk
import shutil
from sql import Database
class Dashboard:
    def __init__(self,root,user_data):
        print("Dashboard : " + str(user_data))
        self.root = root
        self.root.title('Dashboard')
        self.root.wm_iconbitmap('images/icons.ico')
        self.root.geometry("1250x675+0+0")
        self.root.maxsize(1250,675)
        self.root.minsize(1250,675)
        # self.bg = ImageTk.PhotoImage(file='138728.jpg')
        # bg = Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        # self.left = ImageTk.PhotoImage(file='images/sideimage.png')
        # left=Label(self.root,image=self.left).place(x = 80,y = 100,width=400,height=500)
        frame1=Frame(self.root,bg='#274C77')
        frame1.place(x=0,y = 0,width=450,height=675)

        self.image_label = Label(frame1,bg='#274C77')
        # self.image_label = Label(frame1,bg='white')
        self.image_label.place(x=75,y=70,width=300,height=400)
        image = Image.open(user_data[14])
        image.thumbnail((300, 400))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        self.lblDashboardName = Label(frame1,text=user_data[1]+" "+user_data[2],justify=CENTER,bg='#274C77',fg='white',font=('Verdana',20,'bold')).place(x=0,y=450,width=450)
        self.lblDashboardRole = Label(frame1,text=user_data[15],justify=CENTER,bg='#274C77',fg='white',font=('Verdana',10,'bold')).place(x=0,y=500,width=450)
        btnDashboardLogout = Button(frame1,text='Log Out',justify=CENTER,bg='#dcedff',fg='#274C77',command=self.Logout,font=('Verdana',15,'bold')).place(x=25,y=580,width=400)
        ## Store Proprietor
        if(user_data[16] == 0):
            name = user_data[1]+user_data[2]
            storeProprietorFrame=Frame(self.root,bg='#dcedff')
            storeProprietorFrame.place(x=450,y = 0,width=800,height=675)
            createNewProfile = Button(storeProprietorFrame,text='Create new employee profile',command=self.createNewProfileFunc).place(x = 0,y = 0)
        elif(user_data[16] == 1):
            ## Store Manager
            storeManagerFrame=Frame(self.root,bg='#dcedff')
            storeManagerFrame.place(x=450,y = 0,width=800,height=675)
            createNewProfile = Button(storeManagerFrame,text='Create new employee profile').place(x = 0,y = 0)
        elif(user_data[16] == 2):
            ## Store Assistant Store Manager
            storeAssistantStoreManagerFrame=Frame(self.root,bg='#dcedff')
            storeAssistantStoreManagerFrame.place(x=450,y = 0,width=800,height=675)
            stockAndInventory = Button(storeAssistantStoreManagerFrame,text='Stock and Inventory Management').place(x = 0,y = 0)
        elif(user_data[16] == 3):
            ## Store Financial Manager
            storeFinancialManagerFrame=Frame(self.root,bg='#dcedff')
            storeFinancialManagerFrame.place(x=450,y = 0,width=800,height=675)
            financialStatus = Button(storeFinancialManagerFrame,text='Financial Status').place(x = 0,y = 0)
        elif(user_data[16] == 4):
            ## Store Procurement Manager
            storeProcurementManagerFrame=Frame(self.root,bg='#dcedff')
            storeProcurementManagerFrame.place(x=450,y = 0,width=800,height=675)
            stockAndInventory = Button(storeProcurementManagerFrame,text='Stock and Inventory Management').place(x = 0,y = 0)
        elif(user_data[16] == 5):
            ## Store Department Sales Man
            storeDepartmentSalesManFrame=Frame(self.root,bg='#dcedff')
            storeDepartmentSalesManFrame.place(x=450,y = 0,width=800,height=675)
            departmentInventory = Button(storeDepartmentSalesManFrame,text='Department Inventory').place(x = 0,y = 0)
        elif(user_data[16] == 6):
            ## Store Cashier
            storeCashierFrame=Frame(self.root,bg='#dcedff')
            storeCashierFrame.place(x=450,y = 0,width=800,height=675)
            billingApplication = Button(storeCashierFrame,text='Billing Application').place(x = 0,y = 0)
        elif(user_data[16] == 7):
            ## Store Janitor
            storeJanitorFrame=Frame(self.root,bg='#dcedff')
            storeJanitorFrame.place(x=450,y = 0,width=800,height=675)
            checkProfileStatus = Button(storeJanitorFrame,text='Check Proflie Information').place(x = 0,y = 0)

    def createNewProfileFunc(self):
        from register import startWindow
        startWindow()
    def clear(self):
        self.txtRemarks.delete(0,END)
        # self.root.destroy()
        # import register

    def Logout(self):
        self.root.destroy()


