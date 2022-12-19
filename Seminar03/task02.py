


num = int(input("Размер массива: "))
given_list = [i for i in range(-num, num + 1)]

N = int(input("Размер массива: ")) # Вводим размер массива
print("Элементы массива:")
lst = [int(input()) for i in range(N)] # Вводим элементы массива
x = int(input("Число x: ")) # Вводим число x

# Проверяем наличие числа в массиве
if x in lst:
    print("YES")
else:
    print("NO")