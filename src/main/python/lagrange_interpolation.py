def lagrange(diapason_x, values_y, x):
    """
        Perform Lagrange interpolation.

        :param diapason_x: list of x coordinates of data points
        :param values_y: list of y coordinates of data points
        :param x: x value at which to interpolate
        :return: interpolated y value
        """
    result = 0
    iterations = len(diapason_x)
    for i in range(iterations):
        L = 1
        for j in range(iterations):
            if j != i:
                # formula (x - x1)(x - x2)...(x - xn)
                #         (x0 - x1)(x0 - x2)...(x-xn) multiplied n times
                L *= (x - diapason_x[j]) / (diapason_x[i] - diapason_x[j])
        # formula Ln(x) = sum of y0 times (x - x1)(x - x2)...(x - xn)
        #                                 (x0 - x1)(x0 - x2)...(x-xn) multiplied n times
        result += values_y[i] * L
    return result
