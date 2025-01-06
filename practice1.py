import math


def calculate_sqrt():
    # getting the amount from user
    x = float(input('x sqrt = '))
    # calculation of sqrt(e^(-x) + lnx + abs(1/cosx))
    return (math.sqrt((math.exp(-x)) + math.log(x) + math.fabs(1/math.cos(x))))


def calculate_expression():
    # getting the amount from user
    x = float(input('x expression = '))
    # calculation of e^(-x) + ln(x+1) + (cosx)
    return (math.exp(-x) + math.log(x+1) + math.cos(x))


def exponential():
    # getting two amounts from user
    x = float(input('x base = '))
    y = float(input('y power = '))
    # calculatint x**y
    resault = x**y
    # calculating the exp
    return math.exp(resault)


def trigonometric():
    # getting degree from user
    x = float(input('x trigonometric = '))
    theta = x*math.pi/180
    return math.sin(theta), math.cos(theta)


# calling our functions and saving the amounts
resault_sqrt = calculate_sqrt()
resault_expression = calculate_expression()
resault_exponential = exponential()
resault_trigonometric = trigonometric()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# showing amounts
print('the answer of sqrt:', resault_sqrt)
print('the answer of expression:', resault_expression)
print('the answer of exponential:', resault_exponential)
print('trigonometric (sin):',
      round(resault_trigonometric[0], 2), '\ntrigonometric (cos):', round(resault_trigonometric[1], 2))
