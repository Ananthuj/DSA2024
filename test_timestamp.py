from datetime import datetime


def is_valid_timestamp(timestamp_str):
    try:
        # Define the expected format of the timestamp
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return True  # Return True if valid
    except ValueError:
        return False  # Return False if invalid


# Example usage:
input_str = "2024-10-09 15:30:00"
print(is_valid_timestamp(input_str))  # Output: True

invalid_input_str = "2024-13-40 99:99:99"
print(is_valid_timestamp(invalid_input_str))  # Output: False


from datetime import datetime


def test_timestamp(timestamp_str):
    try:
        # Define the expected format of the timestamp
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        # Format the timestamp to calendar time (e.g., October 9, 2024, 3:30 PM)
        calendar_time = timestamp.strftime("%B %d, %Y, %I:%M %p")
        return True, calendar_time  # Return True and the formatted calendar time
    except ValueError:
        return False, None  # Return False if invalid


# Example usage:
input_str = "2024-10-09 15:30:00"
is_valid, calendar_time = test_timestamp(input_str)
print(f"Is valid: {is_valid}, Calendar Time: {calendar_time}")

invalid_input_str = "2024-13-40 99:99:99"
is_valid, calendar_time = test_timestamp(invalid_input_str)
print(f"Is valid: {is_valid}, Calendar Time: {calendar_time}")
