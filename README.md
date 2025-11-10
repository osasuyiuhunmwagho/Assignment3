# ASSIGNMENT 3

This project is a simple database management tool built with Python and PostgreSQL.  
It allows you to **view**, **add**, **update**, and **delete** student records from a `students` table in your database.

**Assignment Demonstration Video:**
https://youtu.be/4XNqTevtnEo

The goal of this project is to demonstrate:
- Secure database connections using environment variables
- Executing SQL queries with `psycopg2`
- Clean function-based database interactions
- Safe commit and connection handling using context managers

---

## 🚀 Features

 Feature | Description 
|--------|-------------|
| View Students | This fetches and list all students in the database |
| Add Student | this inserts a new student record |
| Update Email | Updates a student’s email by student ID |
| Delete Student | this removes a student record by thier student ID |

---

## Tech Stack

 Tool / Library | Purpose 
|----------------|---------|
| Python         | programming |
| PostgreSQL     | Database |
| psycopg2       | The PostgreSQL driver for Python |
| python-dotenv  | This loads the DB credentials from `.env` |

---
## Database Schema

Make sure your database contains the following table:

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
); 

## 📦 Installation & Setup

### 1. Clone the Repo

git clone https://github.com/yourusername/student-database-manager.git
cd Assignment3

#install dependencies
pip install psycopg2-binary python-dotenv

# Create a .env file in your project folder and add:
PGHOST=your_host
PGPORT=5432
PGDATABASE=your_database_name
PGUSER=your_user
PGPASSWORD=your_password

#Running the Program
python main.py

#If the connection is successful, you should see:
LETS GOOOO.... Successfully connected to the database!
