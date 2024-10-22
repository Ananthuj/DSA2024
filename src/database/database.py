import sqlite3
import os

# --------------------Establish the connection----------------------------
def get_connection(db_name='employee_attendance.db'):
    """Establishes and returns a connection to the SQLite database."""
    return sqlite3.connect(db_name)

def close_connection(connection):
    """Closes the SQLite database connection."""
    if connection:
        connection.close()

#----------------------read image as BLOB-------------------------------
def read_image_as_blob(image_path):
    """Reads an image from the given path and returns it as binary data (BLOB)."""
    try:
        with open(image_path, 'rb') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading image {image_path}: {e}")
        return None

# ----------------------------Create tables------------------------------
def create_tables():
    """Creates the departments, employees, and attendance tables in the SQLite database."""
    connection = get_connection()
    cursor = connection.cursor()

    # Drop tables if they exist
    cursor.execute('DROP TABLE IF EXISTS attendance;')
    cursor.execute('DROP TABLE IF EXISTS employees;')
    cursor.execute('DROP TABLE IF EXISTS departments;')
    cursor.execute('DROP TABLE IF EXISTS login;')

    #create login page
    cursor.execute('''
         CREATE TABLE IF NOT EXISTS login (
         username TEXT PRIMARY KEY,
         password TEXT NOT NULL
        )''')
    
    # Create departments table
    cursor.execute(''' 
        CREATE TABLE departments (
            department_id INTEGER PRIMARY KEY AUTOINCREMENT,
            department_name TEXT NOT NULL
        );
    ''')

    # Create employees table
    cursor.execute(''' 
        CREATE TABLE employees (
            employee_id TEXT PRIMARY KEY,
            employee_name TEXT NOT NULL,
            department_id INTEGER,
            email TEXT,
            phone_number TEXT,
            dob DATE,
            address TEXT NOT NULL,
            designation TEXT NOT NULL,
            gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')) NOT NULL,
            hire_date DATE,
            termination_date DATE DEFAULT NULL,
            FOREIGN KEY (department_id) REFERENCES departments (department_id)
        ); 
    ''')

    # Create attendance table
    cursor.execute(''' 
        CREATE TABLE attendance (
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT,
            checkin_time TIMESTAMP DEFAULT NULL,
            checkout_time TIMESTAMP DEFAULT NULL,
            attendance_date DATE DEFAULT NULL,
            attendance_status TEXT CHECK(attendance_status IN ('Present', 'Absent', 'Leave')) DEFAULT NULL,
            FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
        );
    ''')

    connection.commit()
    cursor.close()
    connection.close()

# ---------------------Insert department data----------------------------
def insert_department_data():
    """Inserts multiple department records into the departments table."""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Insert department data
        cursor.executemany(''' 
            INSERT INTO departments (department_name) VALUES (?);
        ''', [
            ('HR',),
            ('Finance',),
            ('IT',),
            ('Marketing',),
            ('Sales',),
            ('Support',),
            ('Development',),
            ('Research',),
            ('Administration',),
            ('Logistics',)
        ])
        connection.commit()
        print("Department data inserted successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        close_connection(connection)

# ---------------------Insert employee details--------------------------
def insert_employee_data():
    """Inserts employee records into the employees' table."""
    conn = get_connection()
    cursor = conn.cursor()

    # List of employees
    employee_data = [
        ('E001', 'Employee 1', 1, 'emp1@example.com', '1234567890', '1990-01-01', 'Address 1', 'Manager', 'Male', '2022-01-01', None),
        ('E002', 'Employee 2', 2, 'emp2@example.com', '2345678901', '1991-02-01', 'Address 2', 'Engineer', 'Female', '2021-05-01', None),
        ('E003', 'Employee 3', 3, 'emp3@example.com', '3456789012', '1992-03-01', 'Address 3', 'Developer', 'Male', '2020-03-15', None),
        ('E004', 'Employee 4', 4, 'emp4@example.com', '4567890123', '1993-04-01', 'Address 4', 'Analyst', 'Female', '2019-08-10', None),
        ('E005', 'Employee 5', 5, 'emp5@example.com', '5678901234', '1994-05-01', 'Address 5', 'Consultant', 'Male', '2023-02-20', None)
    ]

    try:
        # Insert employee data into the employees table
        cursor.executemany('''
            INSERT INTO employees (employee_id, employee_name, department_id, email, phone_number, dob, address, designation, gender, hire_date, termination_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', employee_data)

        conn.commit()
        print("Employee data inserted successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        cursor.close()
        conn.close()


# ---------------------------Insert attendance data------------------------
def insert_attendance_data():
    """Inserts attendance records with photos into the attendance table."""
    conn = get_connection()
    cursor = conn.cursor()

    
    

    # Attendance data (adjust according to actual attendance data)
    attendance_data = [
        ('E001', '2024-10-09 08:30:00', '2024-10-09', 'Present'),
        ('E002', '2024-10-09 08:35:00', '2024-10-09', 'Present'),
        ('E003', '2024-10-09 08:40:00', '2024-10-09', 'Absent'),
        ('E004', '2024-10-09 08:45:00', '2024-10-09', 'Present'),
        ('E005', '2024-10-09 08:50:00', '2024-10-09', 'Leave')
    ]

    
    # Commit the changes
    conn.commit()
    cursor.close()
    conn.close()

    print("Attendance data with photos has been inserted successfully.")

# ----------------------------Main program-----------------------------
if __name__ == "__main__":
    create_tables()  # Assuming you have this function for creating necessary tables
    insert_department_data()  # Assuming you have this function for department data
    insert_employee_data()
    insert_attendance_data()
 