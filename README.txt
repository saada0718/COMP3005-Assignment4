Name: Saad Ahmed

Student Number: 101158210

Install Instructions:

    -> Note: Please refer to the internet on how to install these modules as they are different on each operating system

    1. Make sure you have python 3 installed (I had 3.11.2 installed)

    2. Install the following modules for python:
        -> psycopg2
            -> Run: 'pip install psycopg2' or 'pip3 install psycopg2'
        -> datetime
            -> Run: 'pip install datetime' or 'pip3 install datetime'

    3. A database was created in PostgreSQL with the following information:
        -> hostname = 'localhost'
        -> database = 'Students'
        -> username = 'postgres'
        -> password = 'postgres'
        -> port_ID = 5432

        -> Please create a database with these parameters or update these variables in the script.py file.

        -> If you are struggling with this step, please refer to the video submission as it will provide a visual
           demonstration.

Launch Instructions:

    1. Go to the directory where you downloaded my submission and go to the assignment4 directory from a terminal window.

    2. Type in the following:
        -> python3 script.py

    3. You will be presented with a menu asking what you want to do.

Functions and their purposes:

    -> NOTE: Additional documentation is provided in the script.py should it be needed.


    1. print_menu

        This function prints a menu for the user asking, them what they want to do.
           For example: add a student

    2. drop_table

        This function drops the students table if it exists.

    3. create_database

        This function deletes the students table if it currently exists and creates a new
        students table with the information given in the assignment specification and adds
        the initial values to the table.

    4. addStudent

        This function asks for the attributes for a new student (e.g., first name, last name, etc.)
        and error checks them. Once deemed valid, this function adds the information to the students
        table if it exists.

    5. validate_enrollment_date

        This function validates the enrollment date provided by the user. It is a helper function for
        addStudent function.

    6. validate_email

        This function validates the email provided by the user. It is a helper function for the addStudent
        function.

    7. validate_name
    
        This function validates the first and last name given by the user. It is a helper function for the 
        addStudent function. It makes sure there are no numerical or special characters in the name and only
        letters.

    8. getAllStudents

        This function gets all the students from the students table, if the table exists and prints them
        to the console.

    9. table_exists

       This function is responsible for determining if the students table exists. This is a helper
       function to help with error checking functionality.

    10. updateStudentEmail

        This function asks for current and new email and updates the email of a student with the given email in 
        the students table if the student with the given email exists and the table exists.

    11. student_with_email_exists

        This function determines if a user with the given email exists. This is a helper function for other functions.

    12. deleteStudent
    
        This function asks for a student ID and deletes the student with the student ID from the students table if the 
        table exists and the student with the student ID exists.

    13. student_id_exists

        This function determines if a student with the given ID exists in the students table.


DEMONSTRATION VIDEO LINK: https://youtu.be/KCJ7OgZnvJs
