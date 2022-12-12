"""1)Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
10 чисел в диапазоне от 2 до 5
"""

from random import randint

numbers = []
for i in range(11):
    numbers.append(randint(2, 5))
print(numbers)

count = 0
for i in numbers:
    temp = numbers.count(i)
    if count < temp:
        count = temp
print(count)

# numbers2 = []
# for i in numbers:
#     numbers2.append(numbers.count(i))
# print(numbers2)


# count = 0
# for i in range(len(numbers)-1):
#     if numbers[i] == numbers.count(len(numbers)-1):
#         count += 1
#
# print(count)

"""
2)Данная программа должна вывести n рядов, заполненных знаком ‘*’ определенным образом. А именно: в первом ряду должно быть n «звездочек», в втором n-1, и так далее. А в последнем ряду таким образом будет одна «звездочка». Причем убывать эти «звездочки» должны слева направо. Число n вводится пользователем.
Введите количество рядов: 5
*****
****
***
**
*

count = int(input())
for i in range(count,0,-1):
    print("*"*i)
"""

import random

a = 1
b = 6

array = [random.randint(a, b) for i in range(20)]
print(array)

d = {}

for i in array:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

max = 0
for i in range(a, (b + 1)):
    if (d[i] > max):
        max = d[i]

print(f"Максимальное повторение элемента {max} раз.")



# import random
#
# list_num = []
# max = 0
# for i in range(10):
#     a= random.randint(2,5)
#     list_num.append(a)
# print(list_num)
# print(set(list_num))
# for i in set(list_num):
#     if list_num.count(i)>max:
#         max = list_num.count(i)
# print(max)


import random

a = 1
b = 6

array = [random.randint(a, b) for i in range(20)]
print(array)

print(set(array))
d = {}

for i in array:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

max = 0
for i in range(a, (b + 1)):
    if (d[i] > max):
        max = d[i]

print(f"Максимальное повторение элемента {max} раз.")


import random

number = int(input())
maxRandom = int(input('input max random number'))
maxAmount = 0

list = []
count = [0] * (maxRandom+1)

for i in range(0, number):
    list.append(random.randint(0, maxRandom))

for i in list:
    count[int(i)] += 1

for i in count:
    if i > maxAmount:
        i = maxAmount

print(list)
print(max(count))
print('МАскимально количество раз появилась ' + str(count[maxAmount]) + ', ' + str(maxAmount+1) + ' раз')

