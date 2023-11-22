import psycopg2
import datetime

#Information to connect to database
hostname = 'localhost'
database = 'Students'
username = 'postgres'
pwd = 'postgres'
port_id = 5432

connection = None
cur = None

#Constants to help with menu selection
GET_ALL_STUDENTS = 1
ADD_STUDENT = 2
UPDATE_STUDENT_EMAIL = 3
DELETE_STUDENT = 4
QUIT = 5

"""
   Name: print_menu
   Parameters: None
   Output: None
   Purpose: The purpose of this function is to print a menu for
            the user.
    Author: Saad Ahmed (101158210)
"""
def print_menu():

    print("Enter 1 to get all the students")
    print("Enter 2 to add a student")
    print("Enter 3 to update a student's email")
    print("Enter 4 to delete a student")
    print("Enter 5 to quit.")

"""
    Name: drop_table
    Parameters: connection, cur
    Output: None
    Purpose: The purpose of this function is to drop the students table
             if it exists.
    Author: Saad Ahmed
"""
def drop_table(connection, cur):

    query = 'DROP TABLE IF EXISTS students;'
    cur.execute(query)
    connection.commit()

"""
    Name: create_database
    Parameters: connection, cur
    Output: None
    Purpose: The purpose of this function is to create the students table
             with the information provided as per the assignment specification.
             If the student tables exists. This function will drop the table
             and create a new table with the initial values.
    Author: Saad Ahmed (101158210)
"""
def create_database(connection, cur):

    drop_table(connection, cur)

    query = '''CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date DATE);'''


    cur.execute(query)

    addStudents_script = 'INSERT INTO students ( first_name, last_name, email, enrollment_date ) VALUES ( %s, %s, %s, %s );'
    student_values = [('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')]


    for student in student_values:
        cur.execute(addStudents_script, student)

    connection.commit()

"""
    Name: validate_enrollment_date
    Parameters: enrollment_date
    Output: bool
    Purpose: The purpose of this function is to validate the 
             enrollment date passed in as the parameter.
             This function is a helper function for the 
             addStudent function. The date needs to be in the
             following format to be considered valid (yyyy-dd-mm)
    Author: Saad Ahmed (101158210)
"""
def validate_enrollment_date(enrollment_date):

    date_format = "%Y-%d-%m"

    try:

        datetime.datetime.strptime(enrollment_date, date_format)

        return True

    except Exception as error:

        return False



"""
    Name: validate_email
    Parameters: email, cur
    Output: bool
    Purpose: The purpose of this function is to validate the email provided by the user.
             This function serves as a helper function for the addStudent function.
             If the email provided has a length of zero it is considered invalid or if a
             student with the given email already exists.
    Author: Saad Ahmed (101158210)
"""
def validate_email(email, cur):

    if len(email) == 0:

        return False

    if student_with_email_exists(email, cur) == True:

        return False

    return True

"""
    Name: validate_name
    Parameters: name
    Output: bool
    Purpose: The purpose of this function is to return a boolean based on if the name is valid or not.
             If the name has a length greater than zero and does not contain any numbers or special characters,
             then it is considered valid.
             This function is a helper function for the addStudent function.
    Author: Saad Ahmed (101158210)
"""
def validate_name(name):

    if len(name) == 0:

        return False

    for  i in name:

        if (i < 'a' or i > 'z') and ( i < 'A' or i > 'Z' ): #No special characters or numbers allowed

            return False

    return True

"""
    Name: table_exists
    Parameters: cur
    Output: bool
    Purpose: The purpose of this function is to determine if the table students exists.
             This is a helper function which handles basic error checking for other functions.
    Author: Saad Ahmed (101158210)
"""
def table_exists(cur):

    query = '''SELECT EXISTS ( SELECT 1 FROM information_schema.tables WHERE table_name = 'students' ) AS table_existance;'''
    cur.execute(query)

    table_existance = cur.fetchall()

    if bool(table_existance[0][0]) == False:

        return False

    return True

"""
    Name: student_with_email_exists
    Parameters: email, cur
    Output: bool
    Purpose: The purpose of this function is to determine if a student
             with the given email exists.

             This function assumes that the table students exists. Please
             make sure that the table students exists prior to calling this
             function.
    Author: Saad Ahmed (101158210)
"""
def student_with_email_exists(email, cur):

    query = "SELECT email FROM students WHERE email='"  + email + "';"
    cur.execute(query)

    if len(cur.fetchall()) == 1:
        return True

    return False

"""
    Name: student_id_exists
    Parameters: student_id, cur
    Output: bool
    Purpose: The purpose of this function is to determine if the ID passed
             in the parameter exists in the students table. This function
             serves as a helper function fro deleteStudent function.

             This function assuomes that the table students exists. Please
             make sure that the table exists before calling this function.
    Author: Saad Ahmed (101158210)
"""
def student_id_exists(student_id, cur):

    query = "SELECT student_id FROM students where student_id='"  + str(student_id) + "';"
    cur.execute(query)

    if len(cur.fetchall()) == 1:
        return True

    return False


try:
    connection = psycopg2.connect(

        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id )

    cur = connection.cursor()

    drop_table(connection, cur)

    create_database(connection,cur)

    while True:

        if table_exists(cur) == False:

            print("Table does not exist. Please create table first.")
            continue


        print_menu()
        value = input()

        if value.isnumeric() == False:

            print("The value given is non-numeric please try again.")
            continue

        value = int(value)

        if value == GET_ALL_STUDENTS:

            """
                Name: getAllStudents
                Parameters: None
                Output: None
                Purpose: The purpose of this function is to retreive all the students from the
                         students table and print them. This function assumes all the error checking
                         functionality has been handled
                Author: Saad Ahmed (101158210)
            """
            def getAllStudents():

                query = '''SELECT * FROM students;'''
                cur.execute(query)

                for student in cur.fetchall():
                    print(student)

            getAllStudents()

        elif value == ADD_STUDENT:

            """
                Name: addStudent
                Parameter: first_name, last_name, email, enrollment_date
                Output: None
                Purpose: The purpose of this function is to add the student with given information
                         to the student's table. This function assumes that all error checking
                         functionality has been handled.
                Author: Saad Ahmed (101158210)
            """
            def addStudent(first_name, last_name, email, enrollment_date):

                query = 'INSERT INTO students ( first_name, last_name, email, enrollment_date ) VALUES ( %s, %s, %s, %s ); '
                student_value = ( first_name, last_name, email, enrollment_date )

                cur.execute(query, student_value)
                connection.commit()


            first_name = input("Enter Student's first name: ")

            if validate_name(first_name) == False:

                print("First Name given is invalid")
                print("First Name needs to have a length greater than 0 and cannot contain any numbers or special characters")

                continue
            
            last_name  = input("Enter student's last name: ")

            if validate_name(last_name) == False:

                print("Last Name given is invalid.")
                print("Last Name needs to have a length greater than 0 and cannot contain any numbers or special characters")
                continue

            email = input("Enter student's email: ")

            if validate_email(email, cur) == False:

                print("Email Given is invalid. Make sure that the email has a length greater than zero.")
                continue


            enrollment_date = input("Enter student's enrollment date(yyyy-dd-mm): ")

            if validate_enrollment_date(enrollment_date) == False:

                print("Date given is invalid. Please provide a date in the following format (yyyy-dd-mm)")
                continue

            addStudent(first_name, last_name, email, enrollment_date)

        elif value == UPDATE_STUDENT_EMAIL:


            """
                Name: updateStudentEmail
                Parameters: student_id, new_email
                Output: None
                Purpose: The purpose of this function is update the students email with the given email to the new email.
                         The function assumes that all the error checking has already been handled prior to the adding
                         of information.
                Author: Saad Ahmed (101158210)
            """
            def updateStudentEmail(student_id, new_email):


                query = "UPDATE students SET email='" + new_email + "' WHERE student_id='" + str(student_id) + "';"
                cur.execute(query)
                connection.commit()

            student_id = input("Enter the student's id whose email you would like to change: ")

            if student_id.isnumeric() == False:

                print("The ID that you gave is not a number; thus, invalid.")

                continue

            student_id = int(student_id)

            if student_id_exists(student_id, cur) == False:

                print("Sorry. There is no student with the given ID in our database.")

                continue

            new_email = input("Enter student's new email: ")

            if validate_email(new_email, cur) == False:

                print("The new email that you provided is already exists, or is invalid. Please try again.")

                continue

            updateStudentEmail(student_id, new_email)

        elif value == DELETE_STUDENT:


            """
                Name: deleteStudent
                Parameters: student_id
                Output: None
                Purpose: The purpose of this function is to delete the student with the given ID from the students
                         table. The function assumes that all the error checking functionality has been handled.
                Author: Saad Ahmed (101158210)
            """
            def deleteStudent(student_id):


                query = "DELETE FROM students WHERE student_id=%s"

                cur.execute(query, str(student_id))
                connection.commit()


            student_id = input("Enter student id to delete: ")

            if student_id.isnumeric() == False:

                print("The student id that you provided is non numeric.")
                continue

            student_id = int(student_id)

            if student_id_exists(student_id, cur) == False:

                print("Unfortunately, this student ID does not exist in the table.")
                continue

            deleteStudent(student_id)

        elif value == QUIT:

            break

        else:

            print("Invalid option provided. Please try again.")

        print("\n\n\n\n") #Create some space

    cur.close()
    connection.close()

except Exception as error:
    print(error)
finally:

    if cur is not None:
        cur.close()

    if connection is not None:
        connection.close()
