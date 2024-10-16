from datetime import datetime


def is_valid_timestamp(timestamp_str):
    try:
        _ = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False


# Example usage:
input_str = "2024-10-09 15:30:00"
print(is_valid_timestamp(input_str))

invalid_input_str = "2024-13-40 99:99:99"
print(is_valid_timestamp(invalid_input_str))
