b = float(input('Введите первую сторону треугольника:'))
c = float(input('Введите вторую сторону треугольника:'))
corner = float(input('Введите угол между ними:'))

from math import *

corner = radians(corner)

result = sqrt(b**2 + c**2 - 2*b*c * cos(corner))

print(result)