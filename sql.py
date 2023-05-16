import mysql.connector

class Database:
    __host__ = 'localhost'
    __username__ = 'JV'
    __password__ = 'Jayavighnesh'
    __database__ = 'storemanagement'
    def __init__(self):
        pass
        


    def createEmployee(self):
        mydb = mysql.connector.connect(
            host=self.__host__,
            user=self.__username__,
            password=self.__password__,
            database=self.__database__,
            )
        mycursor = mydb.cursor()
        sql = "INSERT INTO employee (emp_firstname,emp_lastname,emp_email,emp_password,emp_phonenumber,emp_doornum,emp_street,emp_area,emp_city,emp_photo,emp_role,emp_grade,emp_dateofbirth,emp_incomefromemp,emp_salary,emp_remarks,emp_createdAt,emp_updatedAt) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d, %s, %d, %d, %s)"
        val = ("Jayavighnesh", "B K","bkjv2006@gmail.com","Jay",'9344272929','105','Pillayar Koil Street','Ammapet Main Road','Salem','image','Owner',3,'01/01/2006',0,100000,'I am Owner da !!')
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, 'Row Inserted Successfully')