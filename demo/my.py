import mysql.connector
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "demo_for_cec_students"
    )
cursor = connection.cursor()

#name, age, grade, email, contact

def add_students():
    name = input("enter your name")
    age = input("enter your age")
    grade = input("enter your grade")
    email = input("enter your email id")
    contact = input("enter your contact number")
    college = input("enter college name")
    sql= "insert into student_info (name, age, grade, email, contact, college)values(%s, %s,%s, %s,%s,%s)"
    cursor.execute(sql, (name,age,grade,email,contact,college))
    connection.commit()
    print("students details added successfully")
#add_students()




