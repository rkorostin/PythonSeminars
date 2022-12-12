"""
Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
*Пример: *
Для N = 5: 1, -3, 9, -27, 81
"""
#
# num = int(input("Введите число N:"))
#
# list=list(range(1, num+1))
# # print(list)
#
#
#
# # list = [1]
# list2=[]
# for i in list:
#     result = list[i] * -3
#     list2.append(result)
#
# print(list2)


# count = int(input("введите количество членов: "))
# save = 1
# for i in range(1, count + 1):
#     save *= 3
#     if i == 1:
#         print(save / 3)
#     elif i % 2 == 0:
#         print(-1 * (save / 3))
#     else:
#         print(save / 3)

"""
12. Для натурального n создать словарь индекс - значение, состоящий из элементов последовательности 3n + 1.

*Пример: *

- Для
n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# n = int(input())
# a = {}
# for i in range(1,n+1):
#     a[i] = i*3+1
# print(a)


#13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
one = input()
two = input()
# count = 0
# for i in range(len(one)-len(two)+1):
#     if one[i:i+len(two)] == two:
#         count += 1
# print(count)
print(one.count(two))




