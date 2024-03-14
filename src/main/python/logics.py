def get_string_function_value(x, function):
    if isinstance(x, type(None)):
        return f"Cannot determine the value at f({x})"
    else:
        return f"f({x}) = {function(x)}"


def get_function_value(x, function):
    if isinstance(x, type(None)):
        return None
    else:
        return function(x)


def get_values_y(function, diapason_x):
    values_y = []
    for i in range(len(diapason_x)):
        values_y.append(function(diapason_x[i]))
    return values_y


def get_error(theoretical, measured):
    return abs(measured - theoretical)


def decorate():
    print("- * " * 20)
