import mysql.connector
from indemo import mdbConfig

mdb = mysql.connector.connect(**mdbConfig)

mycursor = mdb.cursor()
# mycursor.execute("DROP TABLE subjects")


# mycursor.execute("CREATE TABLE subjects (id MEDIUMINT AUTO_INCREMENT PRIMARY KEY, class VARCHAR(50), subject VARCHAR(255))")
# mycursor.execute("ALTER TABLE subjects DROP COLUMN id")
# mycursor.execute("ALTER TABLE subjects ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST")


def add_courses():
    sql = "INSERT INTO subjects (subjects, jss1, jss2, jss3, sss1, sss2, sss3) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (input("Enter subject name: "), False, False, False, False, False, False)
    mycursor.execute(sql, values)
    mdb.commit()
    print("Added Successfully")


def add_to_jss1():
    mycursor.execute("SELECT id, subjects FROM subjects")
    rows = mycursor.fetchall()
    for row in rows:
        choice = input("Add " + row[1] + " to JSS1 subjects? ").upper()
        if choice == 'YES':
            mycursor.execute("UPDATE subjects SET jss1 = {} WHERE id = {}".format(True, row[0]))
            mdb.commit()
        elif choice == 'NO':
            continue
        else:
            print("Invalid command")


def add_to_jss2():
    mycursor.execute("SELECT id, subjects FROM subjects")
    rows = mycursor.fetchall()
    for row in rows:
        choice = input("Add " + row[1] + " to JSS3 subjects? ").upper()
        if choice == 'YES':
            mycursor.execute("UPDATE subjects SET jss2 = {} WHERE id = {}".format(True, row[0]))
            mdb.commit()
        elif choice == 'NO':
            continue
        else:
            print("Invalid command")


def add_to_jss3():
    mycursor.execute("SELECT id, subjects FROM subjects")
    rows = mycursor.fetchall()
    for row in rows:
        choice = input("Add " + row[1] + " to JSS3 subjects? ").upper()
        if choice == 'YES':
            mycursor.execute("UPDATE subjects SET jss3 = {} WHERE id = {}".format(True, row[0]))
            mdb.commit()
        elif choice == 'NO':
            continue
        else:
            print("Invalid command")


def add_to_sss1():
    mycursor.execute("SELECT id, subjects FROM subjects")
    rows = mycursor.fetchall()
    for row in rows:
        choice = input("Add " + row[1] + " to SSS1 subjects? ").upper()
        if choice == 'YES':
            mycursor.execute("UPDATE subjects SET SSS1 = {} WHERE id = {}".format(True, row[0]))
            mdb.commit()
        elif choice == 'NO':
            continue
        else:
            print("Invalid command")


def add_to_sss2():
    mycursor.execute("SELECT id, subjects FROM subjects")
    rows = mycursor.fetchall()
    for row in rows:
        choice = input("Add " + row[1] + " to SSS2 subjects? ").upper()
        if choice == 'YES':
            mycursor.execute("UPDATE subjects SET SSS2 = {} WHERE id = {}".format(True, row[0]))
            mdb.commit()
        elif choice == 'NO':
            continue
        else:
            print("Invalid command")


def add_to_sss3():
    mycursor.execute("SELECT id, subjects FROM subjects")
    rows = mycursor.fetchall()
    for row in rows:
        choice = input("Add " + row[1] + " to SSS3 subjects? ").upper()
        if choice == 'YES':
            mycursor.execute("UPDATE subjects SET SSS3 = {} WHERE id = {}".format(True, row[0]))
            mdb.commit()
        elif choice == 'NO':
            continue
        else:
            print("Invalid command")


def view_jss1_subjects():
    mycursor.execute("SELECT subjects FROM subjects WHERE jss1 = True")
    rows = mycursor.fetchall()
    if len(rows) < 1:
        print("No subject for this class!")
    else:
        for row in rows:
            print(row)


def view_jss2_subjects():
    mycursor.execute("SELECT subjects FROM subjects WHERE jss2 = True")
    rows = mycursor.fetchall()
    if len(rows) < 1:
        print("No subject for this class!")
    else:
        for row in rows:
            print(row)


def view_jss3_subjects():
    mycursor.execute("SELECT subjects FROM subjects WHERE jss3 = True")
    rows = mycursor.fetchall()
    if len(rows) < 1:
        print("No subject for this class!")
    else:
        for row in rows:
            print(row)


def view_sss1_subjects():
    mycursor.execute("SELECT subjects FROM subjects WHERE sss1 = True")
    rows = mycursor.fetchall()
    if len(rows) < 1:
        print("No subject for this class!")
    else:
        for row in rows:
            print(row)


def view_sss2_subjects():
    mycursor.execute("SELECT subjects FROM subjects WHERE sss2 = True")
    rows = mycursor.fetchall()
    if len(rows) < 1:
        print("No subject for this class!")
    else:
        for row in rows:
            print(row)


def view_sss3_subjects():
    mycursor.execute("SELECT subjects FROM subjects WHERE sss3 = True")
    rows = mycursor.fetchall()
    if len(rows) < 1:
        print("No subject for this class!")
    else:
        for row in rows:
            print(row)


# add_courses()
# add_to_jss1()
# add_to_jss2()
# add_to_jss3()
# add_to_sss1()
# add_to_sss2()
# add_to_sss3()
# view_jss1_subjects()
# view_jss2_subjects()
# view_jss3_subjects()
# view_sss1_subjects()
# view_sss2_subjects()
# view_sss3_subjects()
