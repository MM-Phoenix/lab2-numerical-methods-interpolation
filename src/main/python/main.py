from logics import get_string_function_value, get_values_y, get_error, decorate, get_function_value
from lagrange_interpolation import lagrange
from newton_interpolation import newton

from graph_matplotlib import plot_function
import math


# var 17:
# f(x) = e^x + x
# first diapason [-2, -1, 0, 1]
# second diapason [-2, -1, 0.2, 1]
# X = 0.5


# CONSTANTS
# f(x) = e^x + x
def FUNCTION_17(x): return math.e ** x + x


DIAPASON_X1 = [-2, -1, 0, 1]
VALUES_Y1 = get_values_y(FUNCTION_17, DIAPASON_X1)

DIAPASON_X2 = [-2, -1, 0.2, 1]
VALUES_Y2 = get_values_y(FUNCTION_17, DIAPASON_X2)

X_i = 0.5
FUNCTION_RESULT_X_i = get_function_value(X_i, FUNCTION_17)
STRING_RESULT_X_i = get_string_function_value(X_i, FUNCTION_17)

string_function = "e^x + x"

# description
decorate()
print("Welcome to the interpolation calculator!".upper())
decorate()
print("We have the variant 17 - function is: ")
print(string_function)
print("The first diapason is [-2, -1, 0, 1]")
print("The second diapason is [-2, -1, 0.2, 1]")

decorate()
print("LAGRANGE INTERPOLATION")
decorate()

# DEMONSTRATION OF THE LAGRANGE INTERPOLATION FOR FIRST DIAPASON
print("DEMONSTRATION OF THE LAGRANGE INTERPOLATION FOR FIRST DIAPASON")
lagrange_result1 = lagrange(DIAPASON_X1, VALUES_Y1, X_i)
print(f"Lagrange interpolation for diapason {DIAPASON_X1} is {lagrange_result1}")
print(STRING_RESULT_X_i)
lagrange_result1_error = get_error(FUNCTION_RESULT_X_i, lagrange_result1)
print(f"Lagrange error is {lagrange_result1_error}")

# DEMONSTRATION OF THE LAGRANGE INTERPOLATION FOR FIRST DIAPASON
print("\nDEMONSTRATION OF THE LAGRANGE INTERPOLATION FOR SECOND DIAPASON")
lagrange_result2 = lagrange(DIAPASON_X2, VALUES_Y2, X_i)
print(f"Lagrange interpolation for diapason {DIAPASON_X2} is {lagrange_result2}")
print(STRING_RESULT_X_i)
lagrange_result2_error = get_error(FUNCTION_RESULT_X_i, lagrange_result2)
print(f"Lagrange error is {lagrange_result2_error}")

decorate()
print("NEWTON INTERPOLATION")
decorate()
print("DEMONSTRATION OF THE NEWTON INTERPOLATION FOR FIRST DIAPASON")
newton_result1 = newton(DIAPASON_X1, VALUES_Y2, X_i)
print(f"Newton interpolation for diapason {DIAPASON_X1} is {newton_result1}")
print(STRING_RESULT_X_i)
newton_result1_error = get_error(FUNCTION_RESULT_X_i, newton_result1)
print(f"Newton error is {newton_result1_error}")

print("\nDEMONSTRATION OF THE NEWTON INTERPOLATION FOR SECOND DIAPASON")
newton_result2 = newton(DIAPASON_X2, VALUES_Y2, X_i)
print(f"Newton interpolation for diapason {DIAPASON_X2} is {newton_result2}")
print(STRING_RESULT_X_i)
newton_result2_error = get_error(FUNCTION_RESULT_X_i, newton_result2)
print(f"Newton error is {newton_result2_error}")

decorate()

plot_function(FUNCTION_17, DIAPASON_X1, DIAPASON_X2, X_i, lagrange_result1, lagrange_result2, newton_result1,
              newton_result2)
