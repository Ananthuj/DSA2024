import sqlite3

def execute_query(query):
    """Executes a given SQL query and fetches results."""
    connection = sqlite3.connect('employee_attendance.db')
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()  # Fetch all results
        return results
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        cursor.close()
        connection.close()

# Example usage
if __name__ == "__main__":
    # Get all employees
    all_employees_query = "SELECT * FROM employees;"
    employees = execute_query(all_employees_query)
    for emp in employees:
        print(emp)
        
    # Find an employee by ID
    employee_query = "SELECT * FROM employees WHERE employee_id = 'E001';"
    employee = execute_query(employee_query)
    print(employee)
