# used to read environment variables
import os
#used to connect to and interact with a PostgreSQL database from Python.
import psycopg2

from dotenv import load_dotenv

# Load my credentials from .env
load_dotenv()  


def get_connection():
    #getting credentials from .env files and create a connection to the database
    return psycopg2.connect(
        host=os.getenv("PGHOST"),
        port=os.getenv("PGPORT"),
        database=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD")
    )


def getAllStudents():
    try:
        with get_connection() as dbconnected: # connecting to the database
            with dbconnected.cursor() as cur: #this is like a messenger sending commands to the database and returns result
                cur.execute("SELECT * FROM students ORDER BY student_id;") # run the query
                
                return cur.fetchall() #retrieving the data from the SELECT query
    except psycopg2.Error as e:
        print(f" Error retrieving students: {e}")
        return []


def addStudent(first_name, last_name, email, enrollment_date):
    try:
        with get_connection() as dbconnected:
            with dbconnected.cursor() as cur:
                # %s is the placeholder for psycopg2.
                cur.execute(
                    "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                    (first_name, last_name, email, enrollment_date)
                )
                # save changes from the sql statement
                dbconnected.commit()
                print("- - Student added successfully- -.")
    except psycopg2.Error as e:
        print(f" Error adding student: {e}")


def updateStudentEmail(student_id, new_email):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE students SET email = %s WHERE student_id = %s",
                    (new_email, student_id)
                )
                conn.commit()
                print(" Email updated successfully!! ")
    except psycopg2.Error as e:
        print(f"There was an error updating student email: {e}")


def deleteStudent(student_id):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
                conn.commit()
                print(" Student deleted successfully.")
    except psycopg2.Error as e:
        print(f"There was an error deleting student: {e}")


if __name__ == "__main__":
    try:
        conn = get_connection()
        print("LETS GOOOO.... Successfully connected to the database!")

        #print("\n Fetching all students...")
        
        #students = getAllStudents()
        #for student in students:
        
        #   print(student) 

        
        # test add student
        #addStudent("testfirst", "testname", "test@gmail.com", "2024-09-08")
        
        # Test updateStudentEmail
        #updateStudentEmail(17, "suyi.uhun@example.com")
        
        # Test deleteStudent
        #deleteStudent(18)

        # Closing the connection
        conn.close()
        print("Connection closed.")

    except psycopg2.Error as e:
        print(f"There was an error connecting to database: {e}")