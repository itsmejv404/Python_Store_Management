import mysql.connector

class Database:
    __host__ = 'localhost'
    __username__ = 'root'
    __password__ = ''
    __database__ = 'pystoremanagement'
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=self.__host__,
            user=self.__username__,
            password=self.__password__,
            database=self.__database__,
            )
    def checkLogin(self,email,password):
        self.emp_email = email
        self.emp_password = password
        self.mycursor = self.mydb.cursor()
        sql = "SELECT * FROM employees WHERE email = %s"
        adr = (self.emp_email,)
        self.mycursor.execute(sql, adr)
        myresult = self.mycursor.fetchall()
        print(myresult[0][6])
        if self.emp_password == myresult[0][6]:
            return True,myresult[0]
        else:
            return False,0
    def retriveEmployeeData(self):
        self.mycursor = self.mydb.cursor()
        sql = "SELECT * FROM employees"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        print(myresult[0])
        return myresult
    def createEmployee(self,txtFirstName,txtLastName,txtAge,txtGender,txtEmail,txtPassword,txtPhoneNumber,txtDateOfBirth,txtDoorNum,txtStreet,txtArea,txtCity,txtState,file_path,txtRole,txtGrade,txtSalary,txtDateOfJoining,txtRemarks):
        self.mycursor = self.mydb.cursor()
        self.txtFirstName = txtFirstName
        self.txtLastName = txtLastName
        self.txtAge = txtAge
        self.txtGender = txtGender
        self.txtEmail = txtEmail
        self.txtPassword = txtPassword
        self.txtPhoneNumber = txtPhoneNumber
        self.txtDateOfBirth = txtDateOfBirth
        self.txtDoorNum = txtDoorNum
        self.txtStreet = txtStreet
        self.txtArea = txtArea
        self.txtCity = txtCity
        self.txtState = txtState
        self.file_path = file_path
        self.txtRole = txtRole
        self.txtGrade = int(txtGrade)
        self.txtSalary = int(txtSalary)
        self.txtDateOfJoining = txtDateOfJoining
        self.txtRemarks = txtRemarks
        sql = "INSERT INTO employees (firstname,lastname,age,gender,email,password,phonenumber,dateofbirth,doornum,street,area,city,state,photourl,role,grade,salary,dateofjoining,remarks) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (self.txtFirstName,self.txtLastName,self.txtAge,self.txtGender,self.txtEmail,self.txtPassword,self.txtPhoneNumber,self.txtDateOfBirth,self.txtDoorNum,self.txtStreet,self.txtArea,self.txtCity,self.txtState,self.file_path,self.txtRole,self.txtGrade,self.txtSalary,self.txtDateOfJoining,self.txtRemarks)
        self.mycursor.execute(sql, val)

        self.mydb.commit()

        print(self.mycursor.rowcount, "record inserted.")
    def updateEmployee(self,txtFirstName,txtLastName,txtAge,txtGender,txtEmail,txtPassword,txtPhoneNumber,txtDateOfBirth,txtDoorNum,txtStreet,txtArea,txtCity,txtState,txtRole,txtGrade,txtSalary,txtDateOfJoining,txtRemarks,id,photo = ''):
        self.mycursor = self.mydb.cursor()
        self.txtFirstName = txtFirstName
        self.txtLastName = txtLastName
        self.txtAge = txtAge
        self.txtGender = txtGender
        self.txtEmail = txtEmail
        self.txtPassword = txtPassword
        self.txtPhoneNumber = txtPhoneNumber
        self.txtDateOfBirth = txtDateOfBirth
        self.txtDoorNum = txtDoorNum
        self.txtStreet = txtStreet
        self.txtArea = txtArea
        self.txtCity = txtCity
        self.txtState = txtState
        # self.file_path = file_path
        self.txtRole = txtRole
        self.txtGrade = int(txtGrade)
        self.txtSalary = int(txtSalary)
        self.txtDateOfJoining = txtDateOfJoining
        self.txtRemarks = txtRemarks
        # sql = "UPDATE employees firstname = %s,lastname = %s,age = %s,gender = %s,email = %s,password = %s,phonenumber = %s,dateofbirth = %s,doornum = %s,street = %s,area, = %scity = %s,state = %s,role = %s,grade = %s,salary = %s,dateofjoining = %s,remarks = %s WHERE id = %s;"
        # val = (self.txtFirstName,self.txtLastName,self.txtAge,self.txtGender,self.txtEmail,self.txtPassword,self.txtPhoneNumber,self.txtDateOfBirth,self.txtDoorNum,self.txtStreet,self.txtArea,self.txtCity,self.txtState,self.txtRole,self.txtGrade,self.txtSalary,self.txtDateOfJoining,self.txtRemarks,id)
        # sql = "UPDATE employees firstname = 'Check' WHERE id = "+ str(id) + ";"
        # val = (self.txtFirstName,id)
        # self.mycursor.execute(sql, val)
        # self.mycursor.execute(sql)

        # update_query = "UPDATE employees SET firstname = %s,lastname = %s,age = %s,gender = %s,email = %s,password = %s,phonenumber = %s,doornum = %s,street = %s,area = %s,state = %s,role = %s,grade = %s,salary = %s,dateofjoining = %s,remarks = %s WHERE id = %s;"
        # self.mycursor.execute(update_query, (self.txtFirstName,self.txtLastName,self.txtAge,self.txtGender,self.txtEmail,self.txtPassword,self.txtPhoneNumber,self.txtDoorNum,self.txtStreet,self.txtArea,self.txtState,self.txtRole,self.txtGrade,self.txtSalary,self.txtDateOfJoining,self.txtRemarks,id))
        update_query = "UPDATE employees SET firstname = %s,lastname = %s,age = %s,gender = %s,email = %s,password = %s,phonenumber = %s,doornum = %s,street = %s,area = %s,state = %s,role = %s,grade = %s,salary = %s,dateofjoining = %s,remarks = %s,photourl = %s WHERE id = %s;"
        self.mycursor.execute(update_query, (self.txtFirstName,self.txtLastName,self.txtAge,self.txtGender,self.txtEmail,self.txtPassword,self.txtPhoneNumber,self.txtDoorNum,self.txtStreet,self.txtArea,self.txtState,self.txtRole,self.txtGrade,self.txtSalary,self.txtDateOfJoining,self.txtRemarks,photo,id))

        self.mydb.commit()
    def deleteEmployee(self,deleteID):
        print(deleteID)
        self.mycursor = self.mydb.cursor()
        sql = "DELETE FROM employees WHERE id = " + str(deleteID)
        # val = (8,)
        
        self.mycursor.execute(sql)

        self.mydb.commit()

        print(self.mycursor.rowcount, "record inserted.")

    def retriveItemData(self):
        self.mycursor = self.mydb.cursor()
        sql = "SELECT * FROM inventory"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        print(myresult[0])
        return myresult
    def createItem(self,txtItemName,txtItemQuantity,txtPerItemPrice,txtPerItemProfit,txtTotalItemPrice,txtTotalItemProfit,txtItemCategory):
        self.mycursor = self.mydb.cursor()
        self.txtItemName = txtItemName
        self.txtItemQuantity = int(txtItemQuantity)
        self.txtPerItemPrice = int(txtPerItemPrice)
        self.txtPerItemProfit = int(txtPerItemProfit)
        self.txtTotalItemPrice = int(txtTotalItemPrice)
        self.txtTotalItemProfit = int(txtTotalItemProfit)
        self.txtItemCategory = txtItemCategory
        sql = "INSERT INTO inventory (category_name,item_name,item_quantity,per_item_price,per_item_profit,total_item_price,total_item_profit) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (self.txtItemCategory,self.txtItemName,self.txtItemQuantity,self.txtPerItemPrice,self.txtPerItemProfit,self.txtTotalItemPrice,self.txtTotalItemProfit)
        self.mycursor.execute(sql, val)

        self.mydb.commit()

        print(self.mycursor.rowcount, "Items inserted.")
    def updateItem(self,txtItemName,txtItemQuantity,txtPerItemPrice,txtPerItemProfit,txtTotalItemPrice,txtTotalItemProfit,txtItemCategory,id):
        self.mycursor = self.mydb.cursor()
        self.txtItemName = txtItemName
        self.txtItemQuantity = int(txtItemQuantity)
        self.txtPerItemPrice = int(txtPerItemPrice)
        self.txtPerItemProfit = int(txtPerItemProfit)
        self.txtTotalItemPrice = int(txtTotalItemPrice)
        self.txtTotalItemProfit = int(txtTotalItemProfit)
        self.txtItemCategory = txtItemCategory
        update_query = "UPDATE inventory SET category_name = %s,item_name = %s,item_quantity = %s,per_item_price = %s,per_item_profit = %s,total_item_price = %s,total_item_profit = %s WHERE id = %s;"
        self.mycursor.execute(update_query, (self.txtItemCategory,self.txtItemName,self.txtItemQuantity,self.txtPerItemPrice,self.txtPerItemProfit,self.txtTotalItemPrice,self.txtTotalItemProfit,id))

        self.mydb.commit()
    def deleteItem(self,deleteID):
        print(deleteID)
        self.mycursor = self.mydb.cursor()
        sql = "DELETE FROM inventory WHERE id = " + str(deleteID)
        # val = (8,)
        
        self.mycursor.execute(sql)

        self.mydb.commit()

        print(self.mycursor.rowcount, "Item Deleted.")