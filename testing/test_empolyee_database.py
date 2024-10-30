import sqlite3
import unittest


# Database setup function (for testing purposes)
def setup_database():
    connection = sqlite3.connect("employee_test.db")
    cursor = connection.cursor()

    # Create employee table if it doesn't exist
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS employee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT
    )
    """
    )

    connection.commit()
    return connection


# Function to add a new employee
def add_employee(connection, name, age, department):
    cursor = connection.cursor()
    cursor.execute(
        """
    INSERT INTO employee (name, age, department)
    VALUES (?, ?, ?)
    """,
        (name, age, department),
    )

    connection.commit()


# Test case for database testing
class TestEmployeeDatabase(unittest.TestCase):

    def setUp(self):
        # Set up a fresh database connection for each test
        self.connection = setup_database()

    def tearDown(self):
        # Close the database connection after each test
        self.connection.close()

    def test_add_employee(self):
        """Test if a new employee is correctly added to the employee table."""

        # Expected employee data
        new_employee = ("John Doe", 30, "Engineering")

        # Add the employee to the database
        add_employee(self.connection, *new_employee)

        # Query the database to check if the employee is added
        cursor = self.connection.cursor()
        cursor.execute(
            """
        SELECT name, age, department
        FROM employee
        WHERE name = ? AND age = ? AND department = ?
        """,
            new_employee,
        )

        result = cursor.fetchone()

        # Assert that the result matches the expected data
        self.assertIsNotNone(result)
        self.assertEqual(result, new_employee)


if __name__ == "__main__":
    unittest.main()
