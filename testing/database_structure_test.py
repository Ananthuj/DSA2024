import sqlite3


# Function to drop the attendance table if it exists
def drop_attendance_table():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS attendance;")
    conn.commit()
    conn.close()


# Function to create the attendance table
def create_attendance_table():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


# Function to test the database structure
def test_database_structure():
    # Connect to the SQLite database
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # 1. Check if the attendance table exists
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='attendance';"
    )
    table_exists = cursor.fetchone()
    assert table_exists is not None, "Attendance table does not exist."

    # 2. Check for correct columns
    cursor.execute("PRAGMA table_info(attendance);")
    columns = cursor.fetchall()

    # Expected columns and their data types
    expected_columns = {"id": "INTEGER", "employee_id": "TEXT", "timestamp": "TEXT"}

    actual_columns = {
        column[1]: column[2] for column in columns
    }  # {column_name: data_type}

    for col, col_type in expected_columns.items():
        assert col in actual_columns, f"Column '{col}' is missing."
        assert (
            actual_columns[col] == col_type
        ), f"Column '{col}' has incorrect data type: expected {col_type}, got {actual_columns[col]}."

    # 3. Check for primary key constraint on 'id' column
    for column in columns:
        if column[1] == "id":
            assert column[5] == 1, "Primary key constraint is not set on 'id' column."

    conn.close()


# Create the table and run the test
if __name__ == "__main__":
    drop_attendance_table()  # Drop the table if it exists
    create_attendance_table()  # Create the table
    test_database_structure()  # Run the database structure test
    print("Database structure test passed successfully.")
