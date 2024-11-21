"""
This module provides classes and functions to calculate solar irradiance.

Classes
-------
Irradiance
    A class to calculate solar irradiance

Exceptions
----------
DayOfYearError
    Exception raised when the day of the year is invalid

Notes
-----
The following formulas are used to calculate solar irradiance:

1. Declination angle (delta) in degrees:
    delta = 23.45 * sin(360/ndays * (284 + day_of_year))

2. Sunset hour angle (h) in degrees:
    h = arccos(-tan(latitude) * tan(delta))

3. Earth-Sun distance (e0) in astronomical units:
    e0 = 1.000110 + 0.34221 * cos(X) + 0.01280 * sin(X) + 0.000719 * cos(2X) + 0.000077 * sin(2X)
    where X = 2 * pi * (day_of_year - 1) / ndays

4. Extraterrestrial solar radiation (Ra) in MJ/m^2:
    Ra = 37.60 * e0 * (h * sin(latitude) * sin(delta) + cos(latitude) * cos(delta) * sin(h))

5. Convert solar radiation from MJ/m^2 to W/m^2:
    W/m^2 = MJ/m^2 * 1000000 / 86400
"""

import numpy as np
from cloudness.src.utils import trigonometric_functions as tf
from cloudness.src.utils.is_leap_year import is_leap_year


class DayOfYearError(Exception):
    """
    Exception raised when the day of the year is invalid
    """
    def __init__(self, day_of_year: int, ndays: int) -> None:
        self.day_of_year = day_of_year
        self.ndays = ndays
        self.message = (
            f"Day of year must be between 1 and {ndays}. Got {day_of_year}."
        )
        super().__init__(self.message)


class Irradiance:
    """
    A class to calculate solar irradiance

    Attributes
    ----------
    latitude : float
        The latitude of the location in degrees
    ndays : int
        The number of days in a year

    Methods
    -------
    declination_angle(day_of_year: int) -> float
        Calculate the declination angle of the sun in degrees
    sunset_hour_angle(day_of_year: int) -> float
        Calculate the sunset hour angle in degrees
    earth_sun_distance(day_of_year: int) -> float
        Calculate the Earth-Sun distance in astronomical units
    extraterrestrial_solar_radiation(day_of_year: int) -> float
        Calculate the extraterrestrial solar radiation in MJ/m^2 for a given
        day of the year
    """
    def __init__(self, latitude: float, year: int) -> None:
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude must be between -90 and 90 degrees.")
        self.latitude = latitude
        self.ndays = 366 if is_leap_year(year) else 365

    def declination_angle(self, day_of_year: int) -> float:
        """
        Calculate the declination angle of the sun in degrees

        Returns
        -------
        float
            The declination angle of the sun in degrees
        """
        if day_of_year < 1 or day_of_year > self.ndays:
            raise DayOfYearError(day_of_year, self.ndays)
        return 23.45 * tf.sin((360 / self.ndays) * (284 + day_of_year))

    def sunset_hour_angle(self, day_of_year: int) -> float:
        """
        Calculate the sunset hour angle in degrees

        Returns
        -------
        float
            The sunset hour angle in degrees
        """
        if day_of_year < 1 or day_of_year > self.ndays:
            raise DayOfYearError(day_of_year, self.ndays)
        delta = self.declination_angle(day_of_year)
        return np.arccos(-tf.tan(self.latitude) * tf.tan(delta))

    def earth_sun_distance(self, day_of_year: int) -> float:
        """
        Calculate the Earth-Sun distance in astronomical units

        Returns
        -------
        float
            The Earth-Sun distance in astronomical units
        """
        if day_of_year < 1 or day_of_year > self.ndays:
            raise DayOfYearError(day_of_year, self.ndays)
        X = 2 * np.pi * (day_of_year - 1) / self.ndays
        return (
            1.000110
            + 0.34221 * tf.cos(X)
            + 0.01280 * tf.sin(X)
            + 0.000719 * tf.cos(2 * X)
            + 0.000077 * tf.sin(2 * X)
        )

    def extraterrestrial_solar_radiation(self, day_of_year: int) -> float:
        """
        Calculate the extraterrestrial solar radiation in MJ/m^2 for a given
        day of the year

        Parameters
        ----------
        day_of_year : int
            The day of the year

        Returns
        -------
        float
            The extraterrestrial solar radiation in MJ/m^2
        """
        if day_of_year < 1 or day_of_year > self.ndays:
            raise DayOfYearError(day_of_year, self.ndays)
        delta = self.declination_angle(day_of_year)
        e0 = self.earth_sun_distance(day_of_year)
        h = self.sunset_hour_angle(day_of_year)

        first_term = h * tf.sin(self.latitude) * tf.sin(delta)
        second_term = tf.cos(self.latitude) * tf.cos(delta) * np.sin(h)
        return 37.60 * e0 * (first_term + second_term)

    @staticmethod
    def to_watts_per_m2(mj_per_m2: float) -> float:
        """
        Convert solar radiation from MJ/m^2 to W/m^2

        Parameters
        ----------
        mj_per_m2 : float
            The solar radiation in MJ/m^2

        Returns
        -------
        float
            The solar radiation in W/m^2
        """
        return mj_per_m2 * 1000000 / 86400
