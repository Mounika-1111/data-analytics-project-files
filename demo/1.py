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
    name = input("enter your name :")
    age = input("enter your age :")
    grade = input("enter your grade :")
    email = input("enter your email id :")
    contact = input("enter your contact number :")
    sql= "insert into student_info (name, age, grade, email, contact)values(%s, %s,%s, %s,%s)"
    cursor.execute(sql, (name,age,grade,email,contact))
    connection.commit()
    print("students details added successfully")
# add_students()


def view_students():
    cursor.execute("select * from student_info")
    records=cursor.fetchall()
    print("student_info")
    for row in records:
        #print(row[0],row[1],row[2],row[3],row[4])1
        
        print("name:%s,age:%s,grade:%s,email:%s,contact:%s"%(row[0],row[1],row[2],row[3],row[4]))
# view_students()
def update_students():
    name=input("enter the name to be update :")
    age=input("enter the age to be update :")
    grade=input("enter the grade to be update :")
    email=input("enter the email to be update :")
    contact=input("enter the contact to be update :")
    sql="update student_info set name=%s,age=%s,grade=%s,email=%s,contact=%s where name=%s"
    cursor.execute(sql, (name,age,grade,email,contact,name))
    connection.commit()
    print("student details successfully updated...")

# a function to delete the students......

def delete_students():
    name = input("enter the name to be delete:")
    confirm = input(f"are you sure you want to delete '{name}'?(yes/no)")
    if confirm.lower()=='yes':
        sql = "delete from student_info where name=%s"
        cursor.execute(sql,(name,))
        connection.commit()
        print(f"student {name} deleted successfully")
    else:
        print("delete canceled")

'''def delete_students():
    name = input("Enter the name to be deleted: ")
    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ")

    if confirm.lower() == "yes":
        sql = "DELETE FROM student_info WHERE name = %s"
        cursor.execute(sql, (name,))
        connection.commit()
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")
'''
def main():
    while True:
        print("\n 1. add_students ")
        print("\n 2. view_students ")
        print("\n 3. exit")
        print("\n 4. update")
        print("\n 5. delete")
        choice=input("enter your choice:")
        if choice=='1':
            add_students()
        elif choice=='2':
            view_students()
        elif choice=='3':
            break
        elif choice=='4':
            update_students()
        elif choice=='5':
            delete_students()
        else:
            print("invalid choice :)")
main()            