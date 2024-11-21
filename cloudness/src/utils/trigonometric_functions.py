"""
This module provides trigonometric functions that can handle angles in both
degrees and radians.
"""

import numpy as np


def sin(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the sine of an angle

    Parameters
    ----------
    x : float
        The angle in degrees or radians
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The sine of the angle
    """
    if angle_in_degrees:
        x = np.deg2rad(x)
    return np.sin(x)


def cos(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the cosine of an angle

    Parameters
    ----------
    x : float
        The angle in degrees or radians
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The cosine of the angle
    """
    if angle_in_degrees:
        x = np.deg2rad(x)
    return np.cos(x)


def tan(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the tangent of an angle

    Parameters
    ----------
    x : float
        The angle in degrees or radians
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The tangent of the angle
    """
    if angle_in_degrees:
        x = np.deg2rad(x)
    return np.tan(x)


def sec(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the secant of an angle

    Parameters
    ----------
    x : float
        The angle in degrees or radians
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The secant of the angle
    """
    return 1 / cos(x, angle_in_degrees)


def csc(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the cosecant of an angle

    Parameters
    ----------
    x : float
        The angle in degrees or radians
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The cosecant of the angle
    """
    return 1 / sin(x, angle_in_degrees)


def cot(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the cotangent of an angle

    Parameters
    ----------
    x : float
        The angle in degrees or radians
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The cotangent of the angle
    """
    return 1 / tan(x, angle_in_degrees)


def arcsin(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the arcsine of a value

    Parameters
    ----------
    x : float
        The value
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The arcsine of the value
    """
    result = np.arcsin(x)
    if angle_in_degrees:
        result = np.rad2deg(result)
    return result


def arccos(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the arccosine of a value

    Parameters
    ----------
    x : float
        The value
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The arccosine of the value
    """
    result = np.arccos(x)
    if angle_in_degrees:
        result = np.rad2deg(result)
    return result


def arctan(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the arctangent of a value

    Parameters
    ----------
    x : float
        The value
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The arctangent of the value
    """
    result = np.arctan(x)
    if angle_in_degrees:
        result = np.rad2deg(result)
    return result


def arccot(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the arccotangent of a value

    Parameters
    ----------
    x : float
        The value
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The arccotangent of the value
    """
    return arctan(1 / x, angle_in_degrees)


def arcsec(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the arcsecant of a value

    Parameters
    ----------
    x : float
        The value
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The arcsecant of the value
    """
    return arccos(1 / x, angle_in_degrees)


def arccsc(x: float, angle_in_degrees: bool = True) -> float:
    """
    Calculate the arccosecant of a value

    Parameters
    ----------
    x : float
        The value
    angle_in_degrees : bool, optional
        If True, the angle is in degrees, otherwise in radians, by default True

    Returns
    -------
    float
        The arccosecant of the value
    """
    return arcsin(1 / x, angle_in_degrees)
