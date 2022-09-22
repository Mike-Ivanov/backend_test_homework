from math import sqrt


message = ("Добро пожаловать в самую лучшую программу для вычисления "
           "квадратного корня из заданного числа")


def calculate_square_root(number):
    """Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        message_2 = ("Введите число больше 0")
    else:
        root = {calculate_square_root(your_number)}
        message_2 = (f'Мы вычислили корень квадратный из введенного '
        f'вами числа. Это будет: {root}')
    print(message_2)


print(message)
calc(25.5)
