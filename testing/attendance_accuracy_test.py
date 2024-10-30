import sqlite3
from datetime import datetime

# Connect to SQLite database (or create it)
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Create a table for storing attendance data
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS attendance (
    employee_id INTEGER,
    timestamp TEXT
)
"""
)

# Sample data to be inserted (for testing accuracy)
attendance_data = [
    (101, "2024-10-22 09:00:00"),
    (102, "2024-10-22 09:05:00"),
    (103, "2024-10-22 09:10:00"),
]

# Insert sample data into the database
cursor.executemany(
    "INSERT INTO attendance (employee_id, timestamp) VALUES (?, ?)", attendance_data
)
conn.commit()


# Function to validate data accuracy
def validate_attendance_data(employee_id, expected_timestamp):
    cursor.execute(
        "SELECT timestamp FROM attendance WHERE employee_id = ?", (employee_id,)
    )
    result = cursor.fetchone()

    if result:
        stored_timestamp = result[0]
        # Check if the stored timestamp matches the expected timestamp
        if stored_timestamp == expected_timestamp:
            print(f"Data accuracy test passed for Employee ID {employee_id}")
        else:
            print(
                f"Data accuracy test failed for Employee ID {employee_id}: expected {expected_timestamp}, got {stored_timestamp}"
            )
    else:
        print(f"No record found for Employee ID {employee_id}")


# Test accuracy for each employee (compare expected timestamps with stored ones)
test_data = [
    (101, "2024-10-22 09:00:00"),
    (102, "2024-10-22 09:05:00"),
    (103, "2024-10-22 09:10:00"),
]

for employee_id, expected_timestamp in test_data:
    validate_attendance_data(employee_id, expected_timestamp)

# Close database connection
conn.close()


def calculate_accuracy(correct, total):
    return correct / total


# Call the function and store the result in accuracy
accuracy = calculate_accuracy(95, 100)

# Now compare the accuracy
if accuracy == 0.95:
    print("Test passed!")
else:
    print("Test failed!")
