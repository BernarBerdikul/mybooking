import re


def trim_string(value):
    """method remove whitespaces in string, if string is not None"""
    double_whitespace = "  "
    if isinstance(value, str):
        if double_whitespace in value:
            return " ".join([word for word in value.strip().split()])
        return value.strip()
    elif value is not None:
        value = str(value)
        if double_whitespace in value:
            return " ".join([word for word in value.strip().split()])
        return value.strip()
    return value


def get_digits_from_string(value: str) -> str:
    """get [0-9]+ from value string and return another new"""
    return "".join([symbol for symbol in re.findall(r"[0-9]+", value)])
