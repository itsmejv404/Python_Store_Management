from tkinter import *
from PIL import Image,ImageTk ##pip install pillow
from tkinter import filedialog
from tkinter import ttk
import shutil
from sql import Database
import tkinter as tk
class LoginScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.wm_iconbitmap('images/icons.ico')
        self.geometry("1250x675+0+0")
        self.maxsize(1250,675)
        self.minsize(1250,675)
        self.bg = ImageTk.PhotoImage(file='138728.jpg')
        bg = Label(self,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        self.left = ImageTk.PhotoImage(file='images/sideimage.png')
        left=Label(self,image=self.left).place(x = 80,y = 100,width=400,height=500)

        frame1=Frame(self,bg='white')
        frame1.place(x=480,y = 100,width=700,height=500)
        emailStringVar = StringVar()
        passwordStringVar = StringVar()
        emailStringVar.set('tao@gmail.com')
        passwordStringVar.set('Tao')
        self.lblLoginHead = Label(frame1,text='LOGIN',font=('Verdana',25,'bold'),bg='white',fg='#0373fc').place(x=25,y=25)
        self.lblLoginEmail = Label(frame1,text='Email',font=('Verdana',15,'bold'),bg='white',fg='#0373fc').place(x=25,y=65)
        self.txtLoginEmail = Entry(frame1,font=('Verdana',15,'bold'),textvariable=emailStringVar)
        self.lblLoginPassword = Label(frame1,text='Password',font=('Verdana',15,'bold'),bg='white',fg='#0373fc').place(x=25,y=145)
        self.txtLoginPassword = Entry(frame1,font=('Verdana',15,'bold'),textvariable=passwordStringVar)
        self.btnLogin = Button(frame1,text='Login',font=('Verdana',15,'bold'),bg='#0373fc',fg='white',command=self.login).place(x=25,y=240)
        self.txtLoginEmail.place(x=25,y=105)
        self.txtLoginPassword.place(x=25,y=185)
    def login(self):
        db = Database()
        print(self.txtLoginEmail.get())
        login_status,user_data = db.checkLogin(self.txtLoginEmail.get(),self.txtLoginPassword.get())
        print(login_status)
        if(login_status):
            self.openDashboardWindow(user_data)
    def openDashboardWindow(self,user_data):
        self.withdraw()
        self.dashboard_window = Dashboard(self,user_data)
        self.dashboard_window.protocol("WM_DELETE_WINDOW", self.closeDashboardWindow)

    def closeDashboardWindow(self):
        self.dashboard_window.destroy()
        self.destroy()
        # self.destroy()
        # self.deiconify()
class Dashboard(tk.Toplevel,):
    def __init__(self, root,user_data):
        super().__init__(root)
        print(user_data)
        self.title('Dashboard')
        self.wm_iconbitmap('images/icons.ico')
        self.geometry("1250x675+0+0")
        self.maxsize(1250,675)
        self.minsize(1250,675)
        frame1=Frame(self,bg='#274C77')
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
        btnDashboardLogout = Button(frame1,text='Log Out',justify=CENTER,bg='#dcedff',fg='#274C77',command=self.logout,font=('Verdana',15,'bold')).place(x=25,y=580,width=400)
        ## Store Proprietor
        if(user_data[16] == 0):
            name = user_data[1]+user_data[2]
            storeProprietorFrame=Frame(self,bg='#dcedff')
            storeProprietorFrame.place(x=450,y = 0,width=800,height=675)
            createNewProfile = Button(storeProprietorFrame,text='Add / Manage Employee',command=self.openAddNewProfileWindow).place(x = 0,y = 0)
        elif(user_data[16] == 1):
            ## Store Manager
            storeManagerFrame=Frame(self,bg='#dcedff')
            storeManagerFrame.place(x=450,y = 0,width=800,height=675)
            createNewProfile = Button(storeManagerFrame,text='Create new employee profile').place(x = 0,y = 0)
        elif(user_data[16] == 2):
            ## Store Assistant Store Manager
            storeAssistantStoreManagerFrame=Frame(self,bg='#dcedff')
            storeAssistantStoreManagerFrame.place(x=450,y = 0,width=800,height=675)
            stockAndInventory = Button(storeAssistantStoreManagerFrame,text='Stock and Inventory Management').place(x = 0,y = 0)
        elif(user_data[16] == 3):
            ## Store Financial Manager
            storeFinancialManagerFrame=Frame(self,bg='#dcedff')
            storeFinancialManagerFrame.place(x=450,y = 0,width=800,height=675)
            financialStatus = Button(storeFinancialManagerFrame,text='Financial Status').place(x = 0,y = 0)
        elif(user_data[16] == 4):
            ## Store Procurement Manager
            storeProcurementManagerFrame=Frame(self,bg='#dcedff')
            storeProcurementManagerFrame.place(x=450,y = 0,width=800,height=675)
            stockAndInventory = Button(storeProcurementManagerFrame,text='Stock and Inventory Management').place(x = 0,y = 0)
        elif(user_data[16] == 5):
            ## Store Department Sales Man
            storeDepartmentSalesManFrame=Frame(self,bg='#dcedff')
            storeDepartmentSalesManFrame.place(x=450,y = 0,width=800,height=675)
            departmentInventory = Button(storeDepartmentSalesManFrame,text='Department Inventory').place(x = 0,y = 0)
        elif(user_data[16] == 6):
            ## Store Cashier
            storeCashierFrame=Frame(self,bg='#dcedff')
            storeCashierFrame.place(x=450,y = 0,width=800,height=675)
            billingApplication = Button(storeCashierFrame,text='Billing Application').place(x = 0,y = 0)
        elif(user_data[16] == 7):
            ## Store Janitor
            storeJanitorFrame=Frame(self,bg='#dcedff')
            storeJanitorFrame.place(x=450,y = 0,width=800,height=675)
            checkProfileStatus = Button(storeJanitorFrame,text='Check Proflie Information').place(x = 0,y = 0)
    def openAddNewProfileWindow(self):
        self.withdraw()
        self.newProfile = AddNewProfile(self)
        self.newProfile.protocol("WM_DELETE_WINDOW", self.closeAddNewProfileWindow)
    def closeAddNewProfileWindow(self):
        self.newProfile.withdraw()
        self.deiconify()
        # self.master.deiconify()
    def logout(self):
        self.master.destroy()
class AddNewProfile(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title('Create a new profile')
        self.wm_iconbitmap('images/icons.ico')
        self.geometry("1280x720+0+0")
        self.maxsize(1280,720)
        self.minsize(1280,720)
        # self.bg = ImageTk.PhotoImage(file='138728.jpg')
        # bg = Label(self,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        # self.left = ImageTk.PhotoImage(file='images/sideimage.png')
        # left=Label(self,image=self.left).place(x = 80,y = 100,width=400,height=500)

        frame1=Frame(self,bg='white')
        frame1.place(x=0,y = 0,width=1280,height=720)
        # frame1.photofilename = filedialog.askopenfilename(initialdir='',title="Select a Photo",filetypes=(("JPG Files","*.png"),('all files','*.*')))
        # photonamepath = frame1.photofilename
        # print(photonamepath)
       
        # self.imgPhoto = ImageTk.PhotoImage(Image.open(photonamepath))
        # lblimgPhoto = Label(frame1,image=self.imgPhoto).place(x=400,y=0,width=200,height=0)
        title = Label(frame1,text='Create new Profile',font=("Verdana",20,"bold"),bg="white",fg='#0373fc').place(x=50,y=30)
        lblFirstName = Label(frame1,text='First Name :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=50,y=80)
        lblLastName = Label(frame1,text='Last Name :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=50,y=110)
        lblAge = Label(frame1,text='Age :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=50,y=140)
        lblGender = Label(frame1,text='Gender :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=50,y=170)
        lblEmail = Label(frame1,text='Email :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=50,y=200)
        lblPassword = Label(frame1,text='Password :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=50,y=230)
        lblPhoneNumber = Label(frame1,text='Phone Number :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=50,y=260)
        lblDateOfBirth = Label(frame1,text='Date of Birth :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=50,y=290)


        lblDoorNum = Label(frame1,text='Door No :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=380,y=80)
        lblStreet = Label(frame1,text='Street :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=380,y=110)
        lblArea = Label(frame1,text='Area :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=380,y=140)
        lblCity = Label(frame1,text='City :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=380,y=170)
        lblState = Label(frame1,text='State :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=380,y=200)
        lblRole = Label(frame1,text='Role :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=380,y=230)
        lblGrade = Label(frame1,text='Grade :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=380,y=260)
        lblSalary = Label(frame1,text='Salary :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=380,y=290)


        lblSelectPhoto = Label(frame1,text='Select Photo :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=700,y=230)
        btnChoosePhoto = Button(frame1,text='Choose Photo',width=20,font=("Verdana",10,"bold"),command=self.pick_image,fg='white',bg='#0373fc').place(x=870,y=230)
        lblDateOfJoining = Label(frame1,text='Date of Joining :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=700,y=260)
        lblRemarks = Label(frame1,text='Remarks :',font=("Verdana",10,"bold"),bg="white",fg='#0373fc').place(x=700,y=290)
        btnClear = Button(frame1,text='Clear',border=0,font=("Verdana",10,"bold"),height=1,width=25, bg='#0373fc',fg='white',command=self.clear,state=NORMAL).place(x=130,y=350)
        btnCreate = Button(frame1,text='Create',border=0,font=("Verdana",10,"bold"),width=25, bg='#0373fc',fg='white',command=self.createEmployee).place(x=380,y=350)
        btnUpdate = Button(frame1,text='Update',border=0,font=("Verdana",10,"bold"),width=25, bg='#0373fc',fg='white',command=self.createEmployee).place(x=630,y=350)
        btnDelete = Button(frame1,text='Delete',border=0,font=("Verdana",10,"bold"),width=25, bg='#0373fc',fg='white',command=self.deleteEmployee).place(x=880,y=350)
        # image=Image.open('images/create.png')
        # img=image.resize((450, 350))
        # my_img=ImageTk.PhotoImage(img)
        # self.roundedbutton = Button(frame1, image=my_img,height=20,width=250).place(x=380,y=470)
        self.firstNameStringVar = StringVar()
        self.lastNameStringVar = StringVar()
        self.ageStringVar = StringVar()
        self.genderStringVar = StringVar()
        self.emailStringVar = StringVar()
        self.passwordStringVar = StringVar()
        self.phoneNumberStringVar = StringVar()
        self.dateOfBirthStringVar = StringVar()
        self.doorNumStringVar = StringVar()
        self.streetStringVar = StringVar()
        self.areaStringVar = StringVar()
        self.cityStringVar = StringVar()
        self.stateStringVar = StringVar()
        self.roleStringVar = StringVar()
        self.gradeStringVar = StringVar()
        self.salaryStringVar = StringVar()
        self.dateOfJoiningStringVar = StringVar()
        self.remarksStringVar = StringVar()
        self.txtFirstName = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.firstNameStringVar)
        self.txtLastName = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.lastNameStringVar)
        self.txtAge = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.ageStringVar)
        self.txtGender = ttk.Combobox(frame1, width = 27, textvariable = self.genderStringVar)
        self.txtGender['values'] = (' Male', 
                          ' Female')
        self.txtEmail = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.emailStringVar)
        self.txtPassword = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.passwordStringVar)
        self.txtPhoneNumber = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.phoneNumberStringVar)
        self.txtDateOfBirth = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.dateOfBirthStringVar)
        self.txtDoorNum = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.doorNumStringVar)
        self.txtStreet = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.streetStringVar)
        self.txtArea = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.areaStringVar)
        self.txtCity = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.cityStringVar)
        self.txtState = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.stateStringVar)
        # self.txtRole = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        self.txtRole = ttk.Combobox(frame1, width = 27, textvariable = self.roleStringVar)
        roles = ('Store Proprietor','Store Manager','Store Assistant Manager','Financial Manager','Procurement Manager','Department Sales Man','Cashiers','Janitor')
        self.txtRole['values'] = roles
        self.txtRole.bind("<<ComboboxSelected>>", self.on_combobox_change)
        self.txtGrade = Entry(frame1,textvariable=self.gradeStringVar,font=("Verdana",10,"bold"),bg="white",fg='black',state=DISABLED)
        self.txtSalary = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.salaryStringVar)
        self.txtDateOfJoining = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.dateOfJoiningStringVar)
        self.txtRemarks = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black',textvariable=self.remarksStringVar)

        columns = ('ID','Name','Gender','Date of Birth','Role','Salary')
        self.records_treeview = ttk.Treeview(frame1, columns=columns, show="headings")
        for col in columns:
            self.records_treeview.heading(col, text=col,anchor=W)
        self.records_treeview.pack()

        # Insert sample data
        lstDB = Database()
        self.result = lstDB.retriveEmployeeData()
        # print(result)
        for i in range(len(self.result)):
            self.records_treeview.insert("", "end", values=(self.result[i][0],self.result[i][1] + self.result[i][2],self.result[i][4],self.result[i][8],self.result[i][15],self.result[i][17]))
        # self.records_treeview.insert("", "end", values=(1, "John Doe", 25))
        # Bind the selection event to the Treeview
        self.records_treeview.bind("<<TreeviewSelect>>", self.on_select)
        # records_treeview.config(width=199,height=199)
        self.records_treeview.place(x=50,y=400,width=1200,height=300)
        self.txtFirstName.place(x=170,y=80) 
        self.txtLastName.place(x=170,y=110)
        self.txtAge.place(x=170,y=140)
        self.txtGender.place(x=170,y=170)
        self.txtEmail.place(x=170,y=200)
        self.txtPassword.place(x=170,y=230)
        self.txtPhoneNumber.place(x=170,y=260)
        self.txtDateOfBirth.place(x=170,y=290)


        self.txtDoorNum.place(x=500,y=80)
        self.txtStreet.place(x=500,y=110)
        self.txtArea.place(x=500,y=140)
        self.txtCity.place(x=500,y=170)
        self.txtState.place(x=500,y=200)
        self.txtRole.place(x=500,y=230)
        self.txtGrade.place(x=500,y=260)
        self.txtSalary.place(x=500,y=290)


        self.txtDateOfJoining.place(x=870,y=260)
        self.txtRemarks.place(x=870,y=290)
        self.image_label = Label(frame1)
        self.image_label.place(x=870,y=30,width=150,height=180)
    def on_select(self,event):
            
            selected_item = self.records_treeview.selection()
            if selected_item:
                values = self.records_treeview.item(selected_item)['values']
                print('Menu Selected')
                print(values)
                self.selectedDataset = ''
                for i in self.result:
                    if values[0] == i[0]:
                        self.selectedDataset = i
                        
                        print('Yep')
                    # else:
                        # print('Sup')
                self.firstNameStringVar.set(self.selectedDataset[1])
                self.lastNameStringVar.set(self.selectedDataset[2])
                self.ageStringVar.set(self.selectedDataset[3])
                self.genderStringVar.set(self.selectedDataset[4])
                self.emailStringVar.set(self.selectedDataset[5])
                self.passwordStringVar.set(self.selectedDataset[6])
                self.phoneNumberStringVar.set(self.selectedDataset[7])
                self.dateOfBirthStringVar.set(self.selectedDataset[8])
                self.doorNumStringVar.set(self.selectedDataset[9])
                self.streetStringVar.set(self.selectedDataset[10])
                self.areaStringVar.set(self.selectedDataset[11])
                self.cityStringVar.set(self.selectedDataset[12])
                self.stateStringVar.set(self.selectedDataset[13])
                image = Image.open(self.selectedDataset[14])
                image.thumbnail((400, 200))
                photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=photo)
                self.image_label.image = photo
                # self.photoStringVar.set(self.selectedDataset[1])
                self.roleStringVar.set(self.selectedDataset[15])
                self.gradeStringVar.set(self.selectedDataset[16])
                self.salaryStringVar.set(self.selectedDataset[17])
                self.dateOfJoiningStringVar.set(self.selectedDataset[18])
                self.remarksStringVar.set(self.selectedDataset[19])
    def on_combobox_change(self,event):
        print('Management Roles Modified')
        selected_role = self.txtRole.get()
        roles = ('Store Proprietor','Store Manager','Store Assistant Manager','Financial Manager','Procurement Manager','Department Sales Man','Cashiers','Janitor')
        grades = (0,1,2,3,4,5,6,7)
        self.gradeStringVar.set(roles.index(selected_role))
    def pick_image(self):
        self.file_path = filedialog.askopenfilename(initialdir='',title="Select a Photo",filetypes=(("JPG Files","*.jpg"),("PNG Files","*.png"),('All Files','*.*')))
        image = Image.open(self.file_path)
        image.thumbnail((400, 200))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
    def clear(self):
        
        image = Image.open('images/nopictureselected.png')
        image.thumbnail((400, 200))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        self.txtFirstName.delete(0,END)
        self.txtLastName.delete(0,END)
        self.txtAge.delete(0,END)
        self.txtGender.delete(0,END)
        self.txtEmail.delete(0,END)
        self.txtPassword.delete(0,END)
        self.txtPhoneNumber.delete(0,END)
        self.txtDateOfBirth.delete(0,END)
        self.txtDoorNum.delete(0,END)
        self.txtStreet.delete(0,END)
        self.txtArea.delete(0,END)
        self.txtCity.delete(0,END)
        self.txtState.delete(0,END)
        self.txtRole.delete(0,END)
        self.txtGrade.delete(0,END)
        self.txtSalary.delete(0,END)
        self.txtDateOfJoining.delete(0,END)
        self.txtRemarks.delete(0,END)
        # self.root.destroy()
        # import register
    def createEmployee(self):
        src_path = self.file_path
        dst_path = r"D:/StoreManagement/pystoremanagement/employeeImages/" + self.txtPhoneNumber.get() + ".png"
        shutil.copy(src_path, dst_path)
        print('Copied')
        print(self.file_path)
        print(self.txtFirstName.get())
        print(self.txtLastName.get())
        print(self.txtAge.get())
        print(self.txtGender.get())
        print(self.txtEmail.get())
        print(self.txtPassword.get())
        print(self.txtPhoneNumber.get())
        print(self.txtDateOfBirth.get())
        print(self.txtDoorNum.get())
        print(self.txtStreet.get())
        print(self.txtArea.get())
        print(self.txtCity.get())
        print(self.txtState.get())
        print(self.txtRole.get())
        print(self.txtGrade.get())
        print(self.txtSalary.get())
        print(self.txtDateOfJoining.get())
        print(self.txtRemarks.get())
        db = Database()
        db.createEmployee(self.txtFirstName.get(),self.txtLastName.get(),self.txtAge.get(),self.txtGender.get(),self.txtEmail.get(),self.txtPassword.get(),self.txtPhoneNumber.get(),self.txtDateOfBirth.get(),self.txtDoorNum.get(),self.txtStreet.get(),self.txtArea.get(),self.txtCity.get(),self.txtState.get(),dst_path,self.txtRole.get(),self.txtGrade.get(),self.txtSalary.get(),self.txtDateOfJoining.get(),self.txtRemarks.get())
        image = Image.open('images/nopictureselected.png')
        image.thumbnail((400, 200))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        self.txtFirstName.delete(0,END)
        self.txtLastName.delete(0,END)
        self.txtAge.delete(0,END)
        self.txtGender.delete(0,END)
        self.txtEmail.delete(0,END)
        self.txtPassword.delete(0,END)
        self.txtPhoneNumber.delete(0,END)
        self.txtDateOfBirth.delete(0,END)
        self.txtDoorNum.delete(0,END)
        self.txtStreet.delete(0,END)
        self.txtArea.delete(0,END)
        self.txtCity.delete(0,END)
        self.txtState.delete(0,END)
        self.txtRole.delete(0,END)
        self.txtGrade.delete(0,END)
        self.txtSalary.delete(0,END)
        self.txtDateOfJoining.delete(0,END)
        self.txtRemarks.delete(0,END)
        self.close_window()
    def updateEmployee(self):
        src_path = self.file_path
        dst_path = r"D:/StoreManagement/pystoremanagement/employeeImages/" + self.txtPhoneNumber.get() + ".png"
        shutil.copy(src_path, dst_path)
        print('Copied')
        print(self.file_path)
        print(self.txtFirstName.get())
        print(self.txtLastName.get())
        print(self.txtAge.get())
        print(self.txtGender.get())
        print(self.txtEmail.get())
        print(self.txtPassword.get())
        print(self.txtPhoneNumber.get())
        print(self.txtDateOfBirth.get())
        print(self.txtDoorNum.get())
        print(self.txtStreet.get())
        print(self.txtArea.get())
        print(self.txtCity.get())
        print(self.txtState.get())
        print(self.txtRole.get())
        print(self.txtGrade.get())
        print(self.txtSalary.get())
        print(self.txtDateOfJoining.get())
        print(self.txtRemarks.get())
        db = Database()
        db.createEmployee(self.txtFirstName.get(),self.txtLastName.get(),self.txtAge.get(),self.txtGender.get(),self.txtEmail.get(),self.txtPassword.get(),self.txtPhoneNumber.get(),self.txtDateOfBirth.get(),self.txtDoorNum.get(),self.txtStreet.get(),self.txtArea.get(),self.txtCity.get(),self.txtState.get(),dst_path,self.txtRole.get(),self.txtGrade.get(),self.txtSalary.get(),self.txtDateOfJoining.get(),self.txtRemarks.get())
        image = Image.open('images/nopictureselected.png')
        image.thumbnail((400, 200))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        self.txtFirstName.delete(0,END)
        self.txtLastName.delete(0,END)
        self.txtAge.delete(0,END)
        self.txtGender.delete(0,END)
        self.txtEmail.delete(0,END)
        self.txtPassword.delete(0,END)
        self.txtPhoneNumber.delete(0,END)
        self.txtDateOfBirth.delete(0,END)
        self.txtDoorNum.delete(0,END)
        self.txtStreet.delete(0,END)
        self.txtArea.delete(0,END)
        self.txtCity.delete(0,END)
        self.txtState.delete(0,END)
        self.txtRole.delete(0,END)
        self.txtGrade.delete(0,END)
        self.txtSalary.delete(0,END)
        self.txtDateOfJoining.delete(0,END)
        self.txtRemarks.delete(0,END)
        self.close_window()
    def deleteEmployee(self):
        id = self.selectedDataset[0]
        db = Database()
        print(id)
        db.deleteEmployee(id)
        self.close_window()
    def close_window(self):
        self.destroy()
        self.master.deiconify()

# Create the main window
root = LoginScreen()
# temp_data = (6, 'Franlin', 'Clinton', '22', ' Male', 'franklin@gmail.com', 'Trevor', '1234567890', '01/01/2001', 'Door', 'Street', 'Area', 'Salem', 'Tamil nadu', 'D:/StoreManagement/pystoremanagement/employeeImages/1234567890.png', 'Store Proprietor', 0, 123456, '01/01/2005', 'Waste of Time')
# root = Dashboard(self,temp_data)
# Start the main event loop
root.mainloop()
