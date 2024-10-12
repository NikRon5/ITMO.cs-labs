"""Module providing a function for doing calculations"""

def calculate(a, b, oper):
    """Function for calculating two numbers"""
    try:
        if oper == "+":
            return round(float(a) + float(b), 5)
        if oper == "-":
            return round(float(a) - float(b), 5)
        if oper == "*":
            return round(float(a) * float(b), 5)
        if oper == "/":
            if float(b) == 0: return "Деление на ноль"
            return round(float(a) / float(b), 5)
    except ValueError:
        return "Некорректные данные"

