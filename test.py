# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="JV",
#   password="Jayavighnesh",
#   database="storemanagement"
# )

# mycursor = mydb.cursor()

sql = "INSERT INTO employee (emp_firstname,emp_lastname,emp_email,emp_password,emp_phonenumber,emp_doornum,emp_street,emp_area,emp_city,emp_photo,emp_role,emp_grade,emp_dateofbirth,emp_incomefromemp,emp_salary,emp_remarks,emp_createdAt,emp_updatedAt) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d, %s, %d, %d, %s)"
val = ("Jayavighnesh", "B K","bkjv2006@gmail.com","Jay",'9344272929','105','Pillayar Koil Street','Ammapet Main Road','Salem','image','Owner',3,'01/01/2006',0,100000,'I am Owner da !!')
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="JV",
  password="Jayavighnesh",
  database="storemanagement"
)

# mycursor = mydb.cursor()
# # sql = "INSERT INTO employee (emp_firstname,emp_lastname,emp_email,emp_password,emp_phonenumber,emp_doornum,emp_street,emp_area,emp_city,emp_photo,emp_role,emp_grade,emp_dateofbirth,emp_incomefromemp,emp_salary,emp_remarks,emp_createdAt,emp_updatedAt) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d, %s, %d, %d, %s)"
# val = ("Jayavighnesh", "B K","bkjv2006@gmail.com","Jay",'9344272929','105','Pillayar Koil Street','Ammapet Main Road','Salem','image','Owner',3,'01/01/2006',0,100000,'I am Owner da !!')
# mycursor.execute("INSERT INTO employee (emp_firstname,emp_lastname,emp_email,emp_password,emp_phonenumber,emp_doornum,emp_street,emp_area,emp_city,emp_photo,emp_role,emp_grade,emp_dateofbirth,emp_incomefromemp,emp_salary,emp_remarks,emp_createdAt,emp_updatedAt) VALUES ('Jayavighnesh', 'B K','bkjv2006@gmail.com','Jay','9344272929','105','Pillayar Koil Street','Ammapet Main Road','Salem','image','Owner',3,'01/01/2006',0,100000,'I am Owner da !!')")

mycursor = mydb.cursor()
firstname = 'Jayavighnesh'
lastname = 'B K'
email = 'bkjv2006@gmail.com'
password = 'Jayavighnesh'
phonenumber = '9344272929'
doornum = '105'
street = 'Pillayar Koil Street'
area = 'Ammapet Main Road'
city = 'Salem'
photo = 'image'
role = 'Owner'
grade = 3
dateofbirth = '01/01/2006'
incomefromemp = 1000
salary = 100000
remarks = 'I am Owner da!!'

sql = "INSERT INTO employee (emp_firstname,emp_lastname,emp_email,emp_password,emp_phonenumber,emp_doornum,emp_street,emp_area,emp_city,emp_photo,emp_role,emp_grade,emp_dateofbirth,emp_incomefromemp,emp_salary,emp_remarks) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = (firstname,lastname,email,password,phonenumber,doornum,street,area,city,photo,role,grade,dateofbirth,incomefromemp,salary,remarks)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")