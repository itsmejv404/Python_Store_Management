import mysql.connector

class Database:
    __host__ = 'localhost'
    __username__ = 'JV'
    __password__ = 'Jayavighnesh'
    __database__ = 'storemanagement'
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=self.__host__,
            user=self.__username__,
            password=self.__password__,
            database=self.__database__,
            )
    def createEmployee(self,firstname,lastname,email,password,phonenumber,doornum,street,area,city,photo,role,grade,dateofbirth,incomefromemp,salary,remarks):
        self.mycursor = self.mydb.cursor()
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phonenumber = phonenumber
        self.doornum = doornum
        self.street = street
        self.area = area
        self.city = city
        self.photo = photo
        self.role = role
        self.grade = grade
        self.dateofbirth = dateofbirth
        self.incomefromemp = incomefromemp
        self.salary = salary
        self.remarks = remarks
        sql = "INSERT INTO employee (emp_firstname,emp_lastname,emp_email,emp_password,emp_phonenumber,emp_doornum,emp_street,emp_area,emp_city,emp_photo,emp_role,emp_grade,emp_dateofbirth,emp_incomefromemp,emp_salary,emp_remarks) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (self.firstname,self.lastname,self.email,self.password,self.phonenumber,self.doornum,self.street,self.area,self.city,self.photo,self.role,self.grade,self.dateofbirth,self.incomefromemp,self.salary,remarks)
        self.mycursor.execute(sql, val)

        self.mydb.commit()

        print(self.mycursor.rowcount, "record inserted.")