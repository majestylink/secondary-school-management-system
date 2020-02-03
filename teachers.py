import mysql.connector
from indemo import mdbConfig

mdb = mysql.connector.connect(**mdbConfig)

mycursor = mdb.cursor()


class Teachers:
    def __init__(self, name, address, subject, clas):
        self.mdb = mysql.connector.connect(**mdbConfig)
        self.name = name
        self.address = address
        self.subject = subject
        self.clas = clas
        self.mycursor = self.mdb.cursor()
        print("You are connected to the database")
        print(self.mdb)

    def __del__(self):
        self.mdb.close()

    def employ(self):
        sql = "INSERT INTO teachers(name, address, subject, class) VALUES (%s, %s, %s, %s)"
        values = (self.name, self.address, self.subject, self.clas)
        self.mycursor.execute(sql, values)
        self.mdb.commit()
        print("Added to database")
        print('')
        print("CONGRATULATIONS TO THE NEWLY EMPLOYED TEACHER")


def view_all_teachers():
    mycursor.execute("SELECT * FROM teachers")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)


def sack():
    mycursor = mdb.cursor()
    teacher = input("Enter teacher's name: ")
    sql = "DELETE FROM teachers WHERE name = '{}'".format(teacher)
    mycursor.execute(sql)
    mdb.commit()
    print('')
    print("TEACHER'S RECORD DELETED FROM DATABASE")


def employ_teacher():
    name = input("Enter teacher's name: ")
    address = input("Enter teacher's address: ")
    subject = input("Enter teacher's subject: ")
    clas = input("Enter teacher's class: ")

    name = Teachers(name, address, subject, clas)
    name.employ()


def update_teacher_info():
    mycursor.execute("SELECT id, name, address, subject, class FROM teachers")
    rows = mycursor.fetchall()
    teacher = str(input("Enter teacher's name as it appears in the portal: "))
    mycursor.execute("SELECT id, name, address, subject, class FROM teachers WHERE name = '{}'".format(teacher))
    rows = mycursor.fetchall()
    ind = len(rows)
    if ind < 1:
        print("No teacher with the name")
        print("Make sure you enter the name as it is in the database \n")
        update_teacher_info()
    elif ind >= 1:
        edit_name = str(input("Do you want to edit name? Type 'YES' to edit or 'NO' to continue: "))
        edit_name = edit_name.upper()
        if edit_name == 'YES':
            edit_name = str(input("Enter the correct name: "))
        elif edit_name == 'NO':
            edit_name = rows[1]
        edit_address = str(input("Do you want to edit address? Type 'YES' to edit or 'NO' to continue: "))
        edit_address = edit_address.upper()
        if edit_address == 'YES':
            edit_address = str(input("Enter the correct address: "))
        elif edit_address == 'NO':
            edit_address = rows[2]
        edit_subject = str(input("Do you want to edit subject? Type 'YES' to edit or 'NO' to continue: "))
        edit_subject = edit_subject.upper()
        if edit_subject == 'YES':
            edit_subject = str(input("Enter the correct subject: "))
        elif edit_subject == 'NO':
            edit_subject = rows[3]
        edit_class = str(input("Do you want to edit class? Type 'YES' to edit or 'NO' to continue: "))
        edit_class = edit_class.upper()
        if edit_class == 'YES':
            edit_class = str(input("Enter the correct class: "))
        elif edit_class == 'NO':
            edit_class = rows[4]

        sql = "UPDATE students SET name = '{}', address = '{}', subject = '{}', class = '{}' WHERE id = {}".format(
            edit_name, edit_address, edit_subject, edit_class, rows[0])

        mycursor.execute(sql)
        mdb.commit()
        print("")
        print("TEACHER'S DATABASE EDITED SUCCESSFULLY")
    else:
        print("Invalid input \n")
        update_teacher_info()


# update_teacher_info()
