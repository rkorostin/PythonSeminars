# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

def inputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{inputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number

num1 = inputNumbers('Введите число 1:')
num2 = inputNumbers('Введите число 2:')
num3 = inputNumbers('Введите число 3:')
num4 = inputNumbers('Введите число 4:')
num5 = inputNumbers('Введите число 5:')

max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3
if num4 > max:
    max = num4
if num5 > max:
    max = num5
print (f'Введены числа {num1}', '; ' f'{num2}', '; ' f'{num3}', '; ' f'{num4}', '; ' f'{num5}')
print (f'Максимальное число {max}')