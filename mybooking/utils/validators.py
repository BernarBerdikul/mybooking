from datetime import datetime


def time_format_validation(value: str):
    try:
        datetime.strptime(value, "%H:%M")
        return True
    except ValueError:
        return False


# print(time_format_validation(value="13:40"))
# print(time_format_validation(value="sdfs"))
