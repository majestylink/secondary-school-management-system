import mysql.connector
from indemo import mdbConfig

mdb = mysql.connector.connect(**mdbConfig)

mycursor = mdb.cursor()


class Students:
    def __init__(self, name, address, clas, division, gender, post):
        self.mdb = mysql.connector.connect(**mdbConfig)
        self.name = name
        self.address = address
        self.clas = clas
        self.division = division
        self.gender = gender
        self.post = post
        self.mycursor = self.mdb.cursor()
        print("You are connected to the database")
        print(self.mdb)

    def admit(self):
        sql = "INSERT INTO students (name, address, class, division, gender, post) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.name, self.address, self.clas, self.division, self.gender, self.post)
        self.mycursor.execute(sql, values)
        self.mdb.commit()
        stu_res = "INSERT INTO results (name, ftca, fte, ftt, stca, ste, stt, ttca, tte, ttt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        stu_val = (self.name, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.mycursor.execute(stu_res, stu_val)
        self.mdb.commit()
        print("Added to database")
        print('')
        print("CONGRATULATIONS TO THE NEWLY ADMITTED STUDENT")


def view_all_students():
    mycursor.execute("SELECT name, address, class, gender, post FROM students")
    rows = mycursor.fetchall()
    for row in rows:
        if row:
            print(row)


def admit_student():
    name = input('Enter student name: ')
    address = input("Enter student's address: ")
    clas = input("Enter student's class: ")
    division = input("Enter division: ")
    division = division.upper()
    gender = input("Enter student's gender: ")
    post = input('Post? ')
    post = post.upper()
    if post == 'YES':
        st_post = input("Enter student's post: ")
    elif post == 'NO':
        st_post = 'No post'
    else:
        st_post = 'N/A'

    name = Students(name, address, clas, division, gender, st_post)
    name.admit()


'''
mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), "
                 "class VARCHAR(5), division VARCHAR(1), gender VARCHAR(10), post VARCHAR(50))")

mycursor.execute("ALTER TABLE students ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST")

mycursor.execute("DROP TABLE subjects")

mycursor.execute("CREATE TABLE IF NOT EXISTS subjects (id INT AUTO_INCREMENT PRIMARY KEY, subjects VARCHAR(255) NOT "
                 "NULL,jss1 BOOLEAN NOT NULL DEFAULT 0, jss2 BOOLEAN NOT NULL DEFAULT 0, jss3 BOOLEAN NOT NULL DEFAULT 0, sss1 BOOLEAN NOT NULL DEFAULT 0, "
                 "sss2 BOOLEAN NOT NULL DEFAULT 0, sss3 BOOLEAN NOT NULL DEFAULT 0)")


sql = "INSERT INTO subjects (subjects, jss1, jss2, jss3, sss1, sss2, sss3) VALUES (%s, %s, %s, %s, %s, %s, %s)"
valu = ('Chemistry', False, False, False, True, True, True,)
mycursor.execute(sql, valu)
mdb.commit()
'''


def result_total():
    mdb = mysql.connector.connect(**mdbConfig)

    mycursor = mdb.cursor()
    mycursor.execute("SELECT con_access, exam FROM students")
    # mycursor.execute("SELECT CAST(con_access AS UNSIGNED) as con_access, CAST(exam AS UNSIGNED) as exam FROM
    # students")
    rows = mycursor.fetchall()
    for row in rows:
        if row:
            total = sum(row)
            # total = row['con_access'] + row['exam']
            # print(total)
            # sql = "UPDATE students SET total = {}".format(total)
            # mycursor.execute(sql)
            # mdb.commit()
            # print('DONE')


def promote():
    mdb = mysql.connector.connect(**mdbConfig)
    mycursor = mdb.cursor()
    mycursor.execute("SELECT name, average FROM results")
    rows = mycursor.fetchall()
    for row in rows:
        name = row[0]
        average = row[1]
        sql = "UPDATE students SET average = {} WHERE name = '{}'".format(average, name)
        mycursor.execute(sql)
        mdb.commit()
        print('Done')


def promote_helper():
    mycursor.execute("SELECT name, class FROM students")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
        name = str(row[0])
        if str(row[1]) == 'JSS1' or str(row[1]) == 'JS1':
            print("Executing first if")
            sql = "UPDATE students SET class = '{}' WHERE name = '{}'".format('JSS2', name)
            mycursor.execute(sql)
            mdb.commit()
            print("Processing " + name + "'s data \n")
        elif str(row[1]) == 'JSS2' or str(row[1]) == 'JS2':
            print("Executing second if")
            sql = "UPDATE students SET class = '{}' WHERE name = '{}'".format('JSS3', name)
            mycursor.execute(sql)
            mdb.commit()
            print("Processing " + name + "'s data \n")
        elif str(row[1]) == 'JSS3' or str(row[1]) == 'JS3':
            print("Executing third if")
            sql = "UPDATE students SET class = '{}' WHERE name = '{}'".format('SSS1', name)
            mycursor.execute(sql)
            mdb.commit()
            print("Processing " + name + "'s data \n")
        elif str(row[1]) == 'SSS1' or str(row[1]) == 'SS1':
            print("Executing fourth if")
            sql = "UPDATE students SET class = '{}' WHERE name = '{}'".format('SSS2', name)
            mycursor.execute(sql)
            mdb.commit()
            print("Processing " + name + "'s data \n")
        elif str(row[1]) == 'SSS2' or str(row[1]) == 'SS2':
            print("Executing fifth if")
            sql = "UPDATE students SET class = '{}' WHERE name = '{}'".format('SSS3', name)
            mycursor.execute(sql)
            mdb.commit()
            print("Processing " + name + "'s data \n")
        elif str(row[1]) == 'SSS3' or str(row[1]) == 'SS3':
            print("Executing sixth if")
            sql = "UPDATE students SET class = '{}' WHERE name = '{}'".format('PASSED', name)
            mycursor.execute(sql)
            mdb.commit()
            print('Done \n')
        else:
            print('Invalid')


def expel():
    mycursor = mdb.cursor()
    teacher = input("Enter student's name: ")
    sql = "DELETE FROM students WHERE name = '{}'".format(teacher)
    mycursor.execute(sql)
    mdb.commit()
    print('')
    print("STUDENT'S RECORD DELETED FROM DATABASE - EXPELLED")


def update_student_info():
    mycursor.execute("SELECT name, address, class, division, gender, post FROM students")
    rows = mycursor.fetchall()
    student = str(input("Enter student's name as it appears in the portal: "))
    mycursor.execute(
        "SELECT name, address, class, division, gender, post, id FROM students WHERE name = '{}'".format(student))
    rows = mycursor.fetchall()
    ind = len(rows)
    if ind < 1:
        print("No student with the name")
        print("Make sure you enter the name as it is in the database \n")
        update_student_info()
    elif ind >= 1:
        edit_name = str(input("Do you want to edit name? Type 'YES' to edit or 'NO' to continue: "))
        edit_name = edit_name.upper()
        if edit_name == 'YES':
            edit_name = str(input("Enter the correct name: "))
        elif edit_name == 'NO':
            edit_name = rows[0][0]
        edit_address = str(input("Do you want to edit address? Type 'YES' to edit or 'NO' to continue: "))
        edit_address = edit_address.upper()
        if edit_address == 'YES':
            edit_address = str(input("Enter the correct address: "))
        elif edit_address == 'NO':
            edit_address = rows[0][1]
        edit_class = str(input("Do you want to edit class? Type 'YES' to edit or 'NO' to continue: "))
        edit_class = edit_class.upper()
        if edit_class == 'YES':
            edit_class = str(input("Enter the correct class: "))
        elif edit_class == 'NO':
            edit_class = rows[0][2]
        edit_division = str(input("Do you want to edit division? Type 'YES' to edit or 'NO' to continue: "))
        edit_division = edit_division.upper()
        if edit_division == 'YES':
            edit_division = str(input("Enter the correct division: "))
        elif edit_division == 'NO':
            edit_division = rows[0][3]
        edit_gender = str(input("Do you want to edit gender? Type 'YES' to edit or 'NO' to continue: "))
        edit_gender = edit_gender.upper()
        if edit_gender == 'YES':
            edit_gender = str(input("Enter the correct gender: "))
        elif edit_gender == 'NO':
            edit_gender = rows[0][4]
        edit_post = str(input("Do you want to edit post? Type 'YES' to edit or 'NO' to continue: "))
        edit_post = edit_post.upper()
        if edit_post == 'YES':
            edit_post = str(input("Is the student still a prefect? Reply with 'YES' or 'NO': "))
            edit_post = edit_post.upper()
            if edit_post == 'YES':
                edit_post = str(input("Enter the correct post: "))
            elif edit_post == 'NO':
                edit_post = 'No post'
        elif edit_post == 'NO':
            edit_post = rows[0][5]

        sql = "UPDATE students SET name = '{}', address = '{}', class = '{}', division = '{}', gender = '{}', " \
              "post = '{}' WHERE id = {}".format(edit_name, edit_address, edit_class, edit_division, edit_gender,
                                                 edit_post, rows[0][6])
        mycursor.execute(sql)
        mdb.commit()
        print("")
        print("STUDENT DATABASE EDITED SUCCESSFULLY")
    else:
        print("Invalid input \n")
        update_student_info()
