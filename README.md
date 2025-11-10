# ASSIGNMENT 3

This project is a simple database management tool built with Python and PostgreSQL.  
It allows you to **view**, **add**, **update**, and **delete** student records from a `students` table in your database.
#LINK TO VIDEO :
https://youtu.be/4XNqTevtnEo

The goal of this project is to demonstrate:
- Secure database connections using environment variables
- Executing SQL queries with `psycopg2`
- Clean function-based database interactions
- Safe commit and connection handling using context managers

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| View Students | This fetches and list all students in the database |
| Add Student | this inserts a new student record |
| Update Email | Updates a student’s email by student ID |
| Delete Student | this removes a student record by thier student ID |

---

## 🧰 Tech Stack

| Tool / Library | Purpose |
|----------------|---------|
| Python         | programming |
| PostgreSQL     | Database |
| psycopg2       | PostgreSQL driver for Python |
| python-dotenv  | Loads the DB credentials from `.env` |

---

## 📦 Installation & Setup

### 1. Clone the Repo

git clone https://github.com/yourusername/student-database-manager.git
cd student-database-manager

#install dependencies
pip install psycopg2-binary python-dotenv

# Create a .env file in your project folder and add:
PGHOST=your_host
PGPORT=5432
PGDATABASE=your_database_name
PGUSER=your_user
PGPASSWORD=your_password
