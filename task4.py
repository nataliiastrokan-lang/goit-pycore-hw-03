from datetime import datetime, date, timedelta


def get_upcoming_birthdays(users: list) -> list:
    """
    Returns a list of users whose birthdays occur within the next 7 days (inclusive),
    moving congratulation date to next Monday if birthday falls on a weekend.

    Input: users = [{"name": str, "birthday": "YYYY.MM.DD"}, ...]
    Output: [{"name": str, "congratulation_date": "YYYY.MM.DD"}, ...]
    """
    today = datetime.today().date()
    end_date = today + timedelta(days=7)

    upcoming = []

    for user in users:
        try:
            bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except (KeyError, ValueError, TypeError):
            # Skip invalid records (or you could raise an error)
            continue

        # Birthday date in the current year
        bday_this_year = date(today.year, bday.month, bday.day)

        # If birthday already passed this year, take next year
        if bday_this_year < today:
            bday_this_year = date(today.year + 1, bday.month, bday.day)

        # Check if birthday is within [today, today+7]
        if today <= bday_this_year <= end_date:
            congrat_date = bday_this_year

            # If Saturday (5) or Sunday (6) -> move to next Monday
            if congrat_date.weekday() == 5:      # Saturday
                congrat_date += timedelta(days=2)
            elif congrat_date.weekday() == 6:    # Sunday
                congrat_date += timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congrat_date.strftime("%Y.%m.%d")
            })

    return upcoming

