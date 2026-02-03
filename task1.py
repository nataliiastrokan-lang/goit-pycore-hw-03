from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Calculates the number of days between the given date and today.

    :param date: Date in 'YYYY-MM-DD' format
    :return: Number of days between given date and today
    """
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - given_date
        return delta.days
    except ValueError:
        raise ValueError("Date must be in 'YYYY-MM-DD' format")