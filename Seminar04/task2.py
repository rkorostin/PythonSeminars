"""
Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
1)с помощью математических формул нахождения корней квадратного уравнения
2)с помощью дополнительных библиотек Python

"""

a = 1
b = -3
c = -4
# x1=4, x2=-1


def find_roots(a, b, c):
    roots = []
    D = b ** 2 - 4 * a * c
    if D < 0:
        roots.append('корней нет')
        return roots
    x1 = (-b - D ** 0.5) / 2 * a
    roots.append(x1)
    if D > 0:
        x2 = (-b + D ** 0.5) / 2 * a
        roots.append(x2)
    return roots

print(find_roots(a, b, c))


import math
def find_roots2(a, b, c):
    roots = []
    D = b ** 2 - 4 * a * c
    if D < 0:
        roots.append('корней нет')
        return roots
    x1 = (-b - math.sqrt(D)) / 2 * a
    roots.append(x1)
    if D > 0:
        x2 = (-b + math.sqrt(D)) / 2 * a
        roots.append(x2)
    return roots

print(find_roots2(a, b, c))



