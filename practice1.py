# calculation of sqrt(e^(-x) + lnx + abs(1/cosx))

import math


def calculate(x):
    return (math.sqrt((math.exp(-x)) + math.log(x) + math.fabs(1/math.cos(x))))


# getting the amount from user
x = float(input('x = '))
# calling the function for calculation
resault = calculate(x)
print(resault)
