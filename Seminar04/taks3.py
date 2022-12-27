# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

from math import lcm
a = 4
b = 10
print(lcm(a,b))


a, b = 7, 5
i = max(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print(i)

