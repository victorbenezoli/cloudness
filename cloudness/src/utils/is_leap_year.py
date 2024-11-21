"""
is_leap_year.py - Check if a year is a leap year

This module provides a function to check if a year is a leap year.

Functions
---------
is_leap_year(year: int) -> bool
    Check if a year is a leap year

Usage example
-------------
Check if the year 2020 is a leap year:

>>> from cloudness.utils import is_leap_year
>>> is_leap_year(2020)
True
"""

def is_leap_year(year: int) -> bool:
    """
    Check if a year is a leap year

    Parameters
    ----------
    year : int
        The year to check

    Returns
    -------
    bool
        True if the year is a leap year, False otherwise
    """
    if year < 0:
        raise ValueError("Year must be a positive integer.")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)