#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.


from random import randint

num = int(input("Размер массива: "))

numbers = []
for i in range(num):
    numbers.append(randint(-num, num + 1))



print("Элементы массива:", numbers)

x = int(input("Число x: "))

if x in numbers:
    print(f"Число {x} присутстует в списке")
else:
    print(f"Число {x} отсутствует в списке")
