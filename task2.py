import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Generates a sorted list of unique random numbers for a lottery ticket.

    :param min: Minimum possible number (>= 1)
    :param max: Maximum possible number (<= 1000)
    :param quantity: Amount of numbers to generate
    :return: Sorted list of unique numbers or empty list if parameters are invalid
    """

    # Validation
    if min < 1 or max > 1000 or min > max:
        return []

    if quantity < 1 or quantity > (max - min + 1):
        return []

    # Generate unique numbers
    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)

