import numpy as np
from matplotlib import pyplot as plt


def plot_function(function, diapason1, diapason2, x_i, lagrange_result1, lagrange_result2, newton_result1,
                  newton_result2):
    x_values = np.linspace(-10, 2, 100)
    y_values = function(x_values)

    plt.plot(x_values, y_values, label="e^x + x")

    plt.grid(True)

    plt.title("$f(x) = e^x + x$")

    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.axvline(x=x_i, color='red', linestyle='--')

    plt.scatter(diapason1[0], function(diapason1[0]), color='pink')
    plt.scatter(diapason1[1], function(diapason1[1]), color='pink')
    plt.scatter(diapason1[2], function(diapason1[2]), color='pink')
    plt.scatter(diapason2[2], function(diapason2[2]), color='pink')
    plt.scatter(diapason1[3], function(diapason1[3]), color='pink')
    plt.scatter(x_i, function(x_i), color='pink')

    plt.scatter(x_i, lagrange_result1, color='red', label=f'Interpolation {diapason1} (Lagrange)')
    plt.scatter(x_i, lagrange_result2, color='red', label=f'Interpolation {diapason2} (Lagrange)')
    plt.scatter(x_i, newton_result1, color='green', label=f'Interpolation {diapason1} (Newton)')
    plt.scatter(x_i, newton_result2, color='green', label=f'Interpolation {diapason2} (Newton)')

    plt.legend()
    plt.show()
