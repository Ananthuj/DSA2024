import sqlite3

def get_connection(db_name='employee_attendance.db'):
    """Establishes and returns a connection to the SQLite database."""
    return sqlite3.connect(db_name)

def close_connection(connection):
    """Closes the SQLite database connection."""
    if connection:
        connection.close()

# ------------------- Search Queries ---------------------------------

# 1. Retrieve all employees
def get_all_employees():
    query = "SELECT * FROM employees;"
    return execute_query(query)

# 2. Find employee by ID
def find_employee_by_id(employee_id):
    query = f"SELECT * FROM employees WHERE employee_id = '{employee_id}';"
    return execute_query(query)

# 3. Get all departments
def get_all_departments():
    query = "SELECT * FROM departments;"
    return execute_query(query)

# 4. Get employees by department
def get_employees_by_department(department_id):
    query = f"SELECT * FROM employees WHERE department_id = {department_id};"
    return execute_query(query)

# 5. Get attendance by employee
def get_attendance_by_employee(employee_id):
    query = f"SELECT * FROM attendance WHERE employee_id = '{employee_id}';"
    return execute_query(query)

# 6. Get attendance on a specific date
def get_attendance_by_date(attendance_date):
    query = f"SELECT * FROM attendance WHERE attendance_date = '{attendance_date}';"
    return execute_query(query)

# 7. Count employees per department
def count_employees_per_department():
    query = "SELECT department_id, COUNT(*) as employee_count FROM employees GROUP BY department_id;"
    return execute_query(query)

# 8. Get employees on leave on a specific date
def get_employees_on_leave(attendance_date):
    query = f"SELECT * FROM attendance WHERE attendance_status = 'Leave' AND attendance_date = '{attendance_date}';"
    return execute_query(query)

# 9. Get employees who are present on a specific date
def get_employees_present(attendance_date):
    query = f"SELECT * FROM attendance WHERE attendance_status = 'Present' AND attendance_date = '{attendance_date}';"
    return execute_query(query)

# 10. Get employees absent on a specific date
def get_employees_absent(attendance_date):
    query = f"SELECT * FROM attendance WHERE attendance_status = 'Absent' AND attendance_date = '{attendance_date}';"
    return execute_query(query)

# 11. Get employee contact details (name, email, phone)
def get_employee_contacts():
    query = "SELECT employee_name, email, phone_number FROM employees;"
    return execute_query(query)

# 12. Get attendance for a specific month
def get_attendance_for_month(year_month):
    query = f"SELECT * FROM attendance WHERE strftime('%Y-%m', attendance_date) = '{year_month}';"
    return execute_query(query)

# 13. Find terminated employees
def get_terminated_employees():
    query = "SELECT * FROM employees WHERE termination_date IS NOT NULL;"
    return execute_query(query)

# ----------------- Utility function to execute queries -------------------
def execute_query(query):
    """Executes a given SQL query and fetches results."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()

# -------------------------- Example usage --------------------------------
if __name__ == "__main__":
    # Example 1: Get all employees
    employees = get_all_employees()
    for emp in employees:
        print(emp)
    
    # Example 2: Find employee by ID
    employee = find_employee_by_id('E001')
    print(employee)
    
    # Example 3: Get all departments
    departments = get_all_departments()
    for dept in departments:
        print(dept)
    
    # Example 4: Get employees by department
    employees_in_dept = get_employees_by_department(1)
    for emp in employees_in_dept:
        print(emp)
    
    # Example 5: Get attendance by employee
    attendance = get_attendance_by_employee('E001')
    for record in attendance:
        print(record)

    # Example 6: Get attendance on a specific date
    attendance_on_date = get_attendance_by_date('2024-10-09')
    for record in attendance_on_date:
        print(record)

    # Example 7: Count employees per department
    employee_count_per_dept = count_employees_per_department()
    for count in employee_count_per_dept:
        print(count)
    
    # Example 8: Get employees on leave for a specific date
    employees_on_leave = get_employees_on_leave('2024-10-09')
    for emp in employees_on_leave:
        print(emp)

    # Example 9: Get employees present on a specific date
    employees_present = get_employees_present('2024-10-09')
    for emp in employees_present:
        print(emp)

    # Example 10: Get employees absent on a specific date
    employees_absent = get_employees_absent('2024-10-09')
    for emp in employees_absent:
        print(emp)

    # Example 11: Get employee contacts
    contacts = get_employee_contacts()
    for contact in contacts:
        print(contact)

    # Example 12: Get attendance for a specific month
    attendance_in_month = get_attendance_for_month('2024-10')
    for record in attendance_in_month:
        print(record)

    # Example 13: Find terminated employees
    terminated_employees = get_terminated_employees()
    for emp in terminated_employees:
        print(emp)
