import numpy as np


def get_table_divided_diff(x_values, y_values):
    """
        Calculate the divided differences table.

        :param x_values: list of x coordinates of data points
        :param y_values: list of y coordinates of data points
        :return: divided differences table
        """
    n = len(x_values)
    table = np.zeros([n, n])
    table[:, 0] = y_values

    for j in range(1, n):
        for i in range(1, n):
            # formula for divided differences:
            # f[x0, x1, ..., xn] = (f[x1, ..., xn] - f[x0, ..., xn-1]) / (xn - x0)
            table[i, j] = (table[i, j - 1] - table[i - 1, j - 1]) / (x_values[i] - x_values[i - j])

    return table


def newton(diapason_x, values_y, x):
    """
        Perform Newton interpolation.

        :param diapason_x: list of x coordinates of data points
        :param values_y: list of y coordinates of data points
        :param x: x value at which to interpolate
        :return: interpolated y value
        """
    n = len(diapason_x)
    table = get_table_divided_diff(diapason_x, values_y)
    result = table[0, 0]

    for i in range(1, n):
        # product will be >>> (x - x0)...(x - xn)
        prod = 1
        for j in range(i):
            prod *= (x - diapason_x[j])
        # formula
        # Nn(x) = f[x0] + f[x0, x1](x - x0) + f[x0, x1, x2](x - x0)(x - x1) + ... + f[x0, ..., xn](x - x0)...(x - xn)
        result += table[i, i] * prod

    return result
