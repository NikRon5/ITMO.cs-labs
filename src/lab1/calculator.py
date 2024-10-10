"""Module providing a function for doing calculations"""


def addition(a, b):
    """Function for calculating addition for two numbers"""
    try:
        return float(a) + float(b)
    except ValueError:
        return "Некорректные данные"
