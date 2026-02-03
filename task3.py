import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number to international format.
    Keeps only digits and '+' at the beginning.
    Adds '+38' if country code is missing.

    :param phone_number: Phone number in any format
    :return: Normalized phone number
    """

    # Remove all characters except digits and '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    # If number starts with '380' but without '+', add '+'
    if cleaned.startswith("380"):
        cleaned = "+" + cleaned

    # If number does not start with '+', add '+38'
    elif not cleaned.startswith("+"):
        cleaned = "+38" + cleaned

    return cleaned
